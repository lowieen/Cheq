<template>
    <div class="wrapper">
        <div class="contenedor-contacto">
            <div class="form-contacto">
                <h2>CONTACTO</h2>
                <p>Completa el formulario y resolveremos tus dudas a la brevedad</p>
                <div class="container-err" v-if="formNull">
                    <p>Por favor completa todos los campos</p>
                </div>
                <form class="contactForm">
                    <div class="caja-contacto">
                        <input type="text" v-model="nombre" required>
                        <label>Nombre</label>
                    </div>
                    <div class="caja-contacto">
                        <input class="email" type="email" v-model="email" required>
                        <label>Email</label>
                    </div>
                    <div class="caja-contacto">
                        <input type="tel" v-model="telefono" required>
                        <label>Celular</label>
                    </div>
                    <div class="caja-contacto">
                        <input type="text" v-model="asunto" required>
                        <label>Asunto</label>
                    </div>
                    <div class="caja-contacto">
                        <textarea v-model="mensaje" cols="5" rows="3" required></textarea>
                        <label>Mensaje</label>
                    </div>
                    <div>
                        <button type="button" class="enviar" @click="send" :style="{backgroundColor:color}">{{ msjBtn }}</button>
                    </div>
                </form>
            </div>
            <div class="map">
                <h3>Encontranos en:</h3>
                <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d34776.47517227435!2d-58.45397920234262!3d-34.69978946344973!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1ses!2sar!4v1686363471826!5m2!1ses!2sar" style="border:0;" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
        </div>
    </div>
</template>
<script>

export default{
    data(){
        return{
            //cuerpo form
            nombre: null,
            email: null,
            telefono: null,
            asunto: null,
            mensaje: null,
            //btn
            msjBtn: 'Enviar mensaje',
            formNull: false,
            color: '#27374D'
        }
    },
    methods:{
        send(){
            if(this.nombre !== null && this.email !== null && this.telefono !== null && this.asunto !== null && this.mensaje !== null){
                let mail = {
                    nombre : this.nombre,
                    email : this.email,
                    telefono : this.telefono,
                    asunto : this.asunto,
                    mensaje : this.mensaje
                }

                let url="http://localhost:5000/send-email"
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
    height: 85vh;
    margin-bottom: 5%;
}
.contenedor-contacto{
    width: 85%;
    height: 100%;
    margin: 5% auto;
    display: flex;
    justify-content: center;
    background: rgba(255, 255, 255, .3);
    backdrop-filter: blur(20px);
    box-shadow: 5px 5px 30px rgba(0, 0, 0, .5); 
    padding: 40px;
}

.contenedor-contacto h2{
    font-size: 2em;
    color: #27374D;
    text-align: center;
    margin-bottom: 5px;
    letter-spacing: 3px;
}

.contenedor-contacto p{
    color: #27374D;
    text-align: center;
    letter-spacing: 1px;
}

.form-contacto{
    width: 60%;
    padding: 40px;
}

.caja-contacto{
    position: relative;
    width: 100%;
    height: 75px;
    border-bottom: 2px solid #27374D;
    margin: 30px 0;
}
.caja-contacto label{
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

.caja-contacto input:focus~label,
.caja-contacto input:valid~label,
.caja-contacto textarea:focus~label,
.caja-contacto textarea:valid~label{
    top: -3px;
    font-weight: 600;
}

.caja-contacto input{
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

.caja-contacto textarea{
    width: 100%;
    margin-top: 15px;
    padding: 20px;
    font-size: 1em;
    resize: none;
    transition: .3s ease;
}

.caja-contacto textarea:focus{
    background: #27374D;
    color: #fff;
}

.caja-contacto textarea~label{
    top: 70%;
}

.enviar{
    width: 100%;
    height: 45px;
    border: none;
    outline: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1.2em;
    color: #fff;
    font-weight: 500;
    transform: translateY(150%);
    transition: background-color .3s ease;
}

.container-err{
    margin: 3% 0 5%;
    width: 100%;
}
.container-err p{
    color: red;
    font-weight: 600;
    text-align: start;
}
.map{
    width: 40%;
    height: 100%;
    margin: 0 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    border-left: 2px solid #27374D;
    padding-left: 50px;
}

.map h3{
    letter-spacing: 2px;
}

.map iframe{
    width: 100%;
    height: 100%;
    margin: 20px auto;
}

@media (max-width: 768px){
    .wrapper{
        height: 100%;
        margin-top: 85px;
    }
    .contenedor-contacto{
        height: 100%;
        flex-direction: column;
        align-items: center;
        padding: 10px 40px 40px;
    }
    .contenedor-contacto p{
        text-align: start;
    }
    .form-contacto{
        width: 100%;
        padding: 0;
    }
    .caja-contacto{
        font-size: 1.2em;
    }
    .enviar{
        margin-bottom: 40%;
    }
    .container-err p{
        text-align: center;
    }
    .map{
        width: 100%;
        height: 500px;
        border-top: 2px solid #27374D;
        border-left: 0;
        padding: 60px 0 0 0;
    }
}

@media (min-width: 769px) and (max-width: 1100px){
    .wrapper{
        height: 100%;
    }
    .contenedor-contacto{
        height: 100%;
        flex-direction: column;
        align-items: center;
        padding: 10px 40px 40px;
    }
    .contenedor-contacto p{
        text-align: center;
    }
    .form-contacto{
        width: 100%;
    }
    .caja-contacto{
        font-size: 1.1em;
    }
    .enviar{
        margin-bottom: 20%;
    }
    .map{
        width: 100%;
        height: 500px;
        border-top: 2px solid #27374D;
        border-left: 0;
        padding: 60px 0 0 0;
    }
}

@media (min-width: 1100px) and (max-width: 1920px){
    .caja-contacto{
        height: 50px;
    }
}
</style>

