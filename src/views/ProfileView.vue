<template>
    <main class="main-perfil">
        <div class="welcome">
          <div>
            <h1>Bienvenido</h1>
          </div>
          <div v-for="elem in user" :key="elem.email">
            <h1 v-if="elem.nombre!=='-'">{{elem.nombre}}!</h1>
          </div>  
        </div>
        <div class="wrapper-list">
          <div class="list">
              <h3>Datos de tu Cuenta</h3>            
                <ul>
                  <li
                    class="elem-list"
                    @click="showDatos = 'datos'"
                    :class="{ 'on': showDatos == 'datos' }">
                    Datos Personales
                  </li>
                
                  <li
                    class="elem-list"
                    @click="showDatos = 'direc'"
                    :class="{ 'on': showDatos == 'direc' }">
                    Dirección
                  </li>

                  <li
                    class="elem-list"
                    @click="showDatos = 'pedidos'"
                    :class="{ 'on': showDatos == 'pedidos' }">
                    Pedidos
                  </li>

                  <li v-if="isAdmin">
                    <router-link :to="{ name:'admin' }">Administrar</router-link>
                  </li>

                  <li class="elem-list" @click="emitLogoutEvent">
                    Cerrar sesión
                  </li>
                </ul>
          </div>
          
            <div class="list-data" v-if="showDatos == 'datos'">
              <div class="data-perfil">
                <div class="datos-personales" :class="{edit:!edit}" v-for="elem in dataUser" :key="elem.email">
                  <div>
                    <h4>Nombre</h4>
                    <span>{{elem.nombre}}</span>
                  </div>
                  <div>
                    <h4>Apellido</h4>
                    <span>{{elem.apellido}}</span>
                  </div>
                  <div>
                    <h4>DNI</h4>
                    <span>{{elem.dni}}</span>
                  </div>
                  <div>
                    <h4>Celular</h4>
                    <span>{{elem.cel}}</span>
                  </div>
                  <div class="edit">
                    <button type="button" class="edit-btn" @click="editarDatos">Editar</button>
                  </div>
                </div>

                <div id="edicion" :class="{update:!edit}">
                  <span class="close-datos" @click="closed"><ion-icon :src="close"></ion-icon></span>
                  <div>
                    <label for="nombreInput">Nombre:</label>
                    <input type="text" v-model="nuevoNombre">
                  </div>
                  <div>
                    <label for="apellidoInput">Apellido:</label>
                    <input type="text" v-model="nuevoApellido">
                  </div>
                  <div>
                    <label for="dniInput">DNI:</label>
                    <input type="number" v-model="nuevoDNI">
                  </div>
                  <div>
                    <label for="celularInput">Celular:</label>
                    <input type="number" v-model="nuevoCel">
                  </div>
                  <div>
                    <button class="actualizar" @click="updateDatos">Actualizar</button>
                  </div>
                  <div>
                    <div class="verification">{{ verificationDate }}</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="list-direc" v-else-if="showDatos == 'direc'">
              <div class="data-perfil">
                <div class="data-direc" :class="{edit:!edit}" v-for="elem in dataDirec" :key="elem.email">
                  <div>
                      <h4>Provincia</h4>
                      <span>{{elem.provincia}}</span>
                  </div>
                  <div>
                      <h4>Localidad</h4>
                      <span>{{elem.localidad}}</span>
                  </div>
                  <div>
                      <h4>Calle</h4>
                      <span>{{elem.calle}}</span>
                  </div>
                  <div>
                      <h4>Codigo Postal</h4>
                      <span>{{elem.codigo_postal}}</span>
                  </div>
                  <div>
                      <h4>Piso</h4>
                      <span>{{elem.piso}}</span>
                  </div>
                  <div>
                      <h4>Dpto</h4>
                      <span>{{elem.dpto}}</span>
                  </div>
                  <div>
                      <h4>Datos Extra</h4>
                      <span>{{elem.datos_extra}}</span>
                  </div>
                  <div class="edit">
                      <button type="button" class="edit-btn" @click="editDirec()">Editar</button>
                  </div>   
                </div>

                <div :class="{update:!edit}" id="edicion-direc">
                  <span class="close-datos" @click="closed"><ion-icon :src="close"></ion-icon></span>
                  <div>
                      <label for="provinciaInput">Provincia:</label>
                      <input type="text" v-model="nuevoProv">
                  </div>
                  <div>
                      <label for="localidadInput">Localidad:</label>
                      <input type="text" v-model="nuevoLocalidad">
                  </div>
                  <div>
                      <label for="calleInput">Calle:</label>
                      <input type="text" v-model="nuevoCalle">
                  </div>
                  <div>
                      <label for="codPInput">Codigo Postal:</label>
                      <input type="number" v-model="nuevoCP">
                  </div>
                  <div>
                      <label for="pisoInput">Piso:</label>
                      <input type="text" v-model="nuevoPiso">
                  </div>
                  <div>
                      <label for="dptoInput">Dpto:</label>
                      <input type="text" v-model="nuevoDpto">
                  </div>
                  <div>
                      <label for="datosEInput">Datos Extra:</label>
                      <textarea cols="20" rows="3" v-model="nuevoDatosE"></textarea>
                  </div>
                  <div>
                      <button class="actualizar" @click="updateDirec">Actualizar</button>
                  </div>
                  <div class="container-message">
                    <div class="verification">{{ verificationDirec }}</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="list-pedido" v-else>
              <div class="data-perfil">
                <div class="data-pedidos" v-for="elem in userPedido" :key="elem.numero">
                  <div>
                    <h3>Articulos</h3>
                    <span>- {{ elem.productos }}</span>
                  </div>
                  <div>
                    <h3>Importe</h3>
                    <span>${{ elem.importe }}</span>
                  </div>
                  <div>
                    <h3>Codigo de la compra</h3>
                    <span>{{ elem.numero }}</span>
                  </div>
                </div>
              </div>
            </div>
          
        </div>

      <div class="help">
        <h3>¿Necesitas Ayuda?</h3>
        <div class="help-data">
          <router-link :to="{ name: 'buzos' }" class="index">Productos</router-link>
          <router-link :to="{ name: 'help' }" class="index">Pedidos y formas de pagos</router-link>
          <router-link :to="{ name: 'help' }" class="index">Devoluciones y reembolsos</router-link>
          <router-link :to="{ name: 'help' }" class="index">Entrega</router-link>
          <router-link :to="{ name: 'about' }" class="index">Sobre nosótros</router-link>
        </div>
      </div>
  </main>
</template>

<script>
import { close } from 'ionicons/icons'
import { mapState } from 'vuex';


export default {
  data() {
    return {
      isAdmin: false,
      //icon
      close,
      //aplicar estilos elem list
      showDatos: 'datos',
      //desplazamiento form
      edit: true,
      update: false,
      //nombre en la bienvenida
      user:[],
      //mostrar datos al hacer click en la list
      dataUser: [],
      dataDirec: [],
      dataPedido: [],
      userPedido: [],
      dniUser: null,
      //datos del usuario
      nuevoNombre: '',
      nuevoApellido: '',
      nuevoDNI: '',
      nuevoCel: '',
      verificationDate: '',
      verificationDirec: '',
      //datos direc
      nuevoProv: '',
      nuevoLocalidad: '',
      nuevoCalle: '',
      nuevoCP: '',
      nuevoPiso: '',
      nuevoDpto: '',
      nuevoDatosE: '',
    };
  },
  methods:{
    closed(){
      this.edit = true;
    },
    editarDatos(){
      this.edit = false;
    },
    updateDatos(){
      if( this.nuevoNombre == '' || this.nuevoApellido =='' || this.nuevoDNI =='' || this.nuevoCel ==''){
        this.verificationDate = 'Complete todos los campos por favor.';
          return
      }
      else{
          this.edit = true;

          const newData = {
            email : this.userEmail,
            nombre : this.nuevoNombre,
            apellido : this.nuevoApellido,
            dni : this.nuevoDNI,
            cel : this.nuevoCel
          };

          const url = `http://127.0.0.1:5000/data/${this.userEmail}`;
          let options={
            method: 'PUT',
            headers: {'Content-Type':'application/json'},
            body: JSON.stringify(newData)
          }
    
          fetch(url,options)
            .then(res=>{
              if(res.ok){
                this.$router.push({ name: 'profile' });
                this.fetchData();
              }else if(res===400){
                return res.json()
              }else{
                throw new Error ('Error en la solicitud')
              }
            })
            .catch(err=>{
              alert('Error en la solicitud:' + err)
            })
        }
    },
    editDirec(){
      this.edit = false;
    },
    updateDirec() {
      if( this.nuevoProv == '' || this.nuevoLocalidad =='' || this.nuevoCalle =='' || this.nuevoCP =='' || this.nuevoPiso =='' || this.nuevoDpto ==''){
        this.verificationDirec = 'Complete todos los campos por favor.';
          return
      }
      else{
          if(this.nuevoDatosE == ''){
              this.nuevoDatosE = null
          }
          this.edit = true;

          const newData = {
          email : this.userEmail,
          provincia : this.nuevoProv,
          localidad : this.nuevoLocalidad,
          calle : this.nuevoCalle,
          codigo_postal : this.nuevoCP,
          piso : this.nuevoPiso,
          dpto : this.nuevoDpto,
          datos_extra : this.nuevoDatosE
          }

          const url = `http://127.0.0.1:5000/direc/${this.userEmail}`;
          let options={
              method: 'PUT',
              headers: {'Content-Type':'application/json'},
              body: JSON.stringify(newData)
          }

          fetch(url,options)
            .then(res=>{
                if(res.ok){
                  this.$router.push({ name: 'profile' });
                  this.fetchData();
                }else if(res===400){
                  return res.json()
                }else{
                  throw new Error ('Error en la solicitud')
                }
            })
            .catch(err=>{
              alert('Error en la solicitud:' + err)
            })
      }
    },
    fetchUser(){
      const url = 'http://127.0.0.1:5000/data';

      fetch(url)
        .then(res =>{
            if(res.ok){
              return res.json();
            }else{
              throw new Error('Error al obtener los datos');
            }
        })
        .then(data=>{
          this.user=data.filter(item => item.email === this.userEmail)
        })
        .catch(err=>{
          console.error('Error:', err)
        })
    },
    fetchData() {
      const urlData = 'http://127.0.0.1:5000/data';
      const urlDirec = 'http://127.0.0.1:5000/direc';

      fetch(urlData)
          .then(res => {
              if (res.ok) {
                return res.json();
              } else {
                throw new Error('Error al obtener los datos');
              }
          })
          .then(data => {
            this.dataUser = data.filter(item => item.email === this.userEmail);
            this.dniUser = this.dataUser[0].dni;
          })
          .catch(error => {
            console.error('Error:', error);
          });

      fetch(urlDirec)
          .then(res => {
              if (res.ok) {
                return res.json();
              } else {
                throw new Error('Error al obtener los datos');
              }
          })
          .then(data => {
            this.dataDirec = data.filter(item => item.email === this.userEmail);
          })
          .catch(error => {
            console.error('Error:', error);
          });
    },
    fetchPedidos(){
      fetch('http://127.0.0.1:5000/pedido')
      .then(res => {
        if(res.ok){
          return res.json();
        }else{
          throw new Error('Error al obtener los datos')
        }
      })
      .then(data => {
        this.dataPedido = data;
        this.fetchDetallePedido(this.dniUser)
      })
      .catch(err =>{
        console.error('Error:', err)
      })
    },
    getPedidoPorDNI(dni) {
      const arrayPorDni = this.dataPedido.filter(obj => obj.dni == dni);
      return arrayPorDni.map(pedidos => pedidos.numero);
    },
    fetchDetallePedido(dni) {
      const pedidos = this.getPedidoPorDNI(dni);

      if(dni !== null){
        pedidos.forEach((pedido)=>{
          const url = `http://127.0.0.1:5000/pedido/${pedido}`;
          fetch(url)
            .then(res => {
              if (res.ok) {
                return res.json();
              } else {
                throw new Error('Error al obtener los datos');
              }
            })
            .then(data => {
              this.userPedido.push(data);
            })
            .catch(err => {
              console.error('Error:', err);
            });
        });
      }
    },
    emitLogoutEvent() {
      this.$store.dispatch('userLoggedOut'); // Emitir el evento de cierre de sesión
    },
    Admin(){
      if(this.userEmail == 'admin@gmail.com'){
        this.isAdmin = true;
      }
    }
  },
  computed:{
    userEmail() {
      return this.$store.state.userEmail;
    },
    ...mapState(['userEmail'])// Mapear el estado userEmail de Vuex
    , 
    filteredUserData() {
      // Filtrar los datos del usuario utilizando el userEmail
      return this.dataUser.filter(item => item.email === this.userEmail);
    }
  },
  mounted(){
    this.fetchData();
    this.fetchUser();
    this.fetchPedidos();
    this.Admin();
  }
}  


</script>

<style scoped>
.main-perfil{
  width: 100%;
  height: 100vh;
  margin-top: 5%;
  overflow: hidden;
}

.welcome, 
.wrapper-list{
  width: 70%;
  height: 400px;
  margin: auto;
}


.wrapper-list{
  display: grid;
  grid-template-columns: 50% 50%;
  justify-content: center;
}

.welcome{
  height: 200px;
  display: flex;
}
.welcome h1{
  color: #27374D;
  margin-right: 15px;
  letter-spacing: 2px;
}


.list{
  width: 65%;
  height: 90%;
  position: relative;
  padding: 30px;
  display: grid;
  justify-content: center;
  border-right: 1px solid #27374D;
}
.list a{
  text-decoration: none;
  color: #27374D;
}
.list h3{
  font-size: 1.3em;
  padding: 20px 0;
  color: #27374D;
}
.list ul li{
  list-style: none;
  padding: 20px;
  color: #27374D;
  font-weight: 500;
  cursor: pointer;
  transition: .3s;
}
.list ul li:not(:nth-last-child(1)):after{
  content: '';
  height: 10px;
  width: 10px;
  position: absolute;
  transform: rotate(45deg);
  border-top: 2px solid #27374D;
  border-right: 2px solid #27374D;
  border-radius: 2px;
  margin: 4px 0;
  opacity: 0;
  transition: .7s;
}
.list ul li:hover::after{
  transform: translate(20px) rotate(45deg);
  opacity: 1;
}
.elem-list{
  transition: font-weight 5s;
}
.elem-list.on{
  font-weight: 600;
}


.fade-enter-active, .fade-leave-active {
  transition: opacity .5s
}
.fade-enter, .fade-leave-to{
  opacity: 0
}


.list-data, 
.list-direc,
.list-pedido{
  max-width: 100%;
  height: 90%;
  padding: 10px 30px;
  display: grid;
  color: #27374D;
}
.list-pedido{
  overflow: hidden;
  overflow-x: auto;
}
.data-perfil{
  width: 100%;
  height: 100%;
  display: flex;
}
.datos-personales, 
.data-direc, 
#edicion,
#edicion-direc{
  width: 300px;
  height: 100%;
  display: grid;
  align-items: center;
  transition: .3s;
}
.datos-personales div span, 
.data-direc div span,
.data-pedidos div span{
  padding-left: 10px;
  text-transform: capitalize;
}
.data-pedidos{
  background: transparent;
  border-radius: 2px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, .3); 
  border-top: 2px solid rgba(255, 255, 255, 0.7);
  display: flex;
  justify-content: center;
  flex-direction: column;
  width: 200px;
  height: 95%;
  margin-right: 10px;
}
.data-pedidos div{
  margin: 20px 0;
  padding: 10px;
}

#edicion, 
#edicion-direc{
  filter: opacity(0);
  transform: translate(100%);
  pointer-events: none;
}
#edicion div, 
#edicion-direc div{
  display: grid;
}
#edicion label,
#edicion-direc label{
  font-weight: 600;
}
#edicion input,
#edicion-direc input, 
#edicion-direc textarea{
  padding: 5px;
  letter-spacing: 1px;
  width: 100%;
  border: none;
  border-radius: 3px;
  transition: .5s;
  font-weight: 500;
}
#edicion input:focus,
#edicion-direc input:focus,
#edicion-direc textarea:focus{
  background-color: #27374D;
  color: #fff;
}
.verification{
  font-weight: 400;
  color: red;
}

.edit button, 
.actualizar{
  padding: 5px 0;
  background: #27374D;
  border: none;
  outline: none;
  border-radius: 3px;
  cursor: pointer;
  font-size: 1em;
  color: #fff;
  font-weight: 500;
  transition: .3s;
  letter-spacing: 2px;
  width: 50%;
  margin-top: 10px;
}
.datos-personales.edit,
.data-direc.edit{
  transform: translateX(100%);
  filter: opacity(0);
  pointer-events: none;
}

#edicion.update,
#edicion-direc.update{
  filter: opacity(1);
  transform: translateX(-100%);
  pointer-events: auto;
}


.close-datos{
  position: absolute;
  bottom: 100%;
  left: 90%;
  width: 45px;
  height: 45px;
  filter: drop-shadow(0px 3px 3px rgba(0,0,0,0.5));
  font-size: 2em;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  border-bottom-left-radius: 20px;
  cursor: pointer;
  z-index: 1;
}


.help{
  width: 70%;
  height: 200px;
  color: #27374D;
  margin: 20px auto;
  display: grid;
  grid-template-rows: 10% 90%;
  place-content: center;
  border-top: 2px solid #27374D;
  padding-top: 20px;
}
.help h3{
  padding: 10px 0;
  font-size: 1.3em;
}
.help-data{
  display: grid;
  place-content: center;
  grid-template-columns: 50% 50%;
}
.help-data a{
  width: 250px;
  text-decoration: none;
  color: #27374D;
  font-weight: 500;
  padding: 10px 0;
  margin-left: 30px;
}
.help-data a:hover{
  text-decoration: underline;
}

@media (max-width: 768px){
  .main-perfil{
    height: 100%;
    margin-top: 85px;
  }

  .welcome{
    width: 90%;
    height: 100%;
    font-size: .8em;
    margin-bottom: 20%;
  }
  .wrapper-list{
    height: 100%;
    width: 90%;
  }
  .list {
    width: 90%;
    font-size: 1.1em;
    padding: 0;
  }
  .list ul li:hover::after{
    transform: translate(10px) rotate(45deg);
    opacity: 1;
  }
  .list-data,
  .list-direc,
  .list-pedido{
    height: 100%;
    padding: 0;
    font-size: 1.1em;
  }
  .datos-personales, 
  .data-direc, 
  #edicion,
  #edicion-direc{
    width: 150px;
    height: 100%;
    margin-bottom: 5%;
  }
  #edicion input,
  #edicion-direc input, 
  #edicion-direc textarea{
    margin: 5% 0;
    padding: 5px;
    letter-spacing: 1px;
    width: 100%;
    height: 30px;
    border: none;
    border-radius: 3px;
    transition: .5s;
    font-weight: 500;
  }
  .container-message{
    width: 100%;
    margin: 5% 0;
  }
  .verification{
    width: 100%;
    font-size: .8em;
    font-weight: 600;
  }
  .edit button, 
  .actualizar{
    padding: 5px 0;
    width: 100%;
  }
  .help{
    width: 90%;
    height: 100%;
    border-top: 2px solid #27374D;
    display: flex;
    flex-direction: column;
  }
  .help-data{
    display: flex;
    flex-direction: column;
  }
}

@media (min-width: 769px) and (max-width: 1200px){
  .main-perfil{
    height: 100%;
  }
  .help{
    margin-top: 15%;
  }
}
</style>