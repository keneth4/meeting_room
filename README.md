# meeting_room
Plataforma de administración sencilla para el apartado de salas de juntas.

## Uso
Tan fácil como añadir una nueva sala y reservarla en el horario que gustes, todo lo demás va de forma automática.

- Añade una nueva sala

![Añadir nueva sala](https://i.postimg.cc/76cG088r/agregar-sala.png)

- Reserva la sala deseada

![Añadir nuevo horario](https://i.postimg.cc/DZm4SfNc/agregar-horario.png)

- Selecciona el horario que quieras reservar, dale un nombre a tu reserva y guardala

![Guardar la reserva](https://i.postimg.cc/d3y79Hwk/guardar-reserva.png)

- Borra tu reserva, la sala o añade otra reserva más

![Modificar la reserva](https://i.postimg.cc/Sjbn16xZ/modificar-reserva.png)

Al pasar el tiempo, las salas se irán ocupando y desocupando de manera automática, o puedes liberar la sala de forma manual si así lo deseas.

> Nota: Si el horario que acabas de ingresar no aparece, sólo ten paciencia, a veces puede tardar un poco en aparecer en pantalla, todo dependerá de la velocidad del servidor.

## Reglas
- Los horarios deberán abarcar un período de máximo 2 horas. 
- Los horarios deberán de estar dentro del tiempo restante hasta antes de las 12 de la noche, hora en que se reinicia el conteo.
- No se puede elegir un horario con un tiempo anterior al actual.
- No se puede elegir un horario que interfiera completa o parcialmente con otro que ya se encuentre reservado.
- La hora de ingreso no puede ser más tarde que la de salida.

## Instalación y despliegue

### (Backend | Entorno virtual con Django) para Windows

1. Descompimir el archivo 'env.rar' 
2. Navegar hasta el directorio 'env\Scripts\activate' con la consola para correr el script
3. Una vez que el entorno virtual esté activo, ser verá '(env)' al inicio de la línea de comando
4. Ubicarse en el directio del proyecto '/meeting_room/' en donde se encuentra el archivo 'manage.py'
5. Correr el servidor con 'python manage.py runserver'
	
### (Frontend)

1. Ubicarse en el directorio del proyecto '/vue_meeting_room/' con la consola
2. Correr el comando 'npm i'
3. Una vez instalado el proyecto con sus dependencias y paquetes correr el servidor con 'npm run serve'
4. En el navegador entrar a la dirección proporcionada, comúnmente es 'localhost:8080'
	
## About

### Back-end
Entorno Virtual con las siguientes dependencias instaladas:
 - django 3.1.4
 - djangorestframework 3.12.2
 - django-cors-headers 3.6.0

Informacion de autenticacion para requests a la API en Django:
* Username: lion
* Password: 123

### Front-end
* Vue.js 2.6.11
* Axios 0.21.1
* Vuetify 2.2.11

## Posibles fallos y soluciones
Si algún horario no apareció, se actualizó o se borró de manera correcta, sólo borra el horario/sala correspondiente e ingresa los datos de nuevo de ser necesario.
