<template>
    <header>
        <router-link :to="{ name: 'home' }"><img src="../assets/img/icons/logoCheq.png" alt="logo"></router-link>

        <div class="shop-icon">
            <button class="shop" @click="viewCarshop"><ion-icon :src="cart"></ion-icon></button>
        </div>
        <div class="mobile">
            <div class="container-nav">
                <router-link :to="{ name: 'home' }" class="index"><ion-icon :src="home"></ion-icon></router-link>
                <router-link :to="{ name: 'about' }" class="contacto"><ion-icon :src="call"></ion-icon></router-link>
                <a class="cuenta" @click="toggleLogin" v-if="profileOff">
                    <ion-icon :src="logIn"></ion-icon>
                </a>
                <router-link :to="{ name: 'profile' }" class="perfil" v-else><ion-icon :src="person"></ion-icon></router-link>
                
            </div>
        </div>
        
        <nav>
            <router-link :to="{ name: 'home' }" class="index">Inicio</router-link>
            <router-link :to="{ name: 'about' }" class="contacto">Contacto</router-link>
            <a class="cuenta" @click="toggleLogin" v-if="profileOff">
                {{ isAuthenticated ? userEmail : 'Cuenta' }}
            </a>
            <router-link :to="{ name: 'profile' }" class="perfil" v-else>Perfil</router-link>
            <button class="shop" @click="viewCarshop"><ion-icon :src="cart"></ion-icon></button>
        </nav>
    </header>
    <Transition>
        <div>
            <Login :showLogin="showLogin" @close-login="closeLogin" @register-success="createProfile" @cambiarCuenta="navCuenta" @change-profile="navProfile" />
            <Carshop :showCarshop="showCarshop" @close-carshop="closeCarshop" />
        </div>
    </Transition>
</template>

<script>
import { cart, home, call, person, logIn } from 'ionicons/icons';
import { ref } from 'vue';
import Carshop from './Carshop.vue';
import Login from './Login.vue';

export default{
    props:{
        isAuthenticated: Boolean,
        userEmail: String,
    },
    data(){
        return{
            cart,
            home,
            call,
            person,
            logIn,
            //login
            showLogin:ref(false),
            //nav
            profileOff: ref(true),
            //carshop
            showCarshop: ref(false),
            //menu burger
            isMenuOpen: false,
        }
    },
    methods:{
        toggleMenu() {
            this.isMenuOpen = !this.isMenuOpen;
        },
        viewCarshop(){
            this.showCarshop = !this.showCarshop;
        },
        closeCarshop(){
            this.showCarshop = false
        },
        toggleLogin(){
            this.showLogin = !this.showLogin;
        },
        closeLogin(){
            this.showLogin = false; 
        },
        navProfile(){
            this.profileOff = false;
        },
        navCuenta(){
            this.profileOff = true;
        },
        createProfile(email){
            const newData = {
                email : email,
                nombre : null,
                apellido : null,
                dni : null,
                cel : null
                }

            const newDirec = {
                email : email,
                provincia : null,
                localidad : null,
                calle : null,
                codigo_postal : null,
                piso : null,
                dpto : null,
                datos_extra : null
            }

            const urlData = 'http://127.0.0.1:5000/data';
            const urlDirec = 'http://127.0.0.1:5000/direc';

            let optionsData={
                method: 'POST',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify(newData)
            }
            let optionsDirec={
                method: 'POST',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify(newDirec)
            }
            
            // Primera solicitud Fetch para urlData con optionsData
            fetch(urlData, optionsData)
                .then(res => {
                    if (res.ok) {
                        return res.json()
                    } else if (res.status === 400) {
                        return res.json();
                    } else {
                        throw new Error('Error en la solicitud a urlData.');
                    }
                })
                .catch(err => {
                    console.error('Error en la solicitud a urlData:', err);
                });

            // Segunda solicitud Fetch para urlDirec con optionsDirec
            fetch(urlDirec, optionsDirec)
                .then(res => {
                    if (res.ok) {
                        return res.json()
                    } else if (res.status === 400) {
                        return res.json();
                    } else {
                        throw new Error('Error en la solicitud a urlDirec.');
                    }
                })
                .catch(err => {
                    console.error('Error en la solicitud a urlDirec:', err);
                });
        }
    },
    computed:{
        isLoginIcon() {
            return this.isAuthenticated && this.profileOff;
        }
    },
    components:{
        Login,
        Carshop
    },
}
</script>


<style scoped>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Raleway', sans-serif;
}

header{
    background-color: #27374D;
    display: flex;
    height: 5em;
    width: 100%;
    justify-content: space-between;
    align-items: center;
    padding: 0 150px;
    position: static;
    z-index: 99;
}

header img{
    width: 80px;
    height: 80px;
    filter:contrast(0);
}

nav a{
    position: relative;
    margin-right: 3em;
    text-decoration: none;
    font-size: 1.2em;
    font-weight: 600;
    color: white;
    transition: 0.5s;
    cursor: pointer;
}

nav a::after{
    content: '';
    background-color: white;
    position: absolute;
    bottom: -6px;
    left: 0;
    width: 100%;
    height: 3px;
    border-radius: 5px;
    transform-origin: right;
    transform: scaleX(0);
    transition: transform 0.5s;
}

nav a:hover::after{
    transform-origin: left;
    transform: scaleX(1);
}


.shop{
    width: 120px;
    height: 40px;
    background-color: #27374D;
    border: 2px solid #fff;
    font-size: 1.5em;
    color: #ffffff;
    border-radius: 10px;
    cursor: pointer;
    transition: 0.5s;
}

.shop:hover{
    background-color: white;
    color: #27374D;
}

.shop.active{
    background-color: white;
    color: #27374D;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.3s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

.shop-icon {
    display: none;
    cursor: pointer;
    padding: 15px;
}

nav.navActive {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background-color: #27374D;
    z-index: 1;
    transform: translateY(-100%);
    transition: transform 0.3s ease-in-out;
}

.mobile {
    display: none;
    width: 100%;
    height: 20px;
    background: #27374D;
    position: fixed;
    left: 0;
    bottom: 0;
    z-index: 999;
}
.container-nav {
    height: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    font-size: 2em;
    transform: translateY(-15px);
}
.container-nav a{
    color: #fff;
    border: 10px solid #27374D;
    border-radius: 50%;
    background: #27374D;
    position: relative;
}
.container-nav a::before{
    content: '';
    height: 15px;
    width: 15px;
    position: absolute;
    top: 25%;
    left: 125%;
    border-bottom-left-radius: 25px;
    box-shadow: -3px 4px 0 3px #27374D;
    background-color: transparent;
}
.container-nav a::after{
    content: '';
    height: 15px;
    width: 15px;
    position: absolute;
    top: 25%;
    right: 125%;
    border-bottom-right-radius: 25px;
    box-shadow: 3px 4px 0 3px #27374D;
    background-color: transparent;
}



@media (max-width: 767px) {
    header {
        top: 0;
        height: 80px;
        position: fixed;
        padding: 0 20px;
        z-index: 99;
    }
    header img {
        width: 60px;
        height: 60px;
    }
    .shop-icon {
        display: block;
    }
    .mobile{
        display: block;
        box-shadow: 0px 0px 5px black;
        z-index: 99;
    }
    nav {
        display: none;
    }
    nav a {
        font-size: 1em;
        margin-right: 2em;
    }
    .shop {
        font-size: 1.5em;
        width: 50px;
        height: 50px;
    }
}

@media (min-width: 768px) and (max-width: 1200px) {
    header {
        padding: 0 50px;
        z-index: 99;
    }

    header img {
        width: 70px;
        height: 70px;
    }

    nav a {
        font-size: 1.1em;
    }

    .shop {
        font-size: 1.3em; 
    }
}

</style>