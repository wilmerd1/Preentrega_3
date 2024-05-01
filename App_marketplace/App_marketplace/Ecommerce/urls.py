from django.urls import path
app_name = 'Ecommerce'
from . import views
urlpatterns = [
    
    path('', views.home, name='home'),
]
