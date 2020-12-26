<template>
    <v-container fluid>
        <v-row>
        <v-col cols="3">
            <v-card
            class="my-2"
            >
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
            <v-card
                class="my-2"
            >
                <v-card-text>
                <p class="display-1 text--primary">
                    Salas de juntas
                </p>
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
                    <v-card-text v-if="sala.horarios !== []">
                        <v-container>
                            <v-row v-for="(horario,index) in sala.horarios" v-bind:key="index">
                                <v-col cols="2">
                                    <v-chip
                                    class="ma-2"
                                    color="success"
                                    outlined
                                    >
                                        {{horario.nombre}}
                                    </v-chip>
                                </v-col>
                                <v-col cols="2">
                                    Ingreso: {{horario.horaInicio}}
                                    <br>
                                    Salida: {{horario.horaFin}}
                                </v-col>
                            </v-row>
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
                        @click="setStatus(sala.id,'libre')"
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
                    @click="reservarSala(salaSelected.id,nombreReserva,horaInicio,horaFin,salaSelected.horarios); $refs.picker1.selectingHour = true; $refs.picker2.selectingHour = true;"
                >
                    Reservar
                </v-btn>
                </v-card-title>
                <v-form class="mx-2">
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
      salas: [],
      salasJson: [],
      salaSelected: {},
      nombre: '',
      horarios: [],
      status: 'libre',
      timer: '',
      dialog: false,
      snackbar: false,
      mensaje: '',
      nombreReserva: '',
      horaInicio: '',
      horaFin: '',
  }),
  mounted() {
      
  },
  created() {
      this.gettime()
      this.getSalas()
  },
  methods: {
      gettime() {
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
        setTimeout(() => this.gettime(), 100);
      },
      getSalas(){
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
          })
      },
      addSala(){
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
      setStatus(sala_id,sala_status){
          const sala = this.salas.filter(sala => sala.id === sala_id)[0]
          const nombre = sala.nombre
          const horarios = sala.horarios
          axios({
              method: 'put',
              url: 'http://127.0.0.1:8000/salas/' + sala_id + '/',
              headers: {
                  'Content-Type': 'application/json',
              },
              data: {
                  nombre: nombre,
                  status: sala_status,
              },
              auth: {
                  username: 'lion',
                  password: '123'
              }
          }).then(()=>{
              sala.status = sala_status;
              this.getSalas();
          })
      },
      reservarSala(sala_id,nombre_reserva,hora_inicio,hora_fin,horarios_previos){
          if (this.nombreReserva != '' && this.horaInicio != '' && this.horaFin != ''){
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
              var diferencia = ((date2-date1)/1000)/60;//Diferencia de Horario en minutos
              if (diferencia <= 120 && diferencia > 0){
                const sala = this.salas.filter(sala => sala.id === sala_id)[0];
                const nombre = sala.nombre;
                var horarios = [];
                var horariosT = '';
                const horarioNuevo = '{"nombre": "' + nombre_reserva + '", "horaInicio": "' +  hora_inicio + '", "horaFin": "' +  hora_fin + '"}';
                horarios = horarios_previos;
                horarios.push(JSON.parse(horarioNuevo));
                axios({
                    method: 'put',
                    url: 'http://127.0.0.1:8000/salas/' + sala_id + '/',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    data: {
                        nombre: nombre,
                        horarios: JSON.stringify(horarios),
                    },
                    auth: {
                        username: 'lion',
                        password: '123'
                    }
                }).then(()=>{
                    this.dialog = false;
                    this.getSalas();
                })
              }
              else if (diferencia <= 0){
                this.mensaje = 'La hora de entrada debe ser menor a la de salida';
                this.snackbar = true;
              }
              else{
                this.mensaje = 'Sólo se puede escoger un intervalo de 2 horas o menor';
                this.snackbar = true;
              }
          }
          else{
              this.mensaje = 'Tienes que llenar todos los campos de la reserva';
              this.snackbar = true;
          }
      },
      deleteSala(sala_id){
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
              })
          }
      },
      resetReserva(){
          this.nombreReserva = '';
          this.horaInicio = '';
          this.horaFin = '';
      },
      interpretarHorarios(){
          this.salasJson = [];
          this.salas.forEach(sala => {
              this.salasJson.push({
                  'id': sala.id,
                  'nombre': sala.nombre,
                  'status': sala.status,
                  'horarios': JSON.parse(sala.horarios)
              })
          });
      }
  },
}
</script>
