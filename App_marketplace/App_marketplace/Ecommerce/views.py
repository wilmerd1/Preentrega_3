from django.shortcuts import render
from . import models

# Create your views here.


def home(request):
    query = models.Categoriaproducto.objects.all()
    contexto = {"categorias": query}
    return render(request, 'ecommerce/index.html', contexto)
