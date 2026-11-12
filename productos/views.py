from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from .models import Producto

# IA: [Diferenciación de flujo de ejecución entre FBV y CBV con inyección de contexto adicional]
# Solución manual: [Se implementó la vista basada en funciones 'home' para la página de bienvenida con métricas agregadas mediante ORM, y la vista basada en clases 'ProductoListView' sobreescribiendo get_context_data() para inyectar listas de categorías y marcas de tiempo sin romper la convención de ListView].

def home(request):
    """
    Function-Based View (FBV) para la página de inicio.
    Maneja el ciclo de solicitud-respuesta mediante la función render() y envía un contexto enriquecido.
    """
    total_productos = Producto.objects.count()
    productos_disponibles = Producto.objects.filter(disponible=True, stock__gt=0).count()
    ultimos_productos = Producto.objects.filter(disponible=True)[:3]
    categorias_activas = Producto.objects.values_list('categoria', flat=True).distinct()

    context = {
        'titulo_seccion': 'Panel de Inicio y Métricas del Catálogo',
        'total_productos': total_productos,
        'productos_disponibles': productos_disponibles,
        'ultimos_productos': ultimos_productos,
        'categorias': categorias_activas,
        'fecha_servidor': timezone.now(),
        'estudiante': 'Suárez Román, Arlette',
        'curso': 'Desarrollo de Aplicaciones Web (IS093A)',
    }
    return render(request, 'productos/home.html', context)


class ProductoListView(ListView):
    """
    Class-Based View (CBV) que hereda de ListView para renderizar el catálogo.
    Aplica evaluación perezosa (lazy evaluation) del QuerySet y gestión de contexto vía get_context_data().
    """
    model = Producto
    template_name = 'productos/catalogo.html'
    context_object_name = 'productos'
    paginate_by = 6

    def get_queryset(self):
        """
        Sobrescritura para permitir filtrado opcional mediante parámetro GET o argumento de URL.
        Demuestra el uso de objects.all() y filter().
        """
        queryset = Producto.objects.all()
        categoria = self.kwargs.get('categoria') or self.request.GET.get('categoria')
        busqueda = self.request.GET.get('q')

        if categoria:
            queryset = queryset.filter(categoria__iexact=categoria)
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Extiende el diccionario de contexto para proveer metadatos a la plantilla.
        """
        context = super().get_context_data(**kwargs)
        context['titulo_catalogo'] = 'Catálogo Oficial de Productos - Arquitectura MTV'
        context['categoria_seleccionada'] = self.kwargs.get('categoria') or self.request.GET.get('categoria', 'Todas')
        context['total_resultados'] = self.get_queryset().count()
        context['todas_categorias'] = Producto.objects.values_list('categoria', flat=True).distinct()
        context['fecha_consulta'] = timezone.now()
        return context
