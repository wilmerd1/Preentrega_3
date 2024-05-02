from django.contrib import admin
from .models import Cliente, Categoriaproducto, Producto, Delivery, Pedido

# Register your models here.

class CategoriaproductoAdmin(admin.ModelAdmin):
    search_fields = ("name"),
    ordering = ['name']


class ProductoAdmin(admin.ModelAdmin):
    ordering = ['name']
    autocomplete_fields = ['categoria_id']
    

admin.site.register(Cliente)
admin.site.register(Categoriaproducto, CategoriaproductoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Delivery)
admin.site.register(Pedido)
