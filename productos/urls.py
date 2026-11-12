from django.urls import path
from . import views

# IA: [Resolución inversa de URLs y desacoplamiento con app_name]
# Solución manual: [Se definió el namespace app_name = 'productos' para garantizar reversibilidad limpia mediante {% url 'productos:nombre' %}, evitando cadenas absolutas hardcodeadas en plantillas y vistas].

app_name = 'productos'

urlpatterns = [
    # FBV: Página principal de bienvenida
    path('', views.home, name='home'),

    # CBV: Catálogo completo de productos
    path('catalogo/', views.ProductoListView.as_view(), name='catalogo'),

    # CBV: Catálogo filtrado por categoría mediante parámetro de URL
    path('catalogo/categoria/<str:categoria>/', views.ProductoListView.as_view(), name='catalogo_categoria'),
]
