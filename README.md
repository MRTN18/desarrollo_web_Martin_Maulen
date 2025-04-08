# Tarea 1

En esta tarea distribuí los archivos en vuatro carpetas distintas, en una esta todo lo relacionado a CSS, en donde están todos los archivos que le dan el estilo a la página, a unos que son utilizados más globalmente en los HTML como style.css y otros que son específicos para un HTML, estos que son más específicos llevan el mismo nombre que los archivos HTML donde se usan.

Para los HTML, se creo uno para cada página que se pidio en la tarea, cada uno tiene el nombre de la página a la que hace referencia, los HTML que tiene el nombre actividad{i}.html son las páginas en donde los usuarios son dirigidos cuando hacen click sobre una de las actividades en la lista de actividades.

En la carpeta JS están todos los códigos de JavaScript utilizados en la página, estos tienen los mismos nombres que los HTML donde se están utilizando, el más importante es el agregar-actividad.js, aquí se encuentra la validación del formulario que esta en el HTML agregar-actividad.html. Estas validaciones se hacen idividualmente para cada campo con una función dedicada a cada uno utilizando onchange en la etiqueta input del HTML, luego cuando se presiona el boton agregar actividad, se ejecuta la función validate, la cual llama a todas las funciones de validación de cada campo. Esta función despliega un modal para que el usuario termine de agregar la actividad si es que se pasaron todas las validaciones, si no se muestra un mensaje de error en color rojo debajo de todos los campos que tienen problemas.

Por último, en la carpeta image, se encuentran todas las fotos utilizadas en la página.