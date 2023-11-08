<template>
    <div class="wrapper">
        <div class="title">
            <h3>{{ title }}</h3>
        </div>
        <div>
            <div class="enlaces">
                <h2>Colección invierno</h2>
                <p>Visita tambien nuestros
                    <router-link :to="{ name: 'buzos'}" >
                            <span>buzos,</span>
                    </router-link>
                    <router-link :to="{ name: 'camperas'}" >
                            <span>camperas, </span>
                    </router-link>
                    <router-link :to="{ name: 'remeras'}" >
                            <span>remeras, </span>
                    </router-link>
                    <router-link :to="{ name: 'pantalones'}" >
                            <span>pantalones, </span>
                    </router-link>
                        o
                    <router-link :to="{ name: 'camisas'}" >
                            <span>camisas.</span>
                    </router-link>
                </p>
            </div>
        </div>
        <div class="container">
            <div class="container-product">
                <div class="filter">
                    <div class="container-li">
                        <h4>Ver :</h4>
                        <ul>
                            <li @click="view = 'urban'">Urban</li>
                            <li @click="view = 'vestir'">Vestir</li>
                            <li @click="view = 'stock'">Con Stock</li>
                            <li @click="view = 'all'">Todo</li>
                        </ul>
                    </div>
                </div>
                <div class="grid">
                    <div class="container-grid">
                        <div class="product" v-for='product in products' :key='product.id'>
                            <div>
                                <img :src="product.url_Image" alt="Articulo">
                                <h4>{{product.nombre}}</h4>
                                <p>${{product.precio}}</p>
                                <div class="detail">
                                    <router-link :to="{ name: 'product-detail', params: { id: product.id } }">
                                    Ver detalles
                                    </router-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </template>
  
<script>
  export default {
    props: {
      fetchUrl: String,
      title: String,
    },
    data() {
      return {
        //productos
        products: [],
        all: [],
        camperas: [],
        buzos: [],
        camisas: [],
        pantalones: [],
        remeras: [],
        //filter
        urban: [],
        vestir: [],
        stock: [],
        //condition
        view : 'stock',
        viewRoutes: null,
      };
    },
    mounted() {
      this.fetchProducts();
    },
    computed:{
        filteredProducts() {
            if (this.view === 'vestir') {
                return this.vestir;

            } else if (this.view === 'urban') {
                return this.urban;

            } else if (this.view === 'stock') {
                return this.stock;
                
            } else {
                return this.all;
            }
        }
    },
    watch: {
        filteredProducts: {
            handler(filtered) {
                this.products = filtered;
            },
            immediate: true
        }
    },
    methods: {
        fetchProducts() {
            fetch('http://127.0.0.1:5000/productos') 
                .then((res) => {
                    if (res.ok) {
                        return res.json();
                    } else {
                        throw new Error('Error al obtener los datos de los productos');
                    }
                })
                .then((data) => {
                    if(this.title == 'Camperas'){
                        this.products=data.filter(elem=>elem.nombre.startsWith('Campera'));
                    }else if(this.title == 'Buzos'){
                        this.products=data.filter(elem=>elem.nombre.startsWith('Buzo'))
                    }else if(this.title == 'Remeras'){
                        this.products=data.filter(elem=>elem.nombre.startsWith('Remera'))
                    }else if(this.title == 'Pantalones'){
                        this.products=data.filter(elem=>elem.nombre.startsWith('Pantalon'))
                    }else{
                        this.products=data.filter(elem=>elem.nombre.startsWith('Camisa'))
                    }
                    this.urban=this.products.filter(item => item.tipo == 'Urban');
                    this.vestir=this.products.filter(item => item.tipo == 'Vestir');
                    this.stock=this.products.filter(item => item.stock >= 1);
                    this.all=this.products;
                })  
                .catch((err) => {
                    console.error('Error:', err);
                });
        },
    }
  };
  </script>
  
  <style scoped>
.wrapper{
    width: 100%;
}
.title{
    width: 100%;
    text-align: center;
    margin-top: 3%;
}
.title h3{
    color: #fff;
    font-size: 2.5em;
    text-shadow: 0px 2px 5px rgba(0, 0, 0, 0.5);
    letter-spacing: 3px;
}
.enlaces h2{
    text-align: center;
    color: #27374D;
    font-size: 1.5em;
    letter-spacing: 2px;
}
.enlaces p{
    color: #27374D;
    text-align: center;
    letter-spacing: 2px;
    margin-top: 10px;
}
.enlaces p a{
    text-decoration: underline;
    color: #fff;
    margin: 0;
    text-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);
}
.container{
    width: 80%;
    height: 100%;
    margin: auto;
    margin-top: 5%;
}
.container-product{
    height: 100%;
    display: grid;
    grid-template-columns: 10% 90%;
}
.filter{
    width: 100%;
    height: 100%;
}
.filter h4{
    letter-spacing: 3px;
}
.container-li li{
    color: #27374D;
    letter-spacing: 2px;
    cursor: pointer;
    margin-top: 20%;
    list-style: none;
}
.container-li li:hover{
    text-decoration: underline;
}
.grid{
    width: 80%;
    height: 100%;
    margin: auto;
    border-radius: 3px;
}
.container-grid{
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: repeat(auto-fill, 200px); 
    gap: 40px;
    grid-template-rows: 400px 400px; 
    justify-content: center;
}
.product{
    width: 200px;
    height: 300px;
    box-shadow: 0 3px 10px black;
    border-radius: 3px;
    overflow: hidden;
}
.product img {
    width: 100%;
    height: 210px;
    object-fit: cover;
    border-top: 1.5px solid #ffffff;
    transition: transform .3s ease;
    position: relative;
}
.product img:hover{
    transform: scale(1.5) translateY(-35px);
}
.product img::after{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 200px;
    height: 210px;
    background: #192331;
}

.product h4,
.product p {
    text-align: center;
    margin: 3px 0;
    padding: 0 2px; 
}



.detail {
    width:90%;
    border-radius: 3px;
    background-color: #27374D ;
    border: none;
    padding: 7px;
    cursor: pointer;
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
    padding: 5px 10px;
    font-size: .9em;
    transition: .3s;
}
.detail:hover,
.detail:hover > a {
    background-color: #192331;
}

@media(max-width: 600px){
    .wrapper{
        height: 100%;
        margin-top: 20%;
    }
    .title{
        margin-bottom: 10%;
    }
    .enlaces h2{
        margin: 5% 0;
    }
    .enlaces p{
        padding: 5px;
    }
    .enlaces p a{
        margin: 2%;
    }
    .container{
        width: 90%;
        margin-top: 15%;
    }
    .container-product{
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .container-li h4{
        letter-spacing: 2px;
        font-size: 1.1em;
    }
    .container-li li{
        letter-spacing: 1px;
        margin: 3%;
        margin-bottom: 10%;
        color: #fff;
        background: #27374D;
        box-shadow: 0 1px 7px black;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 3px 7px;
        border-radius: 3px;
        transition: box-shadow .5s ease;
    }
    .container-li li:hover{
        text-decoration: none;
        box-shadow: none;
    }
    .container-li ul{
        display: flex;
    }
    .grid{
        width: 90%;
    }
    .container-grid{
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 200px 200px;
        gap: 5%;
    }
    .product{
        width: 150px;
        height: 320px;
    }
}

@media (min-width: 600px) and (max-width: 768px) {
    .wrapper{
        height: 100%;
        margin-top: 15%;
    }
    .title{
        margin-bottom: 5%;
    }
    .enlaces h2{
        margin: 2% 0;
    }
    .enlaces p{
        padding: 5px;
    }
    .enlaces p a{
        margin: .5%;
    }
    .container{
        width: 90%;
        margin-top: 15%;
    }
    .container-product{
        width: 100%;
    }
    .container-li h4{
        letter-spacing: 2px;
        font-size: 1.3em;
    }
    .container-li li{
        width: 100%;
        letter-spacing: 1px;
        margin-bottom: 30%;
        color: #fff;
        background: #27374D;
        box-shadow: 0 1px 7px black;
        padding: 5px 3px;
        border-radius: 3px;
        transition: box-shadow .5s ease;
        text-align: center;
    }
    .container-li li:hover{
        text-decoration: none;
        box-shadow: none;
    }
    .grid{
        width: 100%;
        margin-left: 5%;
    }
    .container-grid{
        gap: 0;
    }
    .product{
        width: 150px;
        height: 320px;
    }
}
</style>