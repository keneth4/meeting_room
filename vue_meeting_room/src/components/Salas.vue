<template>
    <v-container fluid>
        <v-row>
        <v-col cols="3">
            <v-card
            class="my-2"
            >
                <v-card-text>
                    <p class="display-1 text--primary">
                        Agregar Sala
                    </p>
                    <v-form
                    v-on:submit.prevent="addSala"
                    >
                        <v-text-field
                        v-model="nombre"
                        label="Descripción de la sala"
                        required
                        ></v-text-field>

                        <!--<v-select
                        v-model="status"
                        :items="options"
                        :rules="[v => !!v || 'Item is required']"
                        label="Status"
                        required
                        ></v-select>-->
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
                        {{timer}}
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
                <v-card v-for="sala in salas" v-bind:key="sala.id" class="mx-auto ma-2">
                    <v-card-title>{{sala.nombre}} - {{sala.status}} - {{sala.horarios}}</v-card-title>
                    <v-card-actions>
                        <!--<v-btn
                        text
                        color="teal accent-4"
                        @click="setStatus(sala.id,'ocupada')"
                        >
                        Ocupar
                        </v-btn>-->
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
                Selecciona el horario en {{salaSelected.nombre}}
                <v-spacer></v-spacer>
                <v-btn
                    color="primary"
                    text
                    @click="snackbar = true"
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
                                ></v-time-picker>
                            </v-col>
                            <v-col cols="6" class="d-flex justify-center">
                                <v-time-picker
                                v-model="horaFin"
                                format="ampm"
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
                {{ nombreReserva }} - {{ horaInicio }} - {{ horaFin }}
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
          }).then(response=>this.salas=response.data)
      },
      addSala(){
          if (this.nombre){
              axios({
                  method: 'post',
                  url: 'http://127.0.0.1:8000/salas/',
                  data: {
                      nombre: this.nombre,
                      horarios: this.horarios,
                      status: this.status
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
              }).catch((error)=>{
                  console.log(error)
              })
          }
      },
      setStatus(sala_id,sala_status){
          const sala = this.salas.filter(sala => sala.id === sala_id)[0]
          const nombre = sala.nombre
          axios({
              method: 'put',
              url: 'http://127.0.0.1:8000/salas/' + sala_id + '/',
              headers: {
                  'Content-Type': 'application/json',
              },
              data: {
                  nombre: nombre,
                  status: sala_status
              },
              auth: {
                  username: 'lion',
                  password: '123'
              }
          }).then(()=>{
              sala.status = sala_status
          })
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
      }
  },
}
</script>
