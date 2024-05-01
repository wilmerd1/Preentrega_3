from django.db import models
from django.urls import reverse

# Create your models here.
'''
    Modelo para la tabla cliente
'''

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    direccion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self) -> str:
        return self.name
    

class Categoriaproducto(models.Model):
    categoria_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)

    class Meta:
        
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categoria_detail", kwargs={"pk": self.pk})


class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    categoria_id = models.ForeignKey("categoriaproducto", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("producto_detail", kwargs={"pk": self.pk})


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True, unique=True)
    tipo = models.CharField(max_length=200)
    estatus = models.CharField(max_length=200)

    class Meta:
        verbose_name = "delivery"
        verbose_name_plural = "deliveries"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("delivery_detail", kwargs={"pk": self.pk})


class Pedido(models.Model):
    pedido_id = models.AutoField(primary_key=True, unique=True)
    date = models.DateTimeField()
    status = models.CharField(max_length=200)
    delivery_id = models.ForeignKey("Delivery", on_delete=models.CASCADE)
    cliente_id = models.ForeignKey("Cliente", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return reverse("pedido_detail", kwargs={"pk": self.pk})
