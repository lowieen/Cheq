<template>
    <div class="usuario" :class="{ active: showLogin }" :style="{ height: height + 'px'}">
        <span class="icon-close">
            <ion-icon :src="close" @click="closed"></ion-icon>
        </span>
        <div class="caja-form login" :style="{ transform: 'translateX('+ xOffset + 'px)' }">
            <h3>Iniciar Seción</h3>
            <form action="#">
                <div class="container-input">
                    <span class="icon"><ion-icon :src="mail"></ion-icon></span>
                    <input class="email" type="email" required name="email" v-model="logEmail">
                    <label class="LabelEmail" :class="{ 'move': logEmail }">Email</label>
                    <div class="verification"></div>
                </div>
                <div class="container-input">
                    <span class="icon"><ion-icon :src="lockClosed"></ion-icon></span>
                    <input class="password" type="password" required v-model="logPass">
                    <label :class="{ 'move': logPass }">Contraseña</label>
                    <div class="verification"></div>
                </div>
                <div class="terminos-recuerdame">
                    <router-link @click="closed" :to="{ name: 'restore-password' }">Olvide la contraseña</router-link>
                </div>
                <button type="button" class="btn" @click="login">Iniciar sesión</button>
                <div class="verification" v-if="logVerification">{{ logVerification }}</div>
                <div class="verification" v-if="logVerificationError"> {{ logVerificationError }}</div>
                <div class="login-register">
                    <p>No tengo una cuenta <a href="#" class="register-link" @click="toRegister">Registrarme</a></p>
                </div>
            </form>
        </div>

        <div class="caja-form registro" :style="{ transform: 'translateX('+ (800 + xOffset) + 'px)' }">
            <h3>Registro</h3>
            <form action="#">
                <div class="container-input">
                    <span class="icon"><ion-icon :src="mail"></ion-icon></span>
                    <input type="email" required name="email" class="email" v-model="emailInput" @input="validateEmail" @blur="handleBlur">
                    <label for="email" :class="{ 'move': emailInput }">Email</label>
                    <div class="verification" v-if="shouldShowEmailError">Correo electrónico no válido</div>
                </div>
                <div class="container-input">
                    <span class="icon"><ion-icon :src="lockClosed"></ion-icon></span>
                    <input type="password" required name="password" v-model="passwordInput">
                    <label for="password" :class="{ 'move': passwordInput }">Contraseña</label>
                </div>
                <div class="container-input">
                    <input type="password" required name="password2" v-model="confPasswordInput">
                    <label for="password2" :class="{ 'move': confPasswordInput }">Repita la contraseña</label>
                    <div class="verification" v-if="isConfPassValid">Las contraseñas no coinciden</div>
                </div>
                <div class="terminos-recuerdame">
                    <label><input type="checkbox" class="check" v-model="isChecked">Acepto todos los términos y condiciones</label>
                </div>

                <button type="button" class="btn" :disabled="!isFormValid" @click="registerUser">Registrarme</button>
                <div class="verification success" v-if="verificationMessage"> {{ verificationMessage }}</div>

                <div class="login-register">
                    <p>Ya tengo una cuenta <a class="login-link" @click="toLogin">Iniciar sesión</a></p>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { mail, close, lockClosed } from 'ionicons/icons'
import { ref } from 'vue';

export default{
    props: {
        showLogin: Boolean,
    },
    data(){
        return{
            //icons
            mail,
            close,
            lockClosed,
            //style etiquetas flotantes
            //validform
            emailInput: '',
            passwordInput: '',
            confPasswordInput: '',
            isChecked: false,
            isValidEmail: false,
            shouldShowEmailError: false,
            //style container login
            xOffset: 0,
            height: null,
            //register user
            verificationMessage: '',
            //login user
            logEmail: '',
            logPass: '',
            logVerification: '',
            logVerificationError: '',
            //autenticacion inicio de sesion
            isAuthenticated: localStorage.getItem('isAuthenticated') === 'true',
            //obtener email
            logEmail: ref(''),
            logPass: ref('')
        };
    },
    methods:{
        closed(){
            this.$emit('close-login'); // Emitir evento al componente padre
        },
        async login(){
            const email = this.logEmail.trim();
            const pass = this.logPass.trim();

            if (email === '' || pass === ''){
                this.logVerification = 'Por favor complete todos los campos.';
                return false
            }
            localStorage.setItem('isAuthenticated', 'true');
            this.isAuthenticated = true;

            this.loginUser(email, pass);
            return true
        },
        loginUser(email, pass){
            const store = this.$store;

            const url = 'http://127.0.0.1:5000/user';
            const data = {email: email, password: pass};

            fetch(url, {
                method: 'POST',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify(data)
            })

            .then(res => {
                if(res.ok){
                    this.logVerification = '';
                    this.logVerificationError = '';
                    const userEmail = this.logEmail; // Obtén el correo electrónico
                    store.dispatch('updateUserEmail', userEmail); // Actualiza el valor en el store
                }else if(res.status === 400){
                    return res.json()
                }else{
                    throw new Error('Error en la solicitud.');
                }
            })
            .then(data =>{
                if(data && data.error){
                    this.logVerification = data.error;
                }else{
                    this.$emit('close-login');
                    this.$emit('change-profile');
                }
            })
            .catch(err =>{
                console.error('Error en la solicitud:', err);
                this.logVerification = 'Error en la solicitud. Por favor, inténtelo de nuevo más tarde.';
            })
        },
        registerUser(){
            if (this.isFormValid) {

                const url = 'http://127.0.0.1:5000/users';
                var options = {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({email:this.emailInput, password:this.passwordInput, reset_token:null, reset_token_expiration:null})
                }

                fetch(url,options)
                    .then(res => {
                        if (res.ok) {
                            this.$emit('register-success', this.emailInput); // Emitir evento al componente padre
                            this.verificationMessage = 'Usuario registrado exitosamente.';
                            this.emailInput = '';
                            this.passwordInput = '';
                            this.confPasswordInput = '';
                            this.isChecked = false;
                        }else if (res.status === 400){
                            return res.json();
                        }else{
                            throw new Error('Error en la solicitud.');
                        }
                    })
                    .then(data => {
                        if (data && data.error) {
                            this.verificationMessage = data.error;
                        }
                    })
                    .catch(error => {
                        console.error('Error en la solicitud:', error);
                        this.verificationMessage = 'Error en la solicitud. Por favor, inténtelo de nuevo más tarde.' + error;
                    });
            }
        },
        validateEmail(){
            const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
            this.isValidEmail = emailRegex.test(this.emailInput);
        },
        handleBlur() {
            if (this.emailInput === '') {
                this.shouldShowEmailError = false;
            } 
            else{
                this.shouldShowEmailError = !this.isValidEmail;
            }
        },
        toLogin(){
            this.xOffset += 800;
            this.height = 440;
        },
        toRegister(){
            this.xOffset = -800;
            this.height = 520;
        },
        logout(){
            fetch('http://127.0.0.1:5000/user/logout', {
                method: 'GET',
                headers: {'Content-Type': 'application/json'},
                credentials: 'same-origin' // Enviar las cookies de sesión al servidor
            })
            .then(res => {
                if (res.ok) {
                    localStorage.setItem('isAuthenticated', 'false');
                    this.isAuthenticated = false;
                    localStorage.setItem('isAdmin','false');
                    this.isAdmin = false;
                    this.$emit('cambiarCuenta');
                    this.$router.push({ name: 'home' });
                } else {
                    console.error('Error en el cierre de sesión:', res.status, res.statusText);
                }
            })
            .catch(error => {
                console.error('Error en la petición de cierre de sesión:', error);
            });
        },
    },
    computed:{
        isFormValid(){
            return this.isValidEmail && this.passwordInput !== '' && this.confPasswordInput !== '' && this.confPasswordInput == this.passwordInput && this.isChecked
        },
        isConfPassValid(){
            return this.confPasswordInput !== this.passwordInput //Devuelve true => isConfPassValid = true
        }
    },
    created() {
        this.$store.subscribeAction((action, state) => {
            if (action.type === 'userLoggedOut') {
                this.logout(); // Llamar al método logout cuando se emite el evento 
            }
        });
    }
}
</script>
<style scoped>
.usuario{
    position: absolute;
    right: 0;
    width: 400px;
    height: 440px;
    background: transparent;
    border-radius: 2px;
    backdrop-filter: blur(20px);
    box-shadow: 0 0 30px rgba(0, 0, 0, .5); 
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    transition: filter .5s ease, height .2s ease, top .1s ease, opacity 0.5s ease, visibility 0.5s ease;
    z-index: 99;
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}

.usuario.active {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
}

.usuario .caja-form{
    width: 100%;
    padding: 40px;
}

.usuario .caja-form.registro{
    position: absolute;
    transition: 0.2s ease;
}

.usuario .icon-close{
    position: absolute;
    top: 0;
    right: 0;
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

.caja-form h3{
    font-size: 2em;
    color: #27374D;
    text-align: center;
}

.container-input{
    position: relative;
    width: 100%;
    height: 50px;
    border-bottom: 2px solid #27374D;
    margin: 30px 0;
}

.container-input label{
    position: absolute;
    top: 50%;
    left: 5px;
    transform: translateY(-50%);
    font-size: 1em;
    color: #27374D;
    font-weight: 500;
    pointer-events: none;
    transition: .5s;
}
.LabelEmail.move,
label.move {
  top: -5px; 
}

.container-input input{
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    font-size: 1em;
    color: #27374D;
    font-weight: 600;
    padding: 0 35px 0 5px;
}

.container-input .icon{
    position: absolute;
    right: 8px;
    font-size: 1.2em;
    color: #27374D;
    line-height: 57px;
}

.terminos-recuerdame{
    font-size: .9em;
    color: #27374D;
    font-weight: 500;
    margin: -10px 0 15px;
    display: flex;
    justify-content: end;
}
.caja-form.registro .terminos-recuerdame{
    justify-content: start;
}

.terminos-recuerdame label input{
    accent-color: #27374D;
    margin-right: 3px;
}

.terminos-recuerdame a{
    color: #27374D;    
    text-decoration: none;
}

.terminos-recuerdame a:hover{
    text-decoration: underline;
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
}

.btn:disabled{
    background: #27374d79;
    cursor: not-allowed;
}

.login-register{
    font-size: .9em;
    color: #27374D;
    text-align: center;
    font-weight: 500;
    margin: 25px 0 10px;
}

.login-register p a{
    color: #27374D;
    text-decoration: none;
    font-weight: 600;
    cursor: pointer;
}

.login-register p a:hover{
    text-decoration: underline;
}

.usuario .caja-form.login{
    transition: transform .18s ease;
    transform: translateX(0);
}

.verification{
    color: red;
    padding: 5px;
    font-size: .7em;
    font-weight: 700;
}

.verification.success{
    color: green;
}

@media (max-width: 768px){
    .usuario{
        height: 100% !important;
        width: 100%;
        position: fixed;
        font-size: 1.2em;
        top: 80px;
        z-index: 98;
        background: #ffffff50;
    }

}


</style>