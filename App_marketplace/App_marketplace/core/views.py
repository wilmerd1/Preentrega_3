from django.shortcuts import render
from Ecommerce.models import Categoriaproducto
# Create your views here.
def home(request):
    categoria = Categoriaproducto.objects.all()
    contexto= {'categorias': categoria}
    return render(request, 'core/index.html', contexto)
