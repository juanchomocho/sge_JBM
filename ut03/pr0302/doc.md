[Tema03](../index.md)

# PR0301: Facturas con Odoo

--- 
[PR0302](https://vgonzalez165.github.io/apuntes_sge/ut03_implantacion/pr0302.html)
En esta practica aperenderemos a usar una parte del módulo de **Inventario** en concreto la utilizacion de google imagenes para cargar automaticamente las imagenes de los productos.

## Paso 1:
Buscamos dentro de las aplicaciones el módulo de **inventario** y lo activamos 
![paso1](./inv1.png)

## Paso 2:
Entramos en el módulo de inventario dentro de **productos** e importamos el [archivo](./libros.xls) con los libros en el módulo.
![paso2](./inv2.png)

## Paso 3:
Ahora tenermos que habilitar la busqueda de google imagenes, para esto entramos en **Google APIs** y servicios y nos registramos para poder acceder al dashboard.
![paso3](./inv3.png)

## Paso 4:
Creamos un proyecto y nos vamos al apartado de credenciales para crear una **API** Key. Aqui crearemos un nuevo proyecto, en este caso le he puesto Proyecto JBM.
![paso4.1](./inv4.1.png)
Acto seguido nos vamos a credenciales, pinchamos en crear credenciales y luego clave **API**, Nos crea la clave(que no voy a mostrar) y ya la tenemos.
![paso4.2](./inv4.2.png)
Pinchamos en la barra de busqueda y buscamos custom shearch **API**, pinchamos en el primer resultado y la habilitamos.
![paso4.3](./inv4.3.png)

## Paso 5:
Ahora debemos asignar un *motor de busqueda* para esto iremos a esta [página](https://programmablesearchengine.google.com/about/) y pincharemos en **get Started** y luego en **añadir**.
![paso5.1](./inv5.1.png)
![paso5.2](./inv5.2.png)
Configuramos el *motor de busqueda* tal y como se muestra, puede buscar imágenes ahora además busca en toda la web.
![paso5.3](./inv5.3.png)
Obtenemos la id de el motor de busqueda despues de pinchar en **personalizar** así obtenemos la **ID** de nuestro *buscador*.
![paso5.4](./inv5.4.png)
![paso5.5](./inv5.5.png)

## Paso 6:
Volvemos a godot, en concreto a **ajustes**, en el apartado de **integraciones** seleccionamos la caja de Google Imágenes guardamos, e introducimos tanto la **API** como la **ID** en 2 campos que deberian aparecer debajo de Google Imágenes y guardamos de nuevo.
![paso6.1](./inv6.1.png)
![paso6.2](./inv6.2.png)

## Paso 7:
Vamos al módulo de **inventario** de nuevo en el apartado de **productos** y pinchamos en el producto al que le queramos darle una imagen, luego pincharemos en **acción**, **obtener imágenes de google imágenes** y **obtener imágenes**
![paso7.1](./inv7.1.png)
Con esto ya hemos obtenido la imagen autogenerada que deseabamos y podemos reproducir esto en todos nuestros productos.
![prods](./prods.png)