<template>
    <div class="wrapper-check">
        <div class="container-direc">
            <h3>Detalles de facturación</h3>
                <form class="form-direc" v-if="userEmail">
                    <div v-for="elem in dataUser" :key="elem.email">
                        <label for="dni">DNI</label><input type="number" name="dni" required v-model="elem.dni">
                        <label for="nombre">Nombre</label><input type="text" name="nombre" required v-model="elem.nombre">
                        <label for="apellido">Apellido</label><input type="text" name="apellido" required v-model="elem.apellido">
                        <label for="celular">Telefono</label><input type="tel" name="celular" required v-model="elem.cel">
                    </div>
                    <div v-for="elem in dataDirec" :key="elem.email">
                        <label for="direccion">Direccion de la calle</label><input name="direccion" type="text" required v-model="elem.calle">
                        <label for="localidad">Localidad/Ciudad</label><input name="localidad" type="text" required v-model="elem.localidad">
                        <label for="provincia">Región/Provincia</label><input name="provincia" required v-model="elem.provincia">
                        <label for="postal">Codigo Postal</label><input type="number" name="postal" required v-model="elem.codigo_postal">
                        <label for="email">Email</label><input type="email" name="email" required v-model="userEmail">
                        <label for="nota">Notas del pedido (Opcional)</label><textarea name="nota" cols="20" rows="3" v-model="elem.datos_extra"></textarea>
                    </div>
                </form>
                <form class="form-direc" v-else>
                    <label for="dni">DNI</label><input type="number" name="dni" required v-model="newDni">
                    <label for="nombre">Nombre</label><input type="text" name="nombre" required v-model="newNombre">
                    <label for="apellido">Apellido</label><input type="text" name="apellido" required v-model="newApellido">
                    <label for="celular">Telefono</label><input type="tel" name="celular" required v-model="newCel">
                    <label for="direccion">Direccion de la calle</label><input name="direccion" type="text" required v-model="newDirec">
                    <label for="localidad">Localidad/Ciudad</label><input name="localidad" type="text" required v-model="newLocalidad">
                    <label for="provincia">Región/Provincia</label><input name="provincia" required v-model="newProvincia">
                    <label for="postal">Codigo Postal</label><input type="number" name="postal" required v-model="newCP">
                    <label for="email">Email</label><input type="email" name="email" required v-model="newEmail">
                    <label for="nota">Notas del pedido (Opcional)</label><textarea name="nota" cols="20" rows="3" v-model="newNota"></textarea>
                </form>
        </div>
        <span class="barra"></span>
        <div class="container-resume">
            <h3>Tu pedido</h3>
            <div class="info-pedido">
                <h3>Productos</h3>
                <h4 class="name-product" v-for="(productoEnCarrito, index) in carrito" :key="index">{{ productoEnCarrito.producto.nombre }}</h4>
                <div class="cost-subtotal">
                    <h3>Subtotal</h3>
                    <h4>${{ TotalPrecio }}</h4>
                </div>
                <div class="cost-envio">
                    <h3>Envío</h3>
                    <h4>$1000</h4>
                </div>
                <div class="cost-total">
                    <h3>Total</h3>
                    <h4>${{ TotalConEnvio }}</h4>
                </div>
            </div>
            <div class="info-pagos">
                <div class="ayuda-pagos">
                    <figure>
                        <img src="../assets/img/icons/blue-wallet.png" alt="Icono billetera">
                    </figure>
                    <div>
                        <h5>PAGA RÁPIDO</h5>
                        <h6>USA TU DINERO DISPONIBLE O TARJETAS GUARDADAS</h6>
                    </div>
                </div>
                <div class="ayuda-pagos">
                    <figure>
                        <img src="../assets/img/icons/blue-phone-installments.png" alt="Icono cuotas">
                    </figure>
                    <div>
                        <h5>ACCEDE A CUOTAS</h5>
                        <h6>PAGA CON O SIN TARJETA DE CRÉDITO.</h6>
                    </div>
                </div>
                <div class="ayuda-pagos">
                    <figure>
                        <img src="../assets/img/icons/blue-protection.png" alt="icono seguridad">
                    </figure>
                    <div>
                        <h5>COMPRA CON CONFIANZA</h5>
                        <h6>RECIBE AYUDA SI TIENES ALGÚN PROBLEMA CON TU COMPRA.</h6>
                    </div>
                </div>
                <div class="check">
                    <ion-icon :src="bagCheckSharp"></ion-icon>
                    <h5>Te llevaremos a Mercado Pago para completar tu compra de forma segura.</h5>
                </div>
                <div class="finish-check">
                    <h5>AL CONTINUAR, ACEPTAS NUESTROS TÉRMINOS Y CONDICIONES</h5>
                    <button @click="endCheckout">Realizar el pedido</button>
                </div>
            </div>
        </div>
    </div>

    <transition>
        <div class="wrapper-confirm" v-show="confirm">
            <span class="close">
                <ion-icon :src="close" @click="this.confirm=false"></ion-icon>
            </span>
            <div class="container">
                <div class="tus-datos">
                    <div class="title-confirm">
                        <h3>Tus Datos</h3>
                    </div>
                    <div class="data-confirm" v-for="elem in userShop" :key="elem">
                        <p>DNI: {{ elem.dni }} </p>
                        <p>NOMBRE: {{ elem.nombre }}</p>
                        <p>APELLIDO: {{ elem.apellido }}</p>
                        <p>TELÉFONO: {{ elem.telefono }}</p>
                        <p>DIRECCIÓN: {{ elem.direccion }}</p>
                        <p>LOCALIDAD: {{ elem.localidad }}</p>
                        <p>PROVINCIA: {{ elem.provincia }}</p>
                        <p>CODIGO POSTAL: {{ elem.cp }}</p>
                        <p>EMAIL: {{ elem.email }}</p>
                        <p>NOTA EXTRA:{{ elem.nota }}</p>
                    </div>
                </div>
                <div class="tu-pedido">
                    <div class="title-confirm">
                        <h3>Tu Pedido</h3>
                    </div>
                    <div class="data-confirm">
                        <p>ARTÍCULO:</p>
                        <p v-for="(productoEnCarrito, index) in carrito" :key="index">-{{ productoEnCarrito.producto.nombre }}</p>
                        <p>ENVÍO: $1000</p>
                        <p>TOTAL: ${{ TotalConEnvio }}</p>
                    </div>
                    <div class="btn-confirm">
                        <button class="" @click="nuevoPedido" :class="{confirm:isOkPurchase}">{{ btnConfirm }}</button>
                    </div>
                </div>
            </div>
        </div>
    </transition>
</template>
<script>
import { bagCheckSharp, ticket, close } from 'ionicons/icons'
import { mapState } from 'vuex';

export default{
    data(){
        return{
            //icon
            bagCheckSharp,
            close,
            //datos del usuario registrad
            dataUser: [],
            dataDirec: [],
            user:[],
            //datos del usuario No registrado
            newDni: null,
            newNombre: null,
            newApellido: null,
            newCel: null,
            newDirec: null,
            newLocalidad: null,
            newProvincia: null,
            newCP: null,
            newEmail: null,
            newNota: null,
            //confirmacion de compra
            confirm: false,
            isOkPurchase: false,
            btnConfirm: 'Confirmar compra',
            //datos facturacion
            userShop: [],
            newPedido: [],
            //productos
            product: [],
            idProduct: null,
            upStock: null,
            upSotckTalle: null,
            numCompra: null,
        }
    },
    computed:{
        carrito(){
            return this.$store.state.carrito;
        },
        TotalPrecio(){
            return this.carrito.reduce((total, productoEnCarrito) => {
                return total + productoEnCarrito.producto.precio;
            }, 0)
        },
        TotalConEnvio(){
            return this.TotalPrecio + 1000
        },
        TotalStock(){
            return this.carrito.reduce((total, productoEnCarrito) => {
                return total + productoEnCarrito.cantidad;
            }, 0)
        },
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
    methods:{
        scrollToTop(){
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            })
        },
        nuevoPedido(){
            this.newPedido = this.carrito.map((item, index) => ({
                dni: this.userShop[index].dni,
                productos: item.producto.nombre,
                importe: this.TotalConEnvio,
            }));

            const url = 'http://127.0.0.1:5000/pedido';
            const options = {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(this.newPedido)
            }
            fetch(url, options)
            .then(res=>{
                if(res.ok){
                    this.isOkPurchase = true;
                    this.btnConfirm = 'Gracias por tu compra!';
                    this.reducirStock();
                    return res.json();
                }else{
                    throw new Error('Error en la solicitud')
                }
            })
            .then(data => {
                this.numCompra = data.numeroPedido;
                let mail = {
                    dni: this.userShop[0].dni,
                    nombre: this.userShop[0].nombre,
                    apellido: this.userShop[0].apellido,
                    telefono: this.userShop[0].telefono,
                    direccion: this.userShop[0].direccion,
                    localidad: this.userShop[0].localidad,
                    provincia: this.userShop[0].provincia,
                    cp: this.userShop[0].cp,
                    email: this.userShop[0].email,
                    nota: this.userShop[0].nota,
                    articulo: this.newPedido[0].productos,
                    total: this.TotalConEnvio,
                    numCompra: this.numCompra
                }
                let urlMail="http://localhost:5000/purchase"
                    var optionsMail={
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify(mail)
                    }
                fetch(urlMail, optionsMail)
                    .then(res => {
                        if (res.ok) {
                            res.json()
                        } else {
                            throw new Error('Error en la solicitud.');
                        }
                    })
                    .catch(err => {
                        console.error('Error en la solicitud:', err);
                    });
            })
            .catch(err=>{
                console.error('Error en la solicitud:', err);
            })
        },
        stockTalle(){
            const talle = this.carrito.map( elem => elem.talle);
            const Producto = this.product[0]
            const elemsProducto = Object.entries(Producto) //propiedades y valores a formato iterable

            elemsProducto.forEach(elem=>{
                if(elem[0] == talle){
                    this.upSotckTalle = elem[1] - this.TotalStock;
                }
            })

            this.actualizarStock();
        },
        reducirStock(){
            const ProductCarrito = this.carrito.map( elem => elem.producto.nombre);
        
            fetch('http://127.0.0.1:5000/productos') 
                .then((res) => {
                    if (res.ok) {
                        return res.json();
                    } else {
                        throw new Error('Error al obtener los datos de los productos');
                    }
                })
                .then((data) => {
                    this.product=data.filter(elem => elem.nombre == ProductCarrito);
                    this.idProduct=this.product[0].id;
                    this.upStock=this.product[0].stock - this.TotalStock;
                    this.stockTalle();
                })
                .catch((err) => {
                    console.error('Error:', err);
                });
        },
        actualizarStock(){
            const talle = this.carrito.map( elem => elem.talle);

            const objProduct = {
                talle : talle[0],
                stockTalle : this.upSotckTalle,
                stock : this.upStock,
            }

            const url = `http://127.0.0.1:5000/stock/${this.idProduct}`
            const options = {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(objProduct)
            }

            fetch(url, options)
                .then(res => {
                    if(res.ok){
                        return res.json()
                    }
                })
                .catch(err => {
                    console.error(err)
                })
        },
        endCheckout(){
            if(this.userEmail){
                this.userShop = this.dataUser.map((item, index)=> ({
                    dni: item.dni,
                    nombre: item.nombre,
                    apellido: item.apellido,
                    telefono: item.cel,
                    direccion: this.dataDirec[index].calle,
                    localidad: this.dataDirec[index].localidad,
                    provincia: this.dataDirec[index].provincia,
                    cp: this.dataDirec[index].codigo_postal,
                    email: this.userEmail,
                    nota: this.dataDirec[index].datos_extra
                })) 
                this.confirm = true;
            }else{
                this.userShop = [{
                    dni: this.newDni,
                    nombre: this.newNombre,
                    apellido: this.newApellido,
                    telefono: this.newCel,
                    direccion: this.newDirec,
                    localidad: this.newLocalidad,
                    provincia: this.newProvincia,
                    cp: this.newCP,
                    email: this.newEmail,
                    nota: this.newNota
                }];
                this.confirm = true;
            }
            this.scrollToTop();
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
    },
    mounted(){
        this.fetchData();
        this.fetchUser();
    }
}
</script>


<style scoped>
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

.wrapper-confirm,
.container,
.tus-datos,
.tu-pedido{
    display: flex;
    justify-content: center;
    align-items: center;
}
.wrapper-confirm{
    width: 80%;
    height: 70vh;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: transparent;
    border-radius: 2px;
    backdrop-filter: blur(25px);
    box-shadow: 0 0 30px rgba(0, 0, 0, .5); 
}
.container{
    width: 90%;
    height: 90%;
    background-color: #fff;
}
.tus-datos{
    width: 45%;
    height: 90%;
    flex-direction: column;
}
.tu-pedido{
    width: 45%;
    height: 90%;
    flex-direction: column;
}
.title-confirm{
    width: 100%;
    text-align: center;
    font-size: 2em;
    color: #27374D;
    letter-spacing: 2px;
    margin-bottom: 20px;
}
.data-confirm{
    color: #27374D;
    letter-spacing: 1px;
}
.data-confirm p{
    margin: 15px 0;
    font-weight: 500;
    font-size: 1.1em;
}
.btn-confirm{
    width: 70%;
}
.btn-confirm button{
    width: 100%;
    height: 40px;
    margin-top: 30px;
    border: none;
    border-radius: 3px;
    background-color: #27374D;
    color: #fff;
    font-size: 1em;
    font-weight: 600;
    letter-spacing: 3px;
    cursor: pointer;
    transition: background-color 0.5s ease;
}

.wrapper-check{
    width: 100%;
    height: 100vh;
    display: grid;
    grid-template-columns: 45% 10% 45%;
    margin-top: 5%;
}
.container-direc,
.container-resume{
    margin: auto;
    width: 70%
}
.container-direc h3,
.container-resume > h3{
    font-size: 2em;
    color: #27374D;
    text-align: center;
    letter-spacing: 2px;
    margin-bottom: 20px;
}
.form-direc{
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.form-direc label{
    font-size: 1em;
    color: #27374D;
    font-weight: 600;
    letter-spacing: 2px;
}
.form-direc input{
    width: 100%;
    height: 30px;
    border: none;
    padding: 10px;
    color: #27374D;
    font-weight: 600;
    letter-spacing: 1px;
    margin-bottom: 30px;
}
.form-direc select,
.form-direc textarea{
    border: none;
    height: 30px;
    color: #27374D;
    font-weight: 600;
    letter-spacing: 1px;
    padding: 10px;
}
.form-direc textarea{
    width: 100%;
    height: 100px;
    resize: none;
}
.form-direc input:focus,
.form-direc select:focus,
.form-direc textarea:focus{
    background-color: #27374D;
    color: #fff;
    border: none;
    outline: none;
}


.barra{
    width: 3px;
    height: 100%;
    background-color: #27374D;
    margin: auto;
}



.container-resume{
    display: flex;
    flex-direction: column;
}
.info-pedido div{
    display: flex;
    justify-content: space-between;
    margin: 30px 0 30px;
}
.name-product{
    text-align: end;
}
.cost-total{
    border-top: 2px solid #27374D;
    padding-top: 30px;
}


.info-pagos{
    text-align: center;
}

.ayuda-pagos{
    height: 50px;
    display: flex;
    margin-top: 30px;
}
.ayuda-pagos figure{
    object-fit: cover;
}
.ayuda-pagos figure img{
    height: 100%;
}
.ayuda-pagos div{
    height: 50px;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: start;
    margin-left: 10px;
    color: #27374D;
}
.ayuda-pagos div h5{
    font-size: .9em;
    letter-spacing: 2px;
}
.ayuda-pagos div h6{
    color: rgba(0, 0, 0, 0.6);
    letter-spacing: 1px;
}

.check{
    display: flex;
    justify-content: center;
    align-items: center;
    color: #27374D;
}
.check ion-icon{
    width: 20px;
    height: 20px;
}
.check h5{
    font-size: .9em;
    margin: 30px 0 30px 5px;
}

.finish-check h5{
    font-size: .9em;
    color: #27374D;
    letter-spacing: 1px;
}

.finish-check button{
    width: 100%;
    height: 40px;
    margin-top: 30px;
    border: none;
    border-radius: 3px;
    background-color: #27374D;
    color: #fff;
    font-size: 1em;
    font-weight: 600;
    letter-spacing: 3px;
    cursor: pointer;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.3s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

.btn-confirm button.confirm{
    background-color: green;
    cursor: not-allowed;
}

@media (max-width: 1000px){
    .wrapper-check{
        height: 100%;
        display: flex;
        flex-direction: column;
        margin-top: 20%;
    }
    .container-direc{
        width: 90%;
        margin-bottom: 15%;
    }
    .form-direc label{
        font-size: 1.2em;
    }
    .form-direc input{
        font-size: 1em;
    }
    .barra{
        display: none;
    }
    .container-resume{
        width: 90%;
    }
    .info-pedido div h4{
        font-size: 1.2em;
    }
    .ayuda-pagos div h5{
        font-size: 1em;
    }
    .ayuda-pagos div h6{
        text-align: start;
        font-size: .7em;
    }
    .check ion-icon{
        width: 40px;
        height: 40px;
    }
    .check h5{
        text-align: start;
        margin-left: 5%;
    }
    .finish-check h5{
        margin-top: 5%;
        font-weight: 800;
    }
    .finish-check button{
        margin-bottom: 15%;
        font-size: 1.1em;
    }
    .wrapper-confirm{
        width: 90%;
        height: auto;
        top: 100%;
        padding: 5% 0;
    }
    .container{
        flex-direction: column;
        padding: 5% 0;
    }
    .tus-datos{
        width: 90%;
    }
    .tu-pedido{
        width: 90%;
        margin-top: 10%;
    }
    .data-confirm{
        width: 90%;
    }
    .btn-confirm{
        width: 100%;
    }
}
</style>