<template>
    <div class="wrapper">
        <div class="container">
            <div class="container-password">
                <h2>Restablecer Contraseña</h2>
                <form>
                  <div class="form-group">
                    <label for="password">Nueva Contraseña</label>
                    <input type="password" id="password" v-model="password" required @input="validarPass">
                  </div>
                  <div class="form-group">
                    <label for="confirmPassword">Confirmar Contraseña</label>
                    <input type="password" id="confirmPassword" v-model="confirmPassword" required @input="validarPass">
                  </div>
                  <button type="button" class="btn" @click="resetPassword" :disabled="!isOk">Restablecer Contraseña</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      messageError: '',
      password: '',
      confirmPassword: '',
      isOk: false,
      token: '',
      checkResetToken: [],
    };
  },
  created() {
    // Cuando se carga el componente, obtén el token de la URL
    this.token = this.$route.params.token;
  },
  methods: {
    checkToken(){
      fetch('http://localhost:5000/users')
        .then(res => {
          if(res.ok){
            return res.json()
          } else {
            throw new Error ('Erro en la solucitud')
          }
        })
        .then(data =>{
          this.checkResetToken = data.filter(elem => elem.reset_token)
          if(this.checkResetToken.length == 0){ 
            alert('El Token para el cambio de contraseña ha expirado.')
            this.$router.push({ name: 'home' });
          }
        })
        .catch(err =>{
          console.error('Error: ',err)
        })
    },
    validarPass() {
      if (this.password === this.confirmPassword) {
        this.isOk = true;
      } else {
        this.isOk = false;
      }
    },
    resetPassword() {
      const newPassword = this.password;

      fetch(`http://localhost:5000/new-password/${this.token}`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify({ password: newPassword }),
      })
        .then((response) => {
          if (response.ok) {
            this.token = '';
            this.$router.push({ name: 'home' });
          }
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
  },
  mounted(){
    this.checkToken();
  }
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
.container-password{
  position: absolute;
  transition: 0.2s ease;
}
.container-password label{
    font-size: 1em;
    color: #27374D;
    font-weight: 500;
    pointer-events: none;
    transition: .5s;
    letter-spacing: 1px;
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
  .container-password{
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