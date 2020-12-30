<template>
    <v-container fluid>
        <v-row>
        <v-col cols="3">
            <v-card
            class="my-2"
            >
                                                        <!-- Tarjeta para añadir nuevas salas -->
                <v-card-text>
                    <p class="display-1 text--primary">
                        Agregar sala
                    </p>
                    <v-form
                    v-on:submit.prevent="addSala"
                    >
                        <v-text-field
                        v-model="nombre"
                        label="Descripción de la sala"
                        required
                        ></v-text-field>
                        <v-btn
                            text
                            color="teal accent-4"
                            type="submit"
                        >
                            Agregar
                        </v-btn>
                    </v-form>
                </v-card-text>
            </v-card>
                                                        <!-- Tarjeta con reloj grande -->
            <v-card class="my-2 d-flex justify-center">
                <v-chip
                class="ma-2"
                x-large>
                    <p class="ma-2 display-1 text--primary">
                        {{ timer }}
                    </p>
                </v-chip>
            </v-card>
        </v-col>
        <v-col cols="9">
                                                        <!-- Sección de despliegue para la lista de salas -->
            <v-card
                class="my-2"
            >
                <v-card-text>
                <p class="display-1 text--primary">
                    Salas de juntas
                </p>
                                                        <!-- Tarjeta con todo el contenido de la sala -->
                <v-card v-for="sala in salasJson" v-bind:key="sala.id" class="mx-auto ma-2">
                    <v-card-title>
                        {{ sala.nombre }}
                        <v-chip
                        v-if="sala.status === 'libre'"
                        color="green"
                        class="ma-2">
                            {{ sala.status }}
                        </v-chip>
                        <v-chip
                        v-else
                        color="red"
                        class="ma-2">
                            {{ sala.status }}
                        </v-chip>
                    </v-card-title> 
                    <v-card-text >
                        <v-container v-if="hayHorarios(sala.horarios)">
                            <v-row v-for="(horario,index) in sala.horarios" v-bind:key="index">
                                <v-col class="d-flex justify-end">
                                    <v-chip
                                    class="ma-2"
                                    color="success"
                                    outlined
                                    close
                                    @click:close="borrarHorario(sala.id,index);"
                                    >
                                        {{ horario.nombre }}
                                    </v-chip>
                                </v-col>
                                <v-col>
                                    Ingreso: {{ horario.horaInicio }}
                                    <br>
                                    Salida: {{ horario.horaFin }}
                                </v-col>
                            </v-row>
                        </v-container>
                        <v-container v-else class="d-flex justify-center">
                            <p>La sala aún no cuenta con horarios reservados.</p>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn
                        text
                        color="teal accent-4"
                        @click="resetReserva(); salaSelected=sala; dialog = true;"
                        >
                        Reservar
                        </v-btn>
                        <v-btn
                        text
                        color="teal accent-4"
                        v-if="sala.status === 'ocupada'"
                        @click="liberarSala(sala.id)"
                        >
                        Desocupar
                        </v-btn>
                        <v-spacer></v-spacer>
                        <v-btn
                        text
                        color="teal accent-4"
                        @click="deleteSala(sala.id)"
                        >
                        Borrar
                        </v-btn>
                    </v-card-actions>  
                </v-card>
                </v-card-text>
            </v-card>
        </v-col>
        </v-row>
        <div class="text-center">
                                                        <!-- Dialog para mostrar el menú de horario nuevo -->
            <v-dialog
            v-model="dialog"
            width="700"
            >
            <v-card>
                <v-card-title class="headline grey lighten-2">
                Selecciona el horario en {{ salaSelected.nombre }}
                <v-spacer></v-spacer>
                <v-btn
                    color="primary"
                    text
                    @click="reservarSala(salaSelected.id); $refs.picker1.selectingHour = true; $refs.picker2.selectingHour = true;"
                >
                    Reservar
                </v-btn>
                </v-card-title>
                <v-form class="mx-2" v-on:submit.prevent="">
                    <v-text-field
                    v-model="nombreReserva"
                    label="Nombre para reservación"
                    required
                    clearable
                    ></v-text-field>
                </v-form>
                <v-card-text class="d-flex justify-center">
                    <v-container fluid>
                        <v-row>
                            <v-col cols="6" class="d-flex justify-center">
                                <h4>Horario de Entrada</h4>
                            </v-col>
                            <v-col cols="6" class="d-flex justify-center">
                                <h4>Horario de Salida</h4>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="6" class="d-flex justify-center">
                                <v-time-picker
                                v-model="horaInicio"
                                format="ampm"
                                ref="picker1"
                                ></v-time-picker>
                            </v-col>
                            <v-col cols="6" class="d-flex justify-center">
                                <v-time-picker
                                v-model="horaFin"
                                format="ampm"
                                ref="picker2"
                                ></v-time-picker>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card-text>
                <v-card-actions>
                
                </v-card-actions>
                                                        <!-- Snackbar para mostrar notificaciones de errores en el horario nuevo -->
                <v-snackbar
                v-model="snackbar"
                >
                {{ mensaje }}
                <template v-slot:action="{ attrs }">
                    <v-btn
                    color="teal accent-4"
                    text
                    v-bind="attrs"
                    @click="snackbar = false"
                    >
                    <v-icon>mdi-close</v-icon>
                    </v-btn>
                </template>
                </v-snackbar>
            </v-card>
            </v-dialog>
                                                        <!-- Snackbar para mostrar notificaciones de sala nueva -->
            <v-snackbar
            v-model="snackbar"
            >
            {{ mensaje }}
            <template v-slot:action="{ attrs }">
                <v-btn
                color="teal accent-4"
                text
                v-bind="attrs"
                @click="snackbar = false"
                >
                <v-icon>mdi-close</v-icon>
                </v-btn>
            </template>
            </v-snackbar>
        </div>
    </v-container>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'


export default {
  name: 'Salas',
  data: () => ({
      salas: [], // Array de todas las salas existentes, obtenido de la API
      salasJson: [], // Array de todas las salas existentes, con el Array de horarios parseado a objeto
      salaSelected: {}, // Sala seleccionada, con reservación en curso
      nombre: '', // Campo de llenado, nombre de la sala
      horarios: [], // Valor inicial para crear la sala 
      status: 'libre', // Valor inicial para crear la sala
      timer: '', // Timer/Reloj de pantalla 
      dialog: false, // Variable de activación para el Dialog
      snackbar: false, // Variable de activación para los Snackbar
      mensaje: '', // Contenido del texto en el Snackbar
      nombreReserva: '', // Campo de llenado, nombre de reserva para el nuevo horario
      horaInicio: '', // Campo de llenado, hora de inicio para el nuevo horario
      horaFin: '', // Campo de llenado, hora de salida para el nuevo horario
  }),
  mounted() {
    
  },
  created() { // Al cargar la página se cargaran las siguientes funciones
      this.gettime();
      this.getSalas();
      this.verificarStatusSalas();
  },
  methods: { // Todas las funciones existentes en la página
      gettime() { // Reloj
        var date= new Date();
        var hr = date.getHours();
        var m = date.getMinutes();
        var s = date.getSeconds();
        if(m < 10)
        {
            m = "0" + m
        }
        if(s < 10)
        {
            s = "0" + s
        }
        this.timer = hr + ":" + m + ":" + s;
        if(s == "00"){
            this.verificarStatusSalas(); // Cada minuto se verifica el status de las salas
        }
        setTimeout(() => this.gettime(), 1000);
      },
      getSalas(){ // Cargar las salas en la Tarjeta principal
          axios({
              method: 'get',
              url: 'http://127.0.0.1:8000/salas/',
              auth: {
                  username: 'lion',
                  password: '123'
              }
          }).then((response)=> {
              this.salas=response.data;
              this.interpretarHorarios();
          }).catch((error)=>{
              console.log(error)
          })
      },
      addSala(){ // Añadir nueva Sala a la base de datos
          if (this.nombre){
              axios({
                  method: 'post',
                  url: 'http://127.0.0.1:8000/salas/',
                  data: {
                      nombre: this.nombre,
                      horarios: JSON.stringify(this.horarios),
                  },
                  auth: {
                    username: 'lion',
                    password: '123'
                  }
              }).then((response)=>{
                  let newSala = {
                      'id': response.data.id,
                      'nombre': this.nombre,
                      'horarios': this.horarios,
                      'status': this.status
                  }
                  this.salas.push(newSala)
                  this.nombre = ''
                  this.horarios = []
                  this.status = 'libre'
                  this.getSalas();
              }).catch((error)=>{
                  console.log(error)
              })
          }
          else{
              this.mensaje = 'Proporciona un nombre para la sala';
              this.snackbar = true;
          }
      },
      reservarSala(sala_id){ // Reservar un horario nuevo en la sala indicada
          if (this.nombreReserva != '' && this.horaInicio != '' && this.horaFin != ''){//Que no haya campos vacios
              const nombre_reserva = this.nombreReserva;
              const hora_inicio = this.horaInicio;
              const hora_fin = this.horaFin;
              var ahora = new Date();
              var fechas = this.pasearHorario(hora_inicio,hora_fin);
              if (fechas[0] >= ahora && fechas[1] >= ahora){//Que solo se pueda escoger un horario a partir de la hora actual
                var diferencia = ((fechas[1]-fechas[0])/1000)/60;
                if (diferencia <= 120 && diferencia > 0){//Que el horario sea de maximo 2 horas
                    const sala = this.salas.filter(sala => sala.id === sala_id)[0];
                    var nombre = '';
                    var horarios_previos = [];
                    if (sala == undefined){
                        nombre = this.salaSelected.nombre;
                        horarios_previos = JSON.parse(this.salaSelected.horarios);
                    }
                    else {
                        nombre = sala.nombre;
                        horarios_previos = JSON.parse(sala.horarios);
                    }
                    var horarios = [];
                    const horarioNuevo = '{"nombre": "' + nombre_reserva + '", "horaInicio": "' +  hora_inicio + '", "horaFin": "' +  hora_fin + '"}';
                    horarios = JSON.parse(JSON.stringify(horarios_previos));
                    horarios.push(JSON.parse(horarioNuevo));
                    const nuevo_status = this.verificarSala(horarios);
                    if (this.estaLibre(horarios_previos,fechas[0],fechas[1])){//Que no haya otro horario existente en el mismo rango de tiempo
                        axios({
                            method: 'put',
                            url: 'http://127.0.0.1:8000/salas/' + sala_id + '/',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            data: {
                                nombre: nombre,
                                horarios: JSON.stringify(horarios),
                                status: nuevo_status,
                            },
                            auth: {
                                username: 'lion',
                                password: '123'
                            }
                        }).then(()=>{
                            this.dialog = false;
                            sala.status = nuevo_status;
                            this.getSalas();
                        }).catch((error)=>{
                            console.log(error)
                        })
                    }
                    else{
                        this.mensaje = 'La sala ya está parcial o completamente ocupada en ese horario';
                        this.snackbar = true;
                    }
                }
                else if (diferencia <= 0){//Que la hora de entrada y salida sean coherentes entre si
                    this.mensaje = 'La hora de entrada debe ser menor a la de salida';
                    this.snackbar = true;
                }
                else{
                    this.mensaje = 'Sólo se puede escoger un intervalo de 2 horas o menor';
                    this.snackbar = true;
                }
              }
              else {
                this.mensaje = 'Sólo se puede escoger un horario a partir de la hora actual';
                this.snackbar = true;
              }
          }
          else{
              this.mensaje = 'Tienes que llenar todos los campos de la reserva';
              this.snackbar = true;
          }
      },
      deleteSala(sala_id){ // Borrar la sala indicada
          if (sala_id){
              axios({
                  method: 'delete',
                  url: 'http://127.0.0.1:8000/salas/' + sala_id + '/',
                  headers: {
                    'Content-Type': 'application/json',
                  },
                  auth: {
                    username: 'lion',
                    password: '123'
                  }
              }).then(()=>{
                this.getSalas()
              }).catch((error)=>{
                  console.log(error)
              })
          }
      },
      resetReserva(){ // Reiniciar datos de reserva después de haber guardado una nueva
          this.nombreReserva = '';
          this.horaInicio = '';
          this.horaFin = '';
      },
      interpretarHorarios(){ // Interpretar el Array de horarios de tipo texto JSON a tipo Objeto
          this.salasJson = [];
          const salas = JSON.parse(JSON.stringify(this.salas));
          salas.forEach(sala => {
              this.salasJson.push({
                  'id': sala.id,
                  'nombre': sala.nombre,
                  'status': sala.status,
                  'horarios': JSON.parse(sala.horarios)
              })
          });
      },
      pasearHorario(hora_inicio,hora_fin){ // Parsear dos textos en formato HH:mm a dos tipo Date seteadas con dichos horarios
          const horaInicioHoras = parseInt(hora_inicio.substring(0,2));
          const horaInicioMinutos = parseInt(hora_inicio.substring(3,5));
          const horaFinHoras = parseInt(hora_fin.substring(0,2));
          const horaFinMinutos = parseInt(hora_fin.substring(3,5));
          var date1= new Date();
          date1.setHours(horaInicioHoras);
          date1.setMinutes(horaInicioMinutos);
          var date2= new Date();
          date2.setHours(horaFinHoras);
          date2.setMinutes(horaFinMinutos);
          return [date1,date2];
      },
      estaLibre(horarios,fecha_inicio,fecha_fin){ // Indicar si un horario nuevo está disponible en un Array de horarios de una sala
          horarios = JSON.parse(JSON.stringify(horarios));
          var bandera = true;
          horarios.forEach(horario => {
              var fechas = this.pasearHorario(horario.horaInicio,horario.horaFin);
              if ((fecha_inicio <= fechas[0] && fecha_fin >= fechas[1]) || (fecha_inicio >= fechas[0] && fecha_fin <= fechas[1]) || (fecha_inicio <= fechas[0] && fecha_fin <= fechas[1] && fecha_fin > fechas[0]) || (fechas[0] <= fecha_inicio && fechas[1] <= fecha_fin && fechas[1] > fecha_inicio)){
                  bandera = false;
              }
          });
          return bandera;
      },
      verificarStatusSalas(){ // Verificar el status de todas las salas según sus respectivos horarios
        const salas = JSON.parse(JSON.stringify(this.salas));
        salas.forEach(sala => {
            const nombre = sala.nombre;
            const horarios = JSON.parse(sala.horarios);
            const nuevo_status = this.verificarSala(horarios);
            var nuevosHorarios = JSON.parse(sala.horarios);
            horarios.forEach(horario => {
                var ahora = new Date();
                var fechas = this.pasearHorario(horario.horaInicio,horario.horaFin);
                if (ahora >= fechas[1]){
                    nuevosHorarios = horarios.filter(x => x != horario);
                }
            });
            axios({
                method: 'put',
                url: 'http://127.0.0.1:8000/salas/' + sala.id + '/',
                headers: {
                    'Content-Type': 'application/json',
                },
                data: {
                    nombre: nombre,
                    status: nuevo_status,
                    horarios: JSON.stringify(nuevosHorarios),
                },
                auth: {
                    username: 'lion',
                    password: '123'
                }
            }).then(()=>{
                sala.status = nuevo_status;
                this.getSalas();
            }).catch((error)=>{
                console.log(error)
            })
        });
      },
      verificarSala(hrs){ // Verificar el horario de una sala y devolver si está ocupada o libre según la hora actual
        const horarios = JSON.parse(JSON.stringify(hrs));
        var status = 'libre';
        horarios.forEach(horario => {
            var ahora = new Date();
            var fechas = this.pasearHorario(horario.horaInicio,horario.horaFin);
            if (ahora >= fechas[0] && ahora < fechas[1]){
                status = 'ocupada';
            }
        });
        return status;
      },
      liberarSala(sala_id){ // Liberar una sala que esté ocupada y borrar su horario en curso
          const sala = this.salas.filter(sala => sala.id === sala_id)[0];
          const nombre = sala.nombre;
          const horarios = JSON.parse(sala.horarios);
          var nuevosHorarios = {};
          var bandera = false;
          horarios.forEach(horario => {
            var ahora = new Date();
            var fechas = this.pasearHorario(horario.horaInicio,horario.horaFin);
            if (ahora >= fechas[0] && ahora < fechas[1]){
                nuevosHorarios = horarios.filter(x => x != horario);
                bandera = true;
            }
          });
        if (bandera){
            axios({
                method: 'put',
                url: 'http://127.0.0.1:8000/salas/' + sala_id + '/',
                headers: {
                    'Content-Type': 'application/json',
                },
                data: {
                    nombre: nombre,
                    status: 'libre',
                    horarios: JSON.stringify(nuevosHorarios),
                },
                auth: {
                    username: 'lion',
                    password: '123'
                }
            }).then(()=>{
                sala.status = 'libre';
                this.getSalas();
            }).catch((error)=>{
                console.log(error)
            })
        }
      },
      hayHorarios(horarios){ // Devolver si hay algo en el Array de horarios indicado
          if (horarios.length == 0){ return false }
          else { return true }
      },
      borrarHorario(sala_id,horario_id){ // Borrar el horario indicado y verificar si también es el horario en curso para liberar la sala o no
          const sala = this.salas.filter(sala => sala.id === sala_id)[0];
          const nombre = sala.nombre;
          const horarios = JSON.parse(sala.horarios);
          var bandera = false;
          var status = sala.status;
          var ahora = new Date();
          var fechas = this.pasearHorario(horarios[horario_id].horaInicio,horarios[horario_id].horaFin);
          if (ahora >= fechas[0] && ahora < fechas[1]){
            status = 'libre';
          }
          horarios.splice(horario_id, 1);
          axios({
            method: 'put',
            url: 'http://127.0.0.1:8000/salas/' + sala_id + '/',
            headers: {
                'Content-Type': 'application/json',
            },
            data: {
                nombre: nombre,
                status: status,
                horarios: JSON.stringify(horarios),
            },
            auth: {
                username: 'lion',
                password: '123'
            }
        }).then(()=>{
            this.getSalas();
        }).catch((error)=>{
            console.log(error)
        })
      }
  },
}
</script>
