<template>
    <div class="ventana urban-catalogo" :style="{top: yOffsetU + '%'}">
        <span class="cruz cruzU" @click="closeArt"><ion-icon :src="close"></ion-icon></span>
        <div class="enlaces">
            <h2>Colección invierno</h2>
            <p>Visita tambien nuestros
                <router-link :to="{ name: 'buzos'}"><span>buzos,</span></router-link>
                <router-link :to="{ name: 'camperas'}"><span>camperas,</span></router-link>
                <router-link :to="{ name: 'remeras'}"><span>remeras,</span></router-link>
                <router-link :to="{ name: 'pantalones'}"><span>pantalones</span></router-link>
                o
                <router-link :to="{ name: 'camisas'}"><span>camisas.</span></router-link>
            </p>
        </div>
        <div class="order-search">
            <div class="search">
                <ion-icon :src="searchSharp"></ion-icon>
                <input type="text" v-model="searchU">
            </div>
        </div>
        <div class="articulos urban">
            <div v-for="elem in filteredProductosU" :key="elem.id">
                <div>
                    <img :src="elem.url_Image" alt="Articulo">
                    <h4>{{elem.nombre}}</h4>
                    <p>${{elem.precio}}</p>
                    <div class="detail">
                        <router-link :to="{ name: 'product-detail', params: { id: elem.id } }">
                        Ver
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <div class="ventana vestir-catalogo" :style="{top: yOffsetV + '%'}">
        <span class="cruz cruzV" @click="closeArt"><ion-icon :src="close"></ion-icon></span>
        <div class="enlaces">
            <h2>Colección invierno</h2>
            <p>Visita tambien nuestros
                <router-link :to="{ name: 'buzos'}"><span>buzos,</span></router-link>
                <router-link :to="{ name: 'camperas'}"><span>camperas,</span></router-link>
                <router-link :to="{ name: 'remeras'}"><span>remeras,</span></router-link>
                <router-link :to="{ name: 'pantalones'}"><span>pantalones</span></router-link>
                o
                <router-link :to="{ name: 'camisas'}"><span>camisas.</span></router-link>
            </p>
        </div>
        <div class="order-search">
            <div class="search">
                <ion-icon :src="searchSharp"></ion-icon>
                <input type="text" v-model="searchV">
            </div>
        </div>
        <div class="articulos vestir">
            <div v-for="elem in filteredProductosV" :key="elem.id">
                <div>
                    <img :src="elem.url_Image" alt="Articulo">
                    <h4>{{elem.nombre}}</h4>
                    <p>${{elem.precio}}</p>
                    <div class="detail">
                        <router-link :to="{ name: 'product-detail', params: { id: elem.id } }">
                        Ver
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <main class="main">
        <section>
            <div class="inicio">
                <div class="names">
                    <div class="Che">
                        <h1 class="name1" @click="viewUrban">Ch</h1>
                    </div>
                    <div class="eq">
                        <h1 class="name2"  @click="viewVestir">eq</h1>
                    </div>
                </div>
                <div class="gray" @click="viewUrban">
                    <img src="/src/assets/img/urban.png" alt="Ropa urbana" class="casual">
                </div>
                <div class="lightblue" @click="viewVestir">
                    <img src="/src/assets/img/vestir.png" alt="Ropa de vestir" class="evento">
                </div>
            </div>
        </section>
        <section class="catalogo">
            <h2>CATALOGO</h2>
            <div class="grid-container">
                <div class="grid-item">
                    <figure>
                        <router-link :to="{ name: 'camperas' }">
                            <img src="/src/assets/img/catalogo/camperaU.jpg" alt="campera">
                        </router-link>
                    </figure>
                </div>
                <div class="grid-item">
                    <figure>
                        <router-link :to="{ name: 'buzos' }">
                            <img src="/src/assets/img/catalogo/buzoU.jpg" alt="buzos">
                        </router-link>
                    </figure>
                </div>
                <div class="grid-item">
                    <figure>
                        <router-link :to="{ name: 'remeras' }">
                            <img src="/src/assets/img/catalogo/remeraU.jpg" alt="remeras" >
                        </router-link>
                    </figure>
                </div>  
                <div class="grid-item">
                    <figure>
                        <router-link :to="{ name: 'pantalones' }">
                            <img src="/src/assets/img/catalogo/pantalonU.jpg" alt="pantalones" >
                        </router-link>
                    </figure>
                </div>  
                <div class="grid-item">
                    <figure>
                        <router-link :to="{ name: 'camperas' }">
                            <img src="/src/assets/img/catalogo/camperaV.jpg" alt="camperas">
                        </router-link>
                    </figure>
                </div>  
                <div class="grid-item">
                    <figure>
                        <router-link :to="{ name: 'buzos' }">
                            <img src="/src/assets/img/catalogo/buzoV.jpg" alt="buzos" >
                        </router-link>
                    </figure>
                </div> 
                <div class="grid-item">
                    <figure>
                        <router-link :to="{ name: 'camisas' }">
                            <img src="/src/assets/img/catalogo/camisaV.jpg" alt="camisas">
                        </router-link>
                    </figure>
                </div>
                <div class="grid-item">
                    <figure>
                        <router-link :to="{ name: 'pantalones' }">
                            <img src="/src/assets/img/catalogo/pantalonV.jpg" alt="pantalones">
                        </router-link>
                    </figure>
                </div>  
            </div>
            <div class="container-pagos">
                <div class="tres-cuotas">
                    <p>3</p>
                    <p>Cuotas sin interes</p>
                </div>
                <span></span>
                <div class="seis-cuotas">
                    <p>6</p>
                    <p>Cuotas sin interes</p>
                </div>
            </div>
            <div class="info">
                <div>
                    <ion-icon :src="cube"></ion-icon>
                    <h4>Envio gratis a todo el pais</h4>
                    <p>en compras superiores a $25.000</p>
                </div>
                <div class="store">
                    <ion-icon :src="storefront"></ion-icon>
                    <h4>Retiro en tienda</h4>
                    <p>Elegí tu tienda más cercana</p>
                </div>
                <div>
                    <ion-icon :src="helpCircle"></ion-icon>
                    <h4>¿Necesitas ayuda?</h4>
                    <p>Aclará todas tus dudas o consultas</p>
                </div>
                <div>
                    <ion-icon :src="checkmarkCircle"></ion-icon>
                    <h4>Compra 100% segura</h4>
                    <p>Tu información protegida y garantizada</p>
                </div>
                <div class="card">
                    <ion-icon :src="card"></ion-icon>
                    <h4>Financiación</h4>
                    <p>Conocé las promociones bancarias</p>
                </div>
                <div>
                    <ion-icon :src="sync"></ion-icon>
                    <h4>Cambios</h4>
                    <p>Hasta 30 días después de la compra</p>
                </div>
            </div>
            <router-link :to="{ name: 'about' }" class="extra">
                <ion-icon :src="pin"></ion-icon>
                <p>Encontranos en todos estos locales</p>
            </router-link>
            <iframe src="https://www.youtube-nocookie.com/embed/OaVsCM0Zeio?modestbranding=1&controls=0&mute=1&autoplay=1&disablekb=1&loop=1&playlist=OaVsCM0Zeio&rel=0&showinfo=0" 
            title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture">
            </iframe>
        </section>
    </main>
</template>

<script>
import {card} from 'ionicons/icons';
import {sync} from 'ionicons/icons';
import {checkmarkCircle} from 'ionicons/icons';
import {helpCircle} from 'ionicons/icons';
import {storefront} from 'ionicons/icons';
import {cube} from 'ionicons/icons';
import {pin} from 'ionicons/icons';
import {searchSharp} from 'ionicons/icons';
import {close} from 'ionicons/icons';


export default {
    data() {
        return {
            //icons
            card,
            sync,
            checkmarkCircle,
            helpCircle,
            storefront,
            cube,
            pin,
            searchSharp,
            close,
            //catalogo
            productosV : [],
            productosU : [],
            yOffsetU: null,
            yOffsetV: null,
            //filter
            searchU: '',
            searchV: '',
        };
    },
    computed: {
        filteredProductosU() {
            return this.productosU.filter((elem) =>
                elem.nombre.toLowerCase().includes(this.searchU.toLowerCase())
            );
        },
        filteredProductosV() {
            return this.productosV.filter((elem) =>
                elem.nombre.toLowerCase().includes(this.searchV.toLowerCase())
            );
        },
    },
    methods:{
        viewUrban(){
            this.yOffsetU = 45;
        },
        viewVestir(){
            this.yOffsetV = 45;
        },
        closeArt(){
            this.yOffsetU = -150;
            this.yOffsetV = -150;
        },
    },
    mounted(){
        fetch('http://127.0.0.1:5000/productos') 
            .then((res) => {
                if (res.ok) {
                    return res.json();
                } else {
                    throw new Error('Error al obtener los datos de los productos');
                }
            })
            .then((data) => {
                this.productosU=data.filter(item => item.tipo === 'Urban');
                this.productosV=data.filter(item => item.tipo === 'Vestir');
            })
            .catch((err) => {
                console.error('Error:', err);
            });
    }
};
</script>

<style scoped>
/* CONTENEDOR IMAGENES */

.inicio{
    width: 100%;
    height: 100vh;
    justify-content: center;
    overflow: hidden;
    filter: drop-shadow(0px 5px 5px rgba(0, 0, 0, 0.5));
    display: flex;
    align-items: center;
    position: relative;
}
.inicio div{
    height: 100%;
    width: 50%;
    overflow: hidden;
    margin: 0 5px;
    cursor: pointer;
    transition: transform 0.3s ease;
}
.gray:hover,
.lightblue:hover{
    transform: scale(1.01);
}
.inicio .gray{
    background-color:  rgba(34,34,34,1);
    border-bottom-left-radius: 10px;
    box-shadow: 2px 0px 5px rgba(0, 0, 0, 0.5);
}
.inicio .lightblue{
    background-color: rgb(196, 205, 211);
    border-bottom-right-radius: 10px;
    box-shadow: -2px 0px 5px rgba(0, 0, 0, 0.5);
}
/* contenedor img urban */
.inicio :nth-child(1){
    justify-content: end;
}
/* contenedor img vestir */
.inicio :nth-child(2){
    justify-content: start;
}
/* img */
.casual, .evento{
    cursor: pointer;
    transition: 0.5s ease;
}
.casual{
    width: 83%;
    height: 100%;
    filter: drop-shadow(10px 1px 2px rgba(0, 0, 0, 0.3));
    position: relative;
    top: 30%;
    left: 40%;
}
.evento{
    width: 55%;
    height: 100%;
    filter: drop-shadow(-10px 1px 2px rgba(0, 0, 0, 0.1));
    position: relative;
    top: 30%;
    left: -10%;
}
.evento:hover{
    filter: drop-shadow(-5px 1px 5px rgba(0, 0, 0, 0.1));
}
.casual:hover{
    filter: drop-shadow(5px 1px 2px rgba(0, 0, 0, 0.1));
}
.names{
    position: absolute;
    display: flex;
}
.name1,
.name2{
    width: 100%;
    font-size: 15em;
    position: relative;
    z-index: 9;
}
.name1{ 
    justify-self: end;
    color: rgb(34,34,34);
    text-align: end;
    text-shadow: -2px -2px 0 #DDE6ED, 2px -2px 0 #DDE6ED, -2px 2px 0 #DDE6ED, 2px 2px 0 #DDE6ED;
}
.name2{
    justify-self: start;
    color: #27374D;
    text-shadow: -2px -2px 0 #27374D, 2px -2px 0 #27374D, -2px 2px 0 #27374D, 2px 2px 0 #27374D;
    text-shadow: 0px 5px 5px black;
    text-align: start;
}


/* gird catalogo */
.catalogo h2{
    text-align: center;
    margin-top: 5%;
    font-size: 3em;
}
.grid-container{
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: repeat(4, 1fr); 
    grid-template-rows: 400px 400px; 
    justify-content: center;
    margin-top: 2%;
    /* background-color: #27374D; */
}
.grid-item figure{
    width: 100%;
    height: 100%;
    cursor: pointer;
}
.grid-item img{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: 0.3s;
    filter: opacity(0.7) brightness(.7);
}
.grid-item img:hover{
    border: 1px solid #27374D;
    filter: opacity(2) brightness(1);
}




/* pagos */
.container-pagos{
    width: 100%;
    height: 300px;
    margin-top: 5%;
    display: flex;
    justify-content:center;
    align-items: center;
}
.tres-cuotas, .seis-cuotas{
    display: flex;
    align-items: end;
    color: #27374D;
}
.tres-cuotas :nth-child(1),
.seis-cuotas :nth-child(1){
    font-size: 6em;
    font-weight: 600;
    font-family: sans-serif;
}
.tres-cuotas :nth-child(2),
.seis-cuotas :nth-child(2){
    font-size: 1.5em;
    font-weight: 600;
    margin: 0 0 5% 20%;
}
.container-pagos span{
    height: 25%;
    width: 5px;
    background-color: #27374D;
    margin: 0 15%;
}




/* info */
.info{
    width: 50%;
    margin: 5% auto 0 auto;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: 100px 100px;
    text-align: center;
    grid-row-gap: 10%;
    color: #27374D;
}
.store,
.card{
    border-left: 2px solid #27374D;
    border-right: 2px solid #27374D;
}
.info div a{
    text-decoration: none;
    color: #27374D;
}
.info div ion-icon{
    font-size: 3em;
    margin-bottom: 10px;
}
.info div h4{
    font-size: 1.2em;
}
.info div p{
    margin-bottom: 5em;
}




/* info extra locales */
.extra{
    background-color: #27374D;
    width: 46vw;
    height: 50px;
    margin: 2% auto 7% auto;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #ffffff;
    font-size: 1.1em;
    letter-spacing: 2px;
    text-decoration: none;
    border-radius: 3px;
}
.extra ion-icon{
    font-size: 2em;
    margin-right: 10px;
}



/* video */
iframe{
    width: 100%;
    height: 100vh;
    margin-top: 6%;
}




.ventana {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    backdrop-filter: blur(25px);
    padding: 20px;
    box-shadow: 0px 20px 50px rgba(0,0,0,0.5);
    border-top: 1px solid rgba(255,255,255,0.3);
    border-left: 1px solid rgba(255,255,255,0.1);
    border-radius: 2px;
    width: 80%;
    max-height: 80vh;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    transition: .5s ease;
    z-index: 99;
}

.cruz {
    position: absolute;
    top: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    font-size: 3em;
    cursor: pointer;
    z-index: 99;
}
.cruz ion-icon{
    filter: drop-shadow(0px 3px 3px rgba(0,0,0,0.5));
}

.enlaces h2{
    text-align: center;
    color: #fff;
    font-size: 2.3em;
    margin-top: 2%;
    letter-spacing: 2px;
    text-shadow: 0px 2px 5px rgba(0, 0, 0, 0.5);
}
.enlaces p{
    color: #fff;
    text-align: center;
    letter-spacing: 2px;
    margin-top: 10px;
    text-shadow: 0px 2px 5px rgba(0, 0, 0, 0.5)
}
.enlaces p a{
    text-decoration: underline;
    color: #fff;
}
.order-search{
    margin: 40px 0;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}
.search {
    width: 100%;
    display: flex;
    border-radius: 5px;
    padding: 3px;
}

.search ion-icon {
    font-size: 1.5em;
    color: #27374D;
    margin: 5px 5px 0 0;
}

.search input{
    border: none;
    border-top: 1px solid #fff;
    background-color: transparent;
    width: 30%;
    padding: 6px;
    font-size: 1em;
    font-weight: 600;
    color:#27374D;
    outline: none;
    transition: .2s;
    border-radius: 5px;
    box-shadow: 0px 2px 3px rgba(0,0,0,0.5);
}

.search input:focus{
    box-shadow: none;
    border: none;
    border-bottom: 1px solid #fff;
    box-shadow:inset 0px 2px 3px rgba(0,0,0,0.5);
}

.ventana .articulos {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2%;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  text-shadow: 0 0 5px rgba(0, 0, 0, 0.5);

}

.ventana .articulos div:not(.detail){
    width: 300px;
    height: 400px;
    background: rgba(255, 255, 255, 0.2);
    box-shadow: 0px 20px 50px rgba(0,0,0,0.5);
    border-top: 1px solid rgba(255,255,255,0.3);
    border-radius: 2px;
    backdrop-filter: blur(5px); 
}

.ventana img {
    width: 100%;
    height: 70%;
    object-fit: cover;
    border-top: 1px solid rgba(255,255,255,0.3) 
}

.ventana h4,
.ventana p {
    text-align: center;
    margin-top: 1px;
    padding: 0 2px; 
}



.detail {
    width:70%;
    border-radius: 3px;
    background-color: #27374D ;
    border: none;
    padding: 7px;
    cursor: pointer;
    letter-spacing: 2px;
    transition: .3s;
    position: relative;
    top: 8%;
    left: 50%;
    transform: translateX(-50%);
    text-align: center;
}
.detail a{
    text-decoration: none;
    color: #fff;
    background-color: #27374D;
    padding: 5px 40px;
    transition: .3s;
}
.detail:hover,
.detail:hover > a {
    background-color: #192331;
}



.urban-catalogo{
    top: -150%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: rgba(34, 34, 34, 0.3);
}

.vestir-catalogo{
    top: -150%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: rgba(221, 230, 237, 0.6);
}

@media (max-width:768px){
    .main{
        overflow: hidden;
    }
    .name1,
    .name2{
        font-size: 4em;
        margin-top: 100%;
    }
    .casual{
        width: 100%;
        filter: drop-shadow(10px 1px 2px rgba(0, 0, 0, 0.3));
        position: relative;
        top: 30%;
        left: 20%;
        object-fit: cover;
    }
    .evento{
        width: 100%;
        filter: drop-shadow(-10px 1px 2px rgba(0, 0, 0, 0.1));
        position: relative;
        top: 30%;
        left: 0%;
        object-fit: cover;
    }
    .catalogo h2{
        margin-top: 15%;
    }
    .grid-container{
        grid-template-rows: 200px 200px;
        gap: 1%;
    }
    .grid-item{
        border: 2px solid #DDE6ED;
    }
    .grid-item img{
        filter: opacity(1) brightness(1);
    }
    .tres-cuotas{
        border-right: 2px solid #192331;
    }
    .tres-cuotas,
    .seis-cuotas{
        width: 100%;
        align-items: center;
        justify-content: center;
        padding: 15px;
    }
    .tres-cuotas :nth-child(1),
    .seis-cuotas :nth-child(1){
        font-size: 5em;
    }
    .tres-cuotas :nth-child(2),
    .seis-cuotas :nth-child(2){
        font-size: 1.2em;
    }
    .container-pagos span{
        display: none;
    }
    .info{
        width: 100%;
        grid-row-gap: 40%;
    }
    .info div{
        padding: 0px 7px;
    }
    .info div ion-icon{
        font-size: 2em;
    }
    .info div h4{
        font-size: 1em;
    }
    .info div p{
        margin-bottom: 4em;
    }
    .extra{
        width: 95%;
        margin: 45% auto;
        font-size: 1em;
        letter-spacing: 1px;
    }
    .extra ion-icon{
        font-size: 1.5em;
        margin-right: 5px;
    }
    iframe{
        height: 50vh;
    }

    .ventana{
        width: 90%;
        height: 100%;
        transform: translate(-50%, -40%);
        overflow-x: hidden;
        max-height: 75vh
    }
    .cruz{
        font-size: 2em;
    }
    .enlaces h2{
        font-size: 2em;
        margin-top: 5%;
        letter-spacing: 1px;
    }
    .enlaces p{
        letter-spacing: 1px;
        margin-top: 5%;
    }
    .enlaces p a{
        margin-right: 1%;
    }
    .search {
        width: 100%;
    }
    .search input{
        width: 50%;
    }
    .ventana .articulos {
        width: 100%;
        display: grid;
        grid-template-columns: repeat(2, 140px);
        grid-template-rows: repeat(auto-fill, 350px);
        gap: 7% 3%;
        align-items: center;
        justify-content: center;
        margin: 0;
    }
    .ventana .articulos div:not(.detail){
        width: 140px;
        height: 350px;
    }
    .detail {
        width:90%;
        padding: 5px 0;
        letter-spacing: 0px;
        position: absolute;
        top: 90%;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
    }
    .detail a{
        padding: 5px 45px;
    }
}

@media (min-width:515px) and (max-width:768px){
    .extra{    
        margin: 25% auto;
    }
    .ventana{
        padding: 5px;
    }
    .order-search{
        justify-content: start;
    }
    .search{
        width: 70%;
        margin-left: 5%;
    }
    .ventana .articulos {
        width: 100%;
        grid-template-columns: repeat(3, 140px);
        gap: 7% 4%;
    }
}

@media (min-width: 769px) and (max-width: 1000px){
    .name1,
    .name2{
        font-size: 8em;
    }
    .casual{
        width: 100%;
        filter: drop-shadow(10px 1px 2px rgba(0, 0, 0, 0.3));
        position: relative;
        top: 30%;
        left: 20%;
        object-fit: cover;
    }
    .evento{
        width: 100%;
        filter: drop-shadow(-10px 1px 2px rgba(0, 0, 0, 0.1));
        position: relative;
        top: 30%;
        left: 0%;
        object-fit: cover;
    }
    .catalogo h2{
        margin-top: 15%;
    }
    .grid-item img{
        filter: opacity(1) brightness(1);
    }
    .tres-cuotas,
    .seis-cuotas{
        width: 100%;
        align-items: center;
        justify-content: center;
        padding: 0 15px;
        
    }
    .container-pagos span{
        margin: 0 ;
    }
    .tres-cuotas :nth-child(1),
    .seis-cuotas :nth-child(1){
        font-size: 5em;
        font-weight: 600;
    }
    .tres-cuotas :nth-child(2),
    .seis-cuotas :nth-child(2){
        font-size: 1.4em;
        font-weight: 600;
        margin: 0 3%;
    }
    .info{
        width: 95%;
        grid-row-gap: 15%;
    }
    .extra{
        width: 90%;
        margin: 10% auto 7% auto;
    }
    .ventana{
        width: 90%;
        height: 100%;
        transform: translate(-50%, -40%);
        overflow-x: hidden;
    }
    .ventana .articulos {
        width: 100%;
        grid-template-columns: repeat(4, 150px);
    }
    .ventana .articulos div:not(.detail){
        width: 150px;
        height: 350px;
    }
    .detail {
        width:90%;
        padding: 5px 0;
        letter-spacing: 0px;
        position: absolute;
        top: 90%;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
    }
    .detail a{
        padding: 5px 45px;
    }
}

@media (min-width: 1001px) and (max-width: 1650px){
    .name1,
    .name2{
        font-size: 11em;
    }
    .casual{
        width: 100%;
        filter: drop-shadow(10px 1px 2px rgba(0, 0, 0, 0.3));
        position: relative;
        top: 30%;
        left: 28%;
        object-fit: cover;
    }
    .evento{
        width: 90%;
        filter: drop-shadow(-10px 1px 2px rgba(0, 0, 0, 0.1));
        position: relative;
        top: 30%;
        left: -25%;
    }
    .info{
        width: 70%;
        grid-row-gap: 17%;
    }
    .extra{
        margin: 5% auto 7% auto;
    }
    .ventana{
        width: 90%;
        height: 100%;
        transform: translate(-50%, -40%);
        overflow-x: hidden;
    }
    .ventana .articulos {
        width: 100%;
        grid-template-columns: repeat(2, 300px);
        gap: 10% 3%;
    }
    .ventana .articulos div:not(.detail){
        width: 300px;
        height: 400px;
    }
    .detail {
        width:90%;
        padding: 5px 0;
        letter-spacing: 0px;
        position: absolute;
        top: 90%;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
    }
    .detail a{
        padding: 5px 45px;
    }
}

</style>
