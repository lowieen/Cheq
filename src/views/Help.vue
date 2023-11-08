<template>
    <div class="wrapper">
        <div class="container">
            <div class="container-title">
                <h3>AYUDA</h3>
            </div>
            <div class="container-faq">
                <div class="title-faq">
                    <h5>Preguntas frecuentes</h5>
                </div>
                <div class="container-question">
                    <div class="seccion" @click="optionA" :class="{active:show=='A' && active}">
                        <h6>¿Los descuentos y promociones son los mismos que en el local?</h6>
                        <span :class="{on:show == 'A' && active}"></span>
                    </div>
                    <transition>
                        <div v-if="show == 'A' && active == true">
                            <p>Para realizar la compra no es necesario que estés registrado, aunque sí recomendamos que lo hagas. En caso que ya tengas una cuenta, ingresá con la información de acceso que te hayamos enviado al correo que nos hayas indicado, y seguí las instrucciones: <br>
                            1-Navegá por las categorías de tu preferencia y cuando estés interesado en algún producto simplemente hacé click. <br>
                            2-Seleccioná para aquellos casos requeridos el talle y color de la prenda y hacé click en "COMPRAR" <br>
                            3-Una vez agregado el producto, dirigite al Carrito. Podrás iniciar la compra haciendo click en el botón que así lo indica o continuar navegando y repetir el proceso cuantas veces sea necesario <br>
                            4-En caso de tener un código promocional, ingresalo en este paso. <br>
                            5-Seleccioná el método de envío (retiro en Sucursal OCA o envío a domicilio), e ingresá tu correo electrónico. <br>
                            6-Completá tus datos personales y dirección de envío. Por favor, verificá que todos los datos sean correctos antes de continuar. <br>
                            7-Seleccioná el método de pago. <br>
                            8-En tu resumen de compra figurará el detalle de los productos que hayas agregado. Verificá que el pedido que estés por realizar sea correcto. En caso de que precises modificar algo, simplemente eliminá el elemento y volvé a repetir los primeros pasos. <br>
                            9-¡Listo! Te enviaremos un correo electrónico con la confirmación de tu compra.</p>
                        </div>
                    </transition>
                </div>
                <div class="container-question">
                    <div class="seccion" @click="optionB" :class="{active:show=='B' && active}">
                        <h6>Me registré pero no puedo ingresar ¿Qué hago?</h6>
                        <span :class="{on:show == 'B' && active}"></span>
                    </div>
                    <transition>
                        <div v-if="show == 'B' && active == true">
                            <p>En caso que estés teniendo problemas para ingresar, verificá que estés utilizando los datos que hayas colocado al momento de registrarte. 
                            Podrás validarlos contra el correo de confirmación con la información de acceso que te enviamos luego de haberte registrado. Si luego de corroborar esto aún continuás con inconvenientes, 
                            por favor ingresa en https://www.cheq.com/about para poder enviar un correo y mencionar el problema.</p>
                        </div>            
                    </transition>
                </div>
                <div class="container-question">
                    <div class="seccion" @click="optionC" :class="{active:show=='C' && active}">
                        <h6>¿Cuándo se confirma mi compra?</h6>
                        <span :class="{on:show == 'C' && active}"></span>
                    </div>
                    <transition>
                        <div v-if="show == 'C' && active == true">
                            <p>Recibirás un mail de confirmación o cancelación dentro de las primeras 24 horas. En caso de no haber recibido el correo, por favor comunicate con nosotros
                                con tu número de pedido, nombre, apellido y correo electrónico con el que realizaste la compra, para poder ayudarte.</p>
                        </div>
                    </transition>
                </div>
                <div class="container-question">
                    <div class="seccion" @click="optionD" :class="{active:show=='D' && active}">
                        <h6>¿Cómo cancelo mi compra?</h6>
                        <span :class="{on:show == 'D' && active}"></span>
                    </div>
                    <transition>
                        <div v-if="show == 'D' && active == true">
                            <p>En caso de requerir la cancelación de tu compra, por favor comunicate con nosotros en https://www.cheq.com/request-cancellation, y completa los datos para poder ayudarte.</p>
                        </div>
                    </transition>
                </div>
                <div class="container-question">
                    <div class="seccion" @click="optionE" :class="{active:show=='E' && active}">
                        <h6>¿Puedo retirar mi compra en una tienda?</h6>
                        <span :class="{on:show == 'E' && active}"></span>
                    </div>
                    <transition>
                        <div v-if="show == 'E' && active == true">
                            <p>¡Si! Además de los envíos a domicilio, también contamos con la opción de retiros en tienda. Para optar por esta modalidad, debés seleccionar la de tu preferencia entre las tiendas 
                            habilitadas, al momento de seleccionar el método de envío. 
                            Tené en cuenta que el envío a nuestras tiendas puede demorar hasta 10 días hábiles, y sólo podrás retirar la compra en la tienda que hayas elegido en el momento de la compra. 
                            Cuando esté disponible para ser retirada, te enviaremos un correo electrónico con los datos necesarios.</p>
                        </div>
                    </transition>
                </div>
                <div class="container-question">
                    <div class="seccion" @click="optionF" :class="{active:show=='F' && active}"> 
                        <h6>¿Los precios tienen IVA incluido?</h6>
                        <span :class="{on:show == 'F' && active}"></span>
                    </div>
                    <transition>    
                        <div v-if="show == 'F' && active == true">
                            <p>Sí, todos los precios publicados, así como los costos de envío, tienen el IVA incluido.</p>
                        </div>
                    </transition>
                </div>
                <div class="container-question">
                    <div class="seccion" @click="optionG" :class="{active:show=='G' && active}">
                        <h6>Cambios de Producto</h6>
                        <span :class="{on:show == 'G' && active}"></span>
                    </div>
                    <transition>
                        <div v-if="show == 'G' && active == true">
                            <p>Podrás realizar cambios dentro de los treinta (30) días corridos luego de recibida la compra en cualquiera de nuestros locales, presentando el ticket de cambio o compra, y con el producto en perfecto estado: mismas condiciones en las que fue recibido, en su empaque y con sus etiquetas originales. Por favor considerá que el cambio estará sujeto a la disponibilidad de la tienda en ese momento. Si por algún motivo no hubiese existencia de las prendas, te asesorarán para brindarte más opciones. <br>
                            En caso de no contar con un local físico en tu ciudad comunicate con nosotros con los siguientes datos: <br>
                            1. Por favor, indicanos tu número de pedido. <br>
                            2. Por favor, contanos qué prenda/s deseás cambiar y qué talle necesitás. Con esta información verificaremos el stock. En caso de no contar con disponibilidad, podrás realizar el cambio por otro/s artículo/s de igual valor o bien, en caso de que exista alguna diferencia de precio, podremos enviarte un link de pago. En caso de que sea a tu favor, podrás utilizar el importe para una futura compra. <br>
                            3. Por favor, indicanos cuál es la sucursal OCA más cercana a tu domicilio (debés seleccionar provincia, localidad, y el servicio “Admisión de Paquetes” en el siguiente link: https://www.oca.com.ar/Busquedas/Sucursales , e indicarnos luego dirección, localidad y código postal de la sucursal que hayas elegido). <br>
                            4. Te pedimos que guardes la prenda en la bolsa blanca en la cual recibiste el pedido con el fin de proteger la misma. <br>
                            5. Con la información de la sucursal que nos hagas llegar, te generaremos y enviaremos una etiqueta, la cual deberás imprimir y pegar en el paquete que armes, y acercarla a la sucursal OCA que nos hayas indicado. <br>
                            6. Ni bien nos llegue tu envío, realizaremos el cambio de la prenda y te la volveremos a despachar. <br> 
                            Algunas consideraciones para que tengas en cuenta: <br>
                            - El primer cambio es gratuito. En caso de querer realizarse un segundo cambio, deberás asumir el costo de la devolución de la prenda anterior y del redespacho de la nueva prenda. <br>
                            - Las prendas se cambian sólo por prendas de la misma temporada. <br>
                            -El primer cambio es gratuito. En caso de querer realizarse un segundo cambio, deberás asumir el costo de devolución del producto anterior y del envío del nuevo producto.</p> 
                        </div>
                    </transition>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    data(){
        return{
            show: null,
            grados: 315,
            active: false,
        }
    },
    methods:{
        optionA(){
            this.show = 'A';
            this.active = true;
        },
        optionB(){
            this.show = 'B';
            this.active = true;
        },
        optionC(){
            this.show = 'C';
            this.active = true;
        },  
        optionD(){
            this.show = 'D';
            this.active = true;
        },
        optionE(){
            this.show = 'E';
            this.active = true;
        },
        optionF(){
            this.show = 'F';
            this.active = true;
        },
        optionG(){
            this.show = 'G';
            this.active = true;
        },
    }
}
</script>


<style scoped>
.wrapper{
    width: 100%;
}
.container{
    width: 70%;
    margin: auto;
    margin-top: 5%;
    color: #27374D;
}
.container div{
    margin: 3% 0 2% 0;
}
.container-title h3{
    font-size: 3em;
    letter-spacing: .07em;
    word-spacing: .3em;
}
.container-faq{
    border-top: 1.5px solid #fff;
    border-radius: 3px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.5);
    padding: 30px;
}
.title-faq{
    font-size: 2em;
    border-bottom: 2px solid #27374D;
    padding-bottom: 20px;
}
.container-question{
    position: relative;
}
.container-question h6{
    font-size: 1.5em;   
    border-radius: 2px;
    border: 2px solid #3333331f;
    border-top: 1.5px solid #fff;
    border-right: 1.5px solid #ffffff4f;
    padding: 10px;
    background: linear-gradient(213deg, rgba(246,246,246,.5) 1%, rgba(255,255,255,0) 14%);
    cursor: pointer;
}
.container-question p{
    line-height: 2em;
    letter-spacing: 1px;
}
.seccion{
    position: relative;
    transition: box-shadow .5s ease;
}
.container-question span{
    position: absolute;
    top: 35%;
    right: 2%;
    width: 15px;
    height: 15px;
    border-top: 3px solid #27374D;
    border-right: 3px solid #27374D;
    border-radius: 2px;
    transform: rotate(315deg);
    transition: transform .3s ease;
}
.v-enter-active,
.v-leave-active {
    transition: opacity 0.3s ease;
}

.v-enter-from,
.v-leave-to {
    opacity: 0;
}
.seccion span.on{
    transform: rotate(135deg);
}
.active{
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.5);
}


@media (max-width: 1201px) {
    .container {
        width: 80%;
        margin-top: 10%;
    }

    .container-title h3 {
        font-size: 2.5em;
    }

    .container-question h6 {
        font-size: 1.2em;
        padding: 8px;
    }

    .container-question p {
        line-height: 1.6em;
    }
}

@media (min-width: 769px) and (max-width: 1200px) {
    .container {
        width: 80%;
        margin-top: 5%;
    }

  .container-question h6 {
        padding: 6px 30px 6px 6px;
    }
}

@media (max-width: 768px) {
    .wrapper{
        margin-top: 85px;
    }
    .container {
        width: 90%;
        margin: auto;
    }

    .container-title h3 {
        font-size: 2em;
    }
    .container-question h6 {
        font-size: 1em;
        padding: 6px 25px 6px 6px;
    }

    .container-question p {
        font-size: .9em;
        line-height: 1.4em;
    }

    .seccion span {
        width: 12px;
        height: 12px;
        right: 3%;
    }
}

</style>