from django.test import TestCase, Client
from django.urls import reverse
from .models import Producto

class ProductoModelAndViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.prod1 = Producto.objects.create(
            nombre="Laptop Lenovo Legion 5",
            descripcion="Laptop gamer de alta performance",
            precio=4500.00,
            stock=10,
            categoria="Laptops",
            disponible=True
        )
        self.prod2 = Producto.objects.create(
            nombre="Mouse Logitech G203",
            descripcion="Mouse gamer RGB",
            precio=99.00,
            stock=0,
            categoria="Periféricos",
            disponible=False
        )

    def test_modelo_str_y_propiedades(self):
        """Verifica el método __str__ y la propiedad en_stock."""
        self.assertIn("Laptop Lenovo Legion 5", str(self.prod1))
        self.assertTrue(self.prod1.en_stock)
        self.assertFalse(self.prod2.en_stock)

    def test_fbv_home_view(self):
        """Verifica la respuesta 200 y el contexto inyectado en la FBV home."""
        url = reverse('productos:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productos/home.html')
        self.assertEqual(response.context['total_productos'], 2)
        self.assertEqual(response.context['productos_disponibles'], 1)

    def test_cbv_catalogo_list_view(self):
        """Verifica la respuesta 200 y el comportamiento de la CBV ProductoListView."""
        url = reverse('productos:catalogo')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productos/catalogo.html')
        self.assertEqual(len(response.context['productos']), 2)

    def test_cbv_filtro_categoria(self):
        """Verifica el filtrado de QuerySets por categoría en la CBV."""
        url = reverse('productos:catalogo_categoria', kwargs={'categoria': 'Laptops'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['productos']), 1)
        self.assertEqual(response.context['productos'][0].nombre, "Laptop Lenovo Legion 5")
