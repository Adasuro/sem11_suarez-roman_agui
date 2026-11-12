from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio', 'stock', 'disponible', 'fecha_creacion')
    list_filter = ('categoria', 'disponible', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion', 'categoria')
    list_editable = ('precio', 'stock', 'disponible')
    ordering = ('-fecha_creacion',)
