from django.db import models

# IA: [Validación de precisión decimal y representación textual en modelos ORM]
# Solución manual: [Se implementó DecimalField con max_digits=10 y decimal_places=2 para evitar imprecisiones de punto flotante en transacciones monetarias, junto con el método __str__ para legibilidad en el administrador de Django y depuración en consola].

class Producto(models.Model):
    """
    Modelo representativo de la entidad Producto en la base de datos relacional SQLite.
    Aplica el ORM de Django con validaciones a nivel de esquema y nombres descriptivos.
    """
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Producto")
    descripcion = models.TextField(blank=True, verbose_name="Descripción detallada")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio unitario (S/.)")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock disponible")
    categoria = models.CharField(max_length=80, default="Tecnología", verbose_name="Categoría")
    disponible = models.BooleanField(default=True, verbose_name="Estado de disponibilidad")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de ingreso")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última modificación")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - S/. {self.precio:.2f}"

    @property
    def en_stock(self):
        """Método de negocio encapsulado en el modelo (evitando lógica en vistas)."""
        return self.stock > 0 and self.disponible
