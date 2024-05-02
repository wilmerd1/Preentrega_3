from django.contrib import admin
admin.autodiscover()

from django.urls import path
from . import views

app_name = "Ecommerce"
urlpatterns = [
    path("categorias/", views.categorias, name="categorias"),
    path("clientes/", views.clientes, name="clientes"),
    path("productos/", views.ProductosCreateView.as_view(), name="productos"),
]
