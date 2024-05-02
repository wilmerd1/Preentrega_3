## Proyecto CoderHouse

Comisión: 54135
Alumno: Wilmer Andres Duque Olaya

## Acerca del proyecto

La idea es una aplicación de Ecommerce, pero la parte de administración, donde se podran dar de alta los clientes, productos y categorias, pedidos y consultar los envios con sus estados.


Se creo una aplicación core donde contiene los archivos estaticos (html, css, js) y principales de la aplicación, donde el template base en encarga de enviar la plantilla principal del NavBar para todas las demás aplicaciones..



1. Inicialmente en la pestaña principal esta cargada la tabla de Categorias
2. Se crear la categoria y su tipo, se mostrara automaticamente en la tabla actualizando la vista (Pendiente mostrar alerta de error o creación satisfactoria)
3. Se creo un formulario de productos, donde la categoria a partir de la relación entre las tablas de Categoria y Producto. (Pendiente mejorar la consulta de la tabla)


## Aplicaciones

Se creo la aplicación principal Ecommerce, que contiene actualmente 5 modelos relacionados

## Modelos
los modelos tienen relación entre con llaves principales y foraneas

Cliente
CategoriaProducto
Producto
Delivery
Pedido

## Mejoras Futuras
1. Mejorar la interfaz visual, en la pagina principal cargar con imagenes los productos, cambiar el estado del active de acuerdo con la selección del Nabvar
2. Manejo de permisos a nivel de autenticación
3. Inicio de sesión para manejar quien puede hacer CRUD a las tablas.

## Problemas conocidos

1. Carga de la tabla de Productos
2. Grabación de Clientes con el forms
3. Validaciones y restricciones a nivel de forms y base de datos
4. Direcciones URL en la navegación