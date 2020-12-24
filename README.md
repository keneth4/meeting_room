# meeting_room
Plataforma de administración sencilla para el apartado de salas de juntas

# Instalación y despliegue
	(Backend | Entorno virtual con Django)
	- Descompimir el archivo 'env.rar' 
	- Navegar hasta el directorio 'env\Scripts\activate' con la consola para correr el script
	- Una vez que el entorno virtual esté activo, ser verá '(env)' al inicio de la línea de comando
	- Correr el servidor con 'python manage.py runserver'
	
	(Frontend)
	- Ubicarse en el directorio del proyecto '/vue_meeting_room/'
	- Correr el comando 'npm i'
	- Una vez instalado el proyecto con sus dependencias y paquetes correr el servidor con 'npm run serve'

# Back-end
	Entorno Virtual con las siguientes dependencias instaladas:
	* django 3.1.4
	* djangorestframework 3.12.2
	* django-cors-headers 
	Informacion de autenticacion para requests a django:
	* Username: lion
	* Password: 123

# Front-end
	* Vue.js
	* Axios
	* Vuetify
