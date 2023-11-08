<template>
  <div class="wrapper">
    <div class="container">
      <div class="container-correo">
        <div>
          <h2>Ingresa tu Correo Electrónico</h2>
        </div>
        <div>
          <input type="email" v-model="email" required @input="validarEmail" placeholder="ejemplo@gmail.com">
          <div class="verification" v-if="messageError">{{ messageError }}</div>
        </div>
        <div>
          <button class="btn" type="button" @click="isOkEmail" :disabled="!isEmailValid">{{msjBtn}}</button>
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
export default {
  data() {
    return {
      email: '',
      isEmailValid: false,
      allUsers: [],
      messageError: '',
      msjBtn: 'Continuar'
    };
  },
  methods: {
    validarEmail() {
      const patronEmail = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
      this.isEmailValid = patronEmail.test(this.email);
    },
    isOkEmail(){
      const url = 'http://127.0.0.1:5000/users'
      fetch(url)
        .then(res => {
          if(res.ok){
            return res.json()
          } else {
            throw new Error('Error en la solicitud')
          }
        })
        .then(data => {
          this.allUsers = data;
          if(this.allUsers.some(elem => elem.email == this.email)){
            this.sendEmail(this.email)
          } else {
            this.messageError = 'El correo electrónico ingresado es incorrecto o no está registrado.'
          }
        })
        .catch(err => {
          console.error('Error: ', err)
        })
    },
    sendEmail(email){
      const mail={
        email:email
      }
      let url = 'http://localhost:5000/restablecer-contrasena';
      var options = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(mail)
      }
      fetch(url, options)
        .then(res => {
          if(res.ok){
            this.msjBtn = 'Correo Enviado!';
            return res.json()
          } else {
            throw new Error('Error en la solicitud')
          }
        })
        .catch(err => {
          console.error('Error: ', err)
        })
    }
  },
};
</script>

<style scoped>
.wrapper{
  width: 100%;
  height: 85vh;
  overflow: hidden;
  padding: 3% 0;
}
.container{
  width: 70%;
  height: 100%;
  margin: auto;
  border-top: 3px solid #fff;
  border-radius: 3px;
  box-shadow: 0 3px 20px rgba(0, 0, 0);
  background-color: #ffffff50;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  position: relative;
}
.container h2{
  color: #27374D;
  font-size: 2em;
  margin-bottom: 10%;
  letter-spacing: 1px;
}
.container-correo{
  transition: transform .18s ease;
  transform: translateX(0);
}
.container input{
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    font-size: 1em;
    color: #27374D;
    font-weight: 600;
    padding: 5%;
    margin: 5% 0;
    border-bottom: 1px solid #27374D;
}
.btn{
    width: 100%;
    height: 45px;
    background: #27374D;
    border: none;
    outline: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    color: #fff;
    font-weight: 500;
    transition: .3s;
    letter-spacing: 2px;
}

.btn:disabled{
    background: #27374d79;
    cursor: not-allowed;
}

.verification{
    color: red;
    padding: 5px;
    font-size: .7em;
    font-weight: 700;
}

@media (max-width: 768px){
  .wrapper{
    height: 100vh;
    margin-top: 20%;
  }
  .container{
    height: 100%;
    width: 95%;
  }
  .container h2{
    text-align: center;
  }
  .container-correo{
    width: 90%;
  }
  .container input{
    font-size: 1.2em;
  }
  .btn{
    margin-top: 5%;
  }
  .verification{
    font-size: .9em;
  }
}
@media (max-width: 450px){
  .wrapper{
    margin-top: 25%;
  }
}
</style>