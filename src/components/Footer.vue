<template>
    <footer>
        <div class="wrapper">
            <div class="icons">
                <a href="#"><ion-icon :src="logoFacebook"></ion-icon></a>
                <a href="#"><ion-icon :src="logoInstagram"></ion-icon></a>
            </div>
            <div class="links">
                <router-link :to="{ name:'help' }">Ayuda</router-link>
                <router-link :to="{ name:'request-cancellation' }">Arrepentimiento de compra</router-link>
                <router-link :to="{ name:'privacy-policy' }">Politica de privacidad</router-link>
                <router-link :to="{ name:'terms-and-conditions' }">Terminos y condiciones</router-link>
            </div>
            <div class="text">
                <p><ion-icon :src="card"></ion-icon>Compra Segura</p>
                <p><img src="../assets/img/icons/logoCheq.png" alt="logo"> 2023. Todos los derechos reservados</p>
            </div>
        </div>
    </footer>
</template>

<script lang="ts">
    import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
    import { defineComponent } from 'vue';
    import { card, logoInstagram, logoFacebook } from 'ionicons/icons';

    export default defineComponent({
    name: 'Footer',
    components: {
        IonContent,
        IonHeader,
        IonPage,
        IonTitle,
        IonToolbar
    }, setup() {
        return{
            card,
            logoInstagram,
            logoFacebook,
        }
    }
})

</script>

<style scoped>
footer{
    width: 100%;
    height: 350px;
    background-color: #27374D;
    position: relative;
    left: 0;
    bottom: 0;
    border-top: 2px solid #fff;
}
.icons, .links{
    width: 100%;
    height: 135px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.icons a{
    font-size: 2.5em;
    color: #fff;
    margin: 0 1em;
}

.links{
    border-bottom: 1px solid #fff;
}

.text{
    display: flex;
    justify-content: space-between;
    padding: 25px;
}

.links a, .text p{
    color: #fff;
    margin: 0 3em;
}

.text p img{
    width: 20px;
    height: 20px;
}
.text p ion-icon{
    margin: 0 0.3em;
    font-size: 0.9em;
}

@media (max-width: 768px){
    footer{
        height: 400px;
        bottom: 0;
    }
    .links{
        display: flex;
        flex-direction: column;
        border: none;
        padding-bottom: 5%;
    }
    .links a{
        margin: 2% 0;
    }
    .text{
        border-top: 1px solid #ffffff;
        margin: 2%;
    }
    .text p{
        font-size: 0.7em;
    }
}
</style>