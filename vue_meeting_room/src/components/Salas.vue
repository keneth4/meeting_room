<template>
    <v-container>
        <v-row>
        <v-col cols="3">
            <v-card
            class="mx-auto"
            min-width="400"
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
                        label="Nombre"
                        required
                        ></v-text-field>

                        <v-select
                        v-model="status"
                        :items="options"
                        :rules="[v => !!v || 'Item is required']"
                        label="Status"
                        required
                        ></v-select>
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
        </v-col>
        <v-col cols="9">
            <v-card
                class="mx-auto"
                min-width="500"
                max-width="600"
            >
                <v-card-text>
                <p class="display-1 text--primary">
                    Salas
                </p>
                <v-card v-for="sala in salas" v-bind:key="sala.id" class="my-2">
                    <!--<div v-if="sala.status !== 'ocupada'">-->
                        <v-card-title>{{sala.nombre}} - {{sala.status}}</v-card-title>
                        <v-card-actions>
                            <v-btn
                            text
                            color="teal accent-4"
                            @click="setStatus(sala.id,'ocupada')"
                            >
                            Ocupar
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
                    <!--</div>-->
                </v-card>
                </v-card-text>
            </v-card>
        </v-col>
        </v-row>
    </v-container>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'


export default {
  name: 'Salas',
  data: () => ({
      salas: [],
      nombre: '',
      status: 'libre',
      options: [
        'libre',
        'ocupada',
      ],
  }),
  mounted() {
      this.getSalas()
  },
  methods: {
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
                      'status': this.status
                  }
                  this.salas.push(newSala)
                  this.nombre = ''
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
      }
  },
}
</script>
