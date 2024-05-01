from django.contrib import admin
from .models import Cliente, Categoriaproducto, Producto, Delivery, Pedido

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Categoriaproducto)
admin.site.register(Producto)
admin.site.register(Delivery)
admin.site.register(Pedido)