<template>
    <header>
        <nav class="barra-nav">
            <a href="#agregar" style="--clr:#526D82;">Agregar</a>
            <a href="#modificar" style="--clr:#9DB2BF;">Modificar</a>
            <a href="#eliminar" style="--clr:#27374D;">Eliminar</a>
        </nav>
    </header>
    <main>
        <section style="--clr:#526D82;" id="agregar">
            <div class="tarjeta nuevo">
                <div class="contenido">
                    <h1>Nuevo</h1>
                    <form class="formulario">
                        <label for="nombre">Nombre</label>
                        <input type="text" name="nombre" v-model="newNombre">
                        <label for="precio">Precio</label>
                        <input type="number" name="precio" v-model="newPrecio">
                        <label for="stock">Stock</label>
                        <input type="number" name="stock" v-model="newStock">
                        <label>Talles:</label>
                        <div class="talles">
                            <div class="t-xs">
                                <span>XS</span>
                                <input type="number" v-model="newXS">
                            </div>
                            <div class="t-s">
                                <span>S</span>
                                <input type="number" v-model="newS">
                            </div>
                            <div class="t-m">
                                <span>M</span>
                                <input type="number" v-model="newM">
                            </div>
                            <div class="t-l">
                                <span>L</span>
                                <input type="number" v-model="newL">
                            </div>
                            <div class="t-xl">
                                <span>XL</span>
                                <input type="number" v-model="newXL"> 
                            </div>
                            <div class="t-xxl">
                                <span>XXL</span>
                                <input type="number" v-model="newXXL">
                            </div>
                        </div>
                        <label>Tipo:</label>
                        <div class="checkboxs">
                            <div>
                                <label for="urban">Urban</label>
                                <input type="radio" value="Urban" name="tipo" v-model="newTipo"> 
                            </div>
                            <div>
                                <label for="vestir">Vestir</label>
                                <input type="radio" value="Vestir" name="tipo" v-model="newTipo">
                            </div>
                        </div>
                        <label for="image">URL Imágen del Producto</label>
                        <input type="text" name="image" v-model="newUrl">
                        <button type="button" @click="agregar" class="boton">Agregar</button>
                    </form>
                </div>
            </div>
        </section>


        <section style="--clr:#9DB2BF;" id="modificar">
            <div class="tarjeta modificar">
                <div class="contenido">
                    <h1>Modificar</h1>
                    <form class="formulario">
                        <label for="identificadorUp">ID</label><input type="number" v-model="upID">
                        <label for="nombre">Nombre</label><input type="text" v-model="upNombre">
                        <label for="precio">Precio</label><input type="number" v-model="upPrecio">
                        <label for="stock">Stock</label><input type="number" v-model="upStock">
                        <label>Talles:</label>
                        <div class="talles">
                            <div class="t-xs">
                                <span>XS</span>
                                <input type="number" v-model="upXS">
                            </div>
                            <div class="t-s">
                                <span>S</span>
                                <input type="number" v-model="upS">
                            </div>
                            <div class="t-m">
                                <span>M</span>
                                <input type="number" v-model="upM">
                            </div>
                            <div class="t-l">
                                <span>L</span>
                                <input type="number" v-model="upL">
                            </div>
                            <div class="t-xl">
                                <span>XL</span>
                                <input type="number" v-model="upXL"> 
                            </div>
                            <div class="t-xxl">
                                <span>XXL</span>
                                <input type="number" v-model="upXXL">
                            </div>
                        </div>
                        <label>Tipo:</label>
                        <div class="checkboxs">
                            <div>
                                <label for="urban">Urban</label>
                                <input type="radio" value="Urban" name="tipo2" v-model="upTipo"> 
                            </div>
                            <div>
                                <label for="vestir">Vestir</label>
                                <input type="radio" value="Vestir" name="tipo2" v-model="upTipo">
                            </div>
                        </div>
                        <label for="image">URL Imágen del Producto</label>
                        <input type="text" name="image" v-model="upUrl">
                        <button class="boton" @click="actualizar">Actualizar</button>
                    </form>
                </div>
            </div>
        </section>
        

        <section style="--clr:#27374D;" id="eliminar">
            <div class="tarjeta eliminar">
                <div class="contenido">
                    <h1>Eliminar</h1>
                    <form class="formulario">
                        <label for="identificadorDel">ID</label><input type="number" v-model="delID">
                        <label for="nombre">Nombre</label><input type="text" v-model="delNombre">
                        <button type="button" class="boton" @click="eliminar">Eliminar</button>
                    </form>
                </div>
            </div>
        </section>
    </main>
</template>
<script>
import { mapState } from 'vuex';
import store from '../stores/store'; 


export default{
    data(){
        return{
            //agregar
            newNombre: null,
            newPrecio: null,
            newStock: null,
            newTipo: null,
            newUrl: null,
            newXS: 0,
            newS: 0,
            newM: 0,
            newL: 0,
            newXL: 0,
            newXXL: 0,
            //eliminar
            delID: null,
            delNombre: null,
            //modificar
            upID: null,
            upNombre: null,
            upPrecio: null,
            upStock: null,
            upTipo: null,
            upUrl: null,
            upXS: 0,
            upS: 0,
            upM: 0,
            upL: 0,
            upXL: 0,
            upXXL: 0,
        }
    },
    computed: {
        ...mapState(['isAdmin', 'userEmail']),
    },
    beforeRouteEnter(to, from, next) {
  // Verifica si el usuario es administrador
  const isAdmin = store.state.userEmail === 'admin@gmail.com';

  if (isAdmin) {
    next(); // Permite el acceso si el usuario es administrador
  } else {
    next('/access-denied'); // Redirige a una página de acceso denegado si el usuario no es administrador
  }
},
    methods:{
        agregar(){
            let producto = {
                nombre: this.newNombre,
                precio: this.newPrecio,
                stock: this.newStock,
                tipo: this.newTipo,
                image: this.newUrl,
                XS: this.newXS,
                S: this.newS,
                M: this.newM,
                L: this.newL,
                XL: this.newXL,
                XXL: this.newXXL,
            };

            let url="http://localhost:5000/productos"
            var options={
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(producto)
            }
            fetch(url,options) 
                .then(function(){
                    console.log('creado')
                    alert("Grabado")
                })
                .catch(err => { 
                    alert("Error al grabar")
                    console.error(err)
                })
        },
        eliminar(){
            const url='http://localhost:5000/producto/' + this.delID; 
            var options={
                method: 'DELETE',
            }

            fetch(url, options)
                .then(res => res.text())
                .then(res => {
                    location.reload()
                    alert('Producto Eliminado')
                })
                .catch(err=>{
                    alert('Error al Eliminar el producto')
                })
        },
        actualizar(){
            let producto={
                id : this.upID,
                nombre : this.upNombre,
                precio : this.upPrecio,
                stock : this.upStock,
                tipo : this.upTipo,
                image : this.upUrl,
                XS: this.upXS,
                S: this.upS,
                M: this.upM,
                L: this.upL,
                XL: this.upXL,
                XXL: this.upXXL,
            }

            const url = 'http://localhost:5000/producto/' + this.upID;
            var options={
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(producto)
            }

            fetch(url, options)
                .then(res => res.text())
                .then(res => {
                    alert('Producto Modificado')
                })
                .catch(err => {
                    alert('No se pudo Modificar el producto')
                })
        }
    },
}

</script>

<style scoped>
/* NAV */
header{
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 50px;
    display: flex;
    justify-content: center;
    padding: 10px 50px 0;
    background-color: rgb(34, 34, 34);
    z-index: 9;
    overflow: hidden;
}
.barra-nav{
    display: flex;
    flex-direction: column;
    gap: 50px;
    margin-top: 100px;
}
.barra-nav a{
    position: relative;
    text-decoration: none;
    padding: 12px 20px;
    color: #fff;
    font-weight: 500;
    letter-spacing: 1px;
    font-size: .9em;
}
.barra-nav a:hover{
    color: #fff;
}
.barra-nav a.active{
    background: var(--clr);
    border-top-left-radius: 50px;
    border-bottom-left-radius: 50px;
}
.barra-nav a.active::before{
    content: '';
    width: 20px;
    height: 20px;
    position: absolute;
    bottom: -20px;
    right: 0;
    border-top-right-radius: 20px;
    box-shadow: 5px -5px 0 5px var(--clr);
    background-color: transparent;
}
.barra-nav a.active::after{
    content: '';
    width: 20px;
    height: 20px;
    position: absolute;
    top: -20px;
    right: 0;
    border-bottom-right-radius: 20px;
    box-shadow: 5px 5px 0 5px var(--clr);
    background-color: transparent;
}


/* TARJETAS */
main{
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
section{
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background: var(--clr);
}
.contenido h1{
    text-align: center;
    color: #27374D;
    text-transform: uppercase;
    letter-spacing: 3px;
}
.tarjeta{
    width: 70%;
    height: 90%;
    background: transparent;
    border-radius: 2px;
    backdrop-filter: blur(20px);
    box-shadow: 0 0 30px rgba(0, 0, 0, .5); 
    padding: 50px;
    margin: 5% 0;
}


.formulario{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: #27374D;
    
}
.formulario label{
    padding: 40px 0 15px;
    font-weight: 700;
    letter-spacing: 2px;
    width: 50%;
}
.formulario input{
    padding: 5px;
    letter-spacing: 1px;
    width: 50%;
    border: none;
    border-radius: 3px;
    transition: .5s;
    font-weight: 500;
}
.formulario input:focus{
    background-color: #27374D;
    color: #fff;
}
#identificador,
#stock{
    font-family: sans-serif;
}
.talles{
    width: 50%;
    display: flex;
}
.talles div{
    display: flex;
    flex-direction: column;
}
.talles div span{
    font-weight: 700;
    margin-bottom: 2%;
}
.checkboxs{
    display: flex;
    text-align: center;
}
.checkboxs div input{
    accent-color: #27374D;
    margin-right: 3px;
    cursor: pointer;
}
.boton{
    margin: 40px auto 0;
    width: 50%;
    height: 35px;
    color: #fff;
    font-size: 1em;
    text-transform: uppercase;
    font-weight: 600;
    letter-spacing: 2px;
    border: none;
    background-color: #27374D;
    border-radius: 3px;
    cursor: pointer;
}

.tarjeta.eliminar h1,
.tarjeta.eliminar label{
    color: #fff;
}
.tarjeta.eliminar .boton{
    background-color: #9DB2BF;
}

@media(max-width: 768px){
    header{
        display: none;
    }
    main{
        margin-top: 80px;
    }
    .tarjeta{
        width: 90%;
        top: 60%;
        margin-bottom: 5%;
    }
    .formulario{
        width: 100%;
        font-size: 1.2em;
    }
    .formulario label{
        width: 100%;
    }
    .formulario input{
        width: 100%;
        padding: 10px;
        font-size: .9em;
    }
    .checkboxs div{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        margin:0 5%
    }
    .checkboxs div input{
        width: 20px;
        height: 20px;
    }
    .boton{
        width: 100%;
    }
}

@media(min-width: 769px) and (max-width: 1200px){
    header{
        display: none;
    }
}
</style>