from django.contrib.admin.widgets import AutocompleteSelect
from django import forms

from .admin import admin
from .models import Categoriaproducto,  Producto, Cliente

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoriaproducto
        fields = ('name', 'tipo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'type': 'text'
        })
        self.fields['tipo'].widget.attrs.update({
            'class': 'form-control',
            'type': 'text'
        })

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields =    ("name", "precio", "descripcion","categoria_id")
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "categoria_id":forms.Select(attrs={"class": "form-select mb-3"}) 
        }
            

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('name', 'apellido', 'email', 'direccion')

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
        }