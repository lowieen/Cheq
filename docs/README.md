Documentación del Proyecto "Cheq"

Resumen
"Cheq" es un proyecto de comercio electrónico desarrollado utilizando Vue.js y Python. El propósito de este proyecto es proporcionar una plataforma en línea para la venta de ropa de vestir y urbana, combinar dos estilos diferentes en un sitio. Además de un sistema para la auto-gestión de los productos y sus respectivos stocks. Con Gestión de cuentas de usuarios, de inicios de sesión y registro en la Base de Datos utilizando el método de seguridad Hash.

Tecnologías Utilizadas:
● Vue.js
● Python
● Flask (framework de Python)
● MySQL (base de datos)
● HTML/CSS
● JavaScript
● SMTP (para envío de correos electrónicos)

Instalación:
Para instalar y ejecutar el proyecto en tu entorno local, sigue estos pasos:
1. Clona el repositorio desde GitHub: git clone https://github.com/lowieen/cheq
2. Accede al directorio del proyecto: cd cheq
3. Crea un entorno virtual de Python: python -m venv venv
4. Activa el entorno virtual:
    ● En Windows: venv\Scripts\activate
    ● En macOS y Linux: source venv/bin/activate
5. Instala las dependencias de Python: pip install -r requirements.txt
6. Inicia la aplicación: python app.py

Configuración:
● Base de Datos: Configura la conexión a la base de datos en el archivo app.py.
● Envío de Correos Electrónicos: Configura las credenciales de tu cuenta de correo electrónico Gmail en el archivo send_email.py.

Funcionalidades:
Registro de Usuarios
● Los usuarios pueden registrarse en la plataforma utilizando su correo electrónico y contraseña.

Inicio de Sesión
● Los usuarios registrados pueden iniciar sesión en sus cuentas y tendrán un apartado en la sección Perfil donde podrán ingresar sus datos que se utilizaran para obtener compras realizadas y/o un auto-completado en el formulario del checkout.

Catálogo de Productos
● Se pueden encontrar dos tipos de catálogos al hacer click en las dos secciones que se muestran en 'Home', estas dos secciones están representadas por imagenes de dos estilos diferentes, cada una despliega una ventana con sus respectivos productos.
● Los usuarios pueden navegar por diferentes prendas donde pueden encontrar diferentes filtros si desean aplicar.
● Pueden agregar productos al carrito de compras así como eliminarlos y realizar compras.

Carrito de Compras
● Los usuarios pueden ver y administrar los productos en su carrito de compras.
● Pueden proceder a la compra, donde se les pide datos del usuario si NO está registrado, y por último un resumen para verificar si esta todo en condiciones. Finalizando con la compra actualizando el stock y un envío de correo a nuestro email con los datos de la compra.

Envío de Correos Electrónicos
● Se envían correos electrónicos de las compras al equipo de administración.

Uso
1. Regístrate o inicia sesión en la plataforma, no es si o si necesario.
2. Explora el catálogo de productos, haz click en 'Ver' 
3. Elige el talle y la cantidad de unidades, y agregalos al carrito de compras.
4. Procede al checkout desde la ventana de Carrito de compras y sigue las instrucciones para completar el pago.
5. En la sección Perfil (si te has registrado) estará para completar tus datos y las compras que realizaste con un Codigo de Compra unico de cada Pedido.
6. El equipo de administración recibirá notificaciones de las compras realizadas.

Cuenta ADMIN
● Existe una cuenta admin para poder ingresar a /admin que requiere el permiso de la autenticación de la misma.
1. Inicia Sesión con el email 'admin@gmail.com' y password 'admin'
2. Ve a Perfil y aparecerá 'Administrar' (solamente si estas dentro de la cuenta admin) en la lista de Datos de tu Cuenta.
3. Podrás Agregar, Modificar y Eliminar productos como desees.

Contribuciones:
¡Agradecemos las contribuciones de la comunidad! Si deseas contribuir al proyecto, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama para tu contribución: git checkout -b mi-contribucion
3. Realiza tus cambios y verifica que todo funcione correctamente.
4. Envía un pull request con tus cambios.

Contacto
Para cualquier pregunta o comentario, contactame alexismunioz4@gmail.com

Licencia
Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más información.

Agradecimientos
Agradecemos a todos los desarrolladores que contribuyeron a este proyecto y a la comunidad de código abierto por su apoyo.