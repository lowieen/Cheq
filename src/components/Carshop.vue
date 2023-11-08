<template>
    <div class="data-shop" :class="{ active: showCarshop }">
        <h2>Carrito</h2>
        <p>Productos agregados</p>
        <span class="close">
            <ion-icon :src="close" @click="closed"></ion-icon>
        </span>
        <div class="container-shop">
            <div class="productos-shop">
                <div class="unidad-shop" v-for="(productoEnCarrito, index) in carrito" :key="index">
                    <span class="delete-art">
                        <ion-icon :src="trashOutline" @click="deletedProduct(index)"></ion-icon>
                    </span>
                    <figure>
                        <img :src=productoEnCarrito.producto.url_Image alt="Producto">
                    </figure>
                    <div class="descripcion-shop">
                        <h5 style="text-decoration: underline;">{{ productoEnCarrito.producto.nombre }}</h5>
                        <h5>Precio: ${{ productoEnCarrito.producto.precio }}</h5>
                        <h5>Cantidad: {{ productoEnCarrito.cantidad }}</h5>
                        <h5>Talle: {{ productoEnCarrito.talle }}</h5>
                    </div>
                </div>
            </div>
            <div class="totales">
                <h6>Total prendas: {{ TotalPrendas }}</h6>
                <h6>Total precio: ${{ TotalPrecio }}</h6>
            </div>
            <div class="finalizar">
                <router-link :to="{ name: 'checkout' }" class="btn" @click="closed">Continuar</router-link>
            </div>
        </div>
    </div>
</template>
<script>
import { close, trashOutline } from 'ionicons/icons'

export default{
    props:{
        showCarshop: Boolean,
    },
    data(){
        return{
            close,
            trashOutline,
        }
    },
    methods:{
        deletedProduct(index){
            this.carrito.splice(index, 1);
        },
        closed(){
            this.$emit('close-carshop');
        }
    },
    computed:{
        carrito(){
            return this.$store.state.carrito;
        },
        TotalPrendas(){
            return this.carrito.reduce((total, productoEnCarrito) => {
                return total + productoEnCarrito.cantidad;
            }, 0);
        },
        TotalPrecio(){
            return this.carrito.reduce((total, productoEnCarrito) => {
                return total + productoEnCarrito.producto.precio;
            }, 0)
        }
    },
}
</script>

<style scoped>
.data-shop{
    max-height: 80%;
    overflow-y: auto;
    position:fixed;
    left: 0;
    backdrop-filter: blur(25px);
    box-shadow: 0px 20px 50px rgba(0,0,0,0.5);
    border-radius: 2px;
    color: #ffffff;
    z-index: 99;
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transition: opacity .5s, transform .5s, visibility 0.5s ease;
    text-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);
}
.data-shop h2{
    margin-top: 35px;
}
.data-shop h2,
.data-shop p{
    text-align: center;
}
.container-shop{
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-direction: column;
    padding: 30px;
}
.productos-shop{
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
}
.unidad-shop{
    display: flex;
    margin: 15px 0;
    position: relative;
}
.delete-art{
    position: absolute;
    bottom: 90%;
    left: 100%;
    width: 20px;
    height: 20px;
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
.productos-shop figure{
    width: 75px;
    height: 75px;
}
.productos-shop figure img{
    object-fit: cover;
    width: 75px;
    height: 75px;
}
.descripcion-shop h5,
.totales h6{
    margin: 10px 20px;
    font-size: 0.8em;
    font-weight: 600;
    letter-spacing: 2px;
}
.totales{
    border-top: 2px solid #ffffff;
    padding: 30px;
}
.finalizar{
    width: 100%;
    display: flex;
}
.finalizar .btn{
    width: 100%;
    background: #27374D;
    border: none;
    outline: none;
    border-radius: 3px;
    cursor: pointer;
    font-size: 1em;
    color: #fff;
    font-weight: 400;
    transition: .3s;
    text-align: center;
    text-decoration: none;
    padding: 6px 0;
    letter-spacing: 2px;
}
.close{
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
.active{
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
}

@media (max-width: 768px){
    .data-shop{
        top: 80px;
        width: 100%;
        font-size: 1.2em;
    }
}
</style>