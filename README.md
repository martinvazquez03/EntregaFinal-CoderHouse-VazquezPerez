# Tercera_Pre_Entrega_CoderHouse_MartinVazquezPerez

#LINK AL VIDEO MOSTRANDO EL FUNCIONAMIENTO DE LA PAGINA: https://youtu.be/drq6rEQHTTg

# Este proyecto me gustaria usarlo como base para el proyecto final y ademas usarlo con mis amigos una vez termine el curso

# Se trata de un blog con informacion sobre nuestro grupo de amigos, llamado Sie7e-600. En el mismo se incluyen videos, comentarios, creacion de usuarios, una seccion para conocer a la comunidad y ademas un link hacia la unica red social que manejamos (por el momento).

# En cuanto a la funcionalidad de cada archivo views.py:

# Dentro de la app MainM (actua a modo de nucleo/inicio de la pagina):
    * view_mainmenu: renderiza el template MainM/index.html (que hereda de MainM/base.html, al igual que todos los archivos index.html que haya en la carpeta templates de cada una de las apps), mostrandose asi en pantalla la seccion de inicio.

    * view_about: renderiza el template MainM/about.html, mostrando en pantalla la seccion de redes sociales, la cual contiene un link a nuestro instagram.

    *los unicos cambios que sufrieron estas dos funciones fue hacer una verificacion a traves de un if para saber si el usuario estaba logueado (request.user.is_authenticated) con el fin de mostrar el avatar

# Dentro de la app Cliente (que en realidad es la seccion de usuarios):
    * view_Cliente: renderiza el template Cliente/index.html (que hereda de MainM/index.html), a su vez, a traves de la listview muestra una lista con todos los usuarios creados.

    * Formulario_usuarios: se encarga de renderizar el template Cliente/crear_usuario.html en caso de recibir un request GET,mostrandonos asi un formulario para crear un usuario, si recibe un request de tipo POST, valida la informacion, la guarda en la base de datos y nos redirige a la pagina principal de la app cliente (en la pagina web aparece como registro/inicio de sesion).// modificacion: ahora utiliza el modelo User importado desde django para que la autenticacion fuera mas sencilla, dentro de Cliente/forms.py se encuentra el nuevo formulario

    * view_formulario_buscado: esta funcion actua practicamente igual a la anterior, renderiza el template Cliente/buscar_usuario.html que nos muestra un formulario con un solo campo, se pone el nombre de usuario y nos devuelve el nombre, apellido, nombre de usuario e email de la persona con dicho usuario. Esto se muestra luego de que la funcion al recibir el request de tipo POST nos renderice el template encargado de mostrar lo anteriormente dicho (Cliente/buscar_usuario.html).

    *funciones login y logout: creo que esta bastante claro el uso de las mismas, 

# Dentro de la app Producto (que en realidad es la seccion de videos en este caso):
    *view_Producto: renderiza el template Producto/index.html (extension de MainM/base.html), mostrando asi videos traidos del modelo Videos.
    
    *view_comentar: funciona igual que la funcion Formulario_usuarios, solo que esta en vez de mostrar un formulario con los campos del modelo Usuario, muestra un formulario con dos campos basado en el modelo Comentarios.// modificacion: ahora sabe que usuario quiere comentar sin que haga falta escribirlo manualmente ya que obtiene la informacion a traves del login hecho, por otro lado obtiene otro campo que es el de "post" haciendo referencia al modelo Video a traves de una foreign key asociando asi ambos modelos 


