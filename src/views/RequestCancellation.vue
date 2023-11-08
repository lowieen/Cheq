<template>
    <div class="wrapper">
        <div class="container">
            <div class="banner">
                <h2>Solicitud de Cancelación</h2>
            </div>
            <div class="container-err" v-if="formNull">
                <p>Por favor completa todos los campos</p>
            </div>
            <div class="container-form">
                <div class="form-solicitud">
                    <form>
                        <div class="container-input">
                            <input type="text" name="nombre" required v-model="nombre">
                            <label for="nombre">Nombre:</label>
                        </div>
                        <div class="container-input">                       
                            <input type="text" name="apellido" required v-model="apellido">
                            <label for="apellido">Apellido:</label>
                        </div>
                        <div class="container-input">                           
                            <input type="text" name="dni" required v-model="dni">
                            <label for="dni">DNI:</label>
                        </div>
                        <div class="container-input">                         
                            <input type="text" name="compra" required v-model="compra">
                            <label for="compra">Numero de compra:</label>
                        </div>
                        <div class="container-input">                     
                            <input type="email" name="email" required v-model="email">
                            <label for="email">Email:</label>
                        </div>
                        <div class="container-input">                         
                            <textarea name="motivo" cols="30" rows="10" required v-model="motivo"></textarea>
                            <label for="motivo">Motivo de la solicitud:</label>
                        </div>
                        <div class="container-btn">
                            <button type="button" class="enviar" @click="send" :style="{backgroundColor:color}">{{ msjBtn }}</button>
                        </div>
                    </form>
                </div>
                <div  class="recordatorio">
                    <h5>Recordá que:</h5>
                    <p>Tendrás un plazo máximo de 10 días de corrido posteriores a la recepción del pedido para solicitar la revocación.</p>
                    <p>Gestionaremos la devolución una vez recibidas en nuestro depósito las prendas que desees devolver, siempre considerando 
                    que deberán estar en perfecto estado, sin uso, en su empaque y con sus etiquetas originales.</p>
                    <p>El dinero a reembolsar será reintegrado al mismo medio de pago que hayas utilizado al momento de la compra.</p>
                    <p>Considera que los tiempos de impacto y acreditación dependerán exclusivamente de tu entidad financiera y bancaria.</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    data(){
        return{
            //form
            nombre: null,
            apellido: null,
            dni: null,
            compra: null,
            email: null,
            motivo: null,
            //btn
            msjBtn: 'Enviar mensaje',
            formNull: false,
            color: '#27374D'
        }
    },
    methods:{
        send(){
            if(this.nombre!==null && this.apellido!==null && this.dni!==null && this.compra!==null && this.email!==null && this.motivo!==null){
                let mail = {
                    nombre : this.nombre,
                    apellido : this.apellido,
                    dni : this.dni,
                    compra : this.compra,
                    email : this.email,
                    motivo : this.motivo
                }

                let url="http://localhost:5000/cancellation"
                var options={
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(mail)
                }

                
                fetch(url, options)
                    .then(res => {
                        if (res.ok) {
                            this.color = 'green';
                            this.msjBtn = 'Mensaje enviado!';
                        } else {
                            throw new Error('Error en la solicitud.');
                        }
                    })
                    .catch(err => {
                        this.color = 'red';
                        this.msjBtn = 'Error en el envio.';
                        console.error('Error en la solicitud:', err);
                    });
            } else {
                this.formNull = true;
            }
        },
    }
}
</script>

<style scoped>
.wrapper{
    width: 100%;
    margin-bottom: 5%;
}
.container{
    width: 70%;
    margin: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
.banner{
    width: 100%;
    margin:5% 0;
}
.banner h2{
    color: #27374D;
    font-size: 2.5em;
    letter-spacing: .15em;
    word-spacing: .5em;
}
.container-err{
    width: 100%;
}
.container-err p{
    color: red;
    font-weight: 600;
    text-align: start;
}
.container-form{
    display: flex;
    align-items: center;
    justify-content: center;

}
.form-solicitud{
    width: 50%;
    padding: 40px;
}
.form-solicitud div{
    position: relative;
    width: 100%;
    height: 50px;
    margin: 30px 0;
}
.container-input{
    position: relative;
    width: 100%;
    height: 50px;
    border-bottom: 2px solid #27374D;
    margin: 30px 0;
}
.container-input input:focus~label,
.container-input input:valid~label,
.container-input textarea:focus~label,
.container-input textarea:valid~label{
    top: -3px;
    font-weight: 600;
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
.container-input input{
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    font-size: 1em;
    color: #27374D;
    font-weight: 400;
    padding: 0 35px 0 15px;
}
.container-input textarea{
    width: 100%;
    height: 150px;
    margin-top: 15px;
    padding: 20px;
    font-size: 1em;
    resize: none;
}

.container-input textarea~label{
    top: 70%;
}

.enviar{
    width: 100%;
    height: 45px;
    background: #27374D;
    border: none;
    outline: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.2em;
    color: #fff;
    font-weight: 500;
    transform: translateY(100px);
    transition: background-color 3s ease;
}
.recordatorio{
    width: 50%;
    height: 100%;
    color: #27374D;
    margin-left: 5%;
}
.recordatorio h5{
    font-size: 1.5em;
    margin: 5% 0;
    letter-spacing: 2px;
}
.recordatorio p{
    letter-spacing: 1px;
    line-height: 1.5em;
    margin: 5% 0;
}

/*media query*/
@media (max-width: 768px){
    .wrapper{
        margin-top: 85px;
    }
    .banner h2{
        font-size: 1.7em;
        text-align: center;
    }
    .container{
        width: 100%;
    }
    .container-form{
        flex-direction: column;
    }
    .container-input label{
        font-size: 1.2em;
    }
    .container-input input{
        font-size: 1.1em;
    }
    .container-input textarea{
        font-size: 1.2em;
    }
    .form-solicitud{
        width: 100%;
    }
    .recordatorio{
        width: 80%;
        margin-top: 10%;
    }
    .recordatorio h5{
        font-size: 1.8em;
    }
    .recordatorio p{
        font-size: 1.2em;
        line-height: 1.8em;
    }
}
@media (max-width: 1200px){
    .banner h2{
        font-size: 1.9em;
        text-align: center;
    }
    .container{
        width: 90%;
    }
    .form-solicitud{
        padding: 40px 0;
    }
    
}
@media (max-width: 1400px){
    .container{
        width: 90%;
    }
    .form-solicitud{
        padding: 40px 0;
    }
}

</style>