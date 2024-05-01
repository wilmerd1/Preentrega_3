## Creación superuser Django user: 
admin 123


## Pasos despues de crear la APP
1. Config -> Settings se agrega la app en INSTALLED_APP
2. Config -> Path con "", include('app.urls')
3. App -> crear url.py  ... import views path ('', views.home, name='home')  --> Home es el nombre de la funcion o metodo
4. App -> Views  crear función  def home(request) return render(request, 'RUTA HTML')
5. App -> Carpeta Templates -> HTML
6. App -> models -> se crea la clase que es como la tabla con sus atributos class nombre_clase(models.Model)
7. migrar base de datos - makamigrations
8. crear la base de datos - migrate __nombreApp__

## Mostrar modelo de la base de datos
1. Ecommerce -> admin se agregan las clases admin.site.register(clase)

# Mostrar en la pagina web
1. views . importar clase

