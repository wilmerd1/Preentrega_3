from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models, forms
from django.views.generic import CreateView
from django.views.generic import ListView


# Create your views here.


def categorias(request):
    query = models.Categoriaproducto.objects.all()
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ecommerce:categorias')
    else:
        form = forms.CategoriaForm()
    contexto = {"categorias":query,"form": form}
    return render(request, "ecommerce/categorias.html", contexto)

def productos(request):

    pruductos = models.Producto.objects.all()
    contexto= {'productos': pruductos}

    return render(request, "ecommerce/productos.html", contexto)

def clientes(request):
    query = models.Cliente.objects.all()
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ecommerce:clientes')
    else:
        form = forms.ClienteForm()
    contexto = {"clientes":query,"form": form}
    return render(request, "ecommerce/clientes.html", contexto)

class ProductosCreateView(CreateView):
    model = models.Producto
    template_name = "ecommerce/productos.html"
    form_class = forms.ProductosForm
    success_url = '.'
    


class ClientesList(ListView):
    model = models.Cliente