import smtplib
from flask import url_for
from email.mime.text import MIMEText
import urllib.parse 

def send_email(data):
    nombre = data['nombre']
    email = data['email']
    telefono = data['telefono']
    asunto = data['asunto']
    msj = data['mensaje']

    #Establecer conexion al servidor de correos SMTP
    conexion = smtplib.SMTP(host= 'smtp.gmail.com', port= 587)
    conexion.ehlo()

    # Crear el objeto MIMEText para el correo electrónico
    msg = MIMEText(f"Nombre: {nombre}\nEmail: {email}\nCelular: {telefono}\nAsunto: {asunto}\nMensaje: {msj}")
    msg['Subject'] = 'Mensaje de Contacto'
    msg['From'] = 'correo@gmail.com'
    msg['To'] = 'correo@gmail.com'

    try: 
        #Encriptacion TLS
        conexion.starttls()
        #Inicio sesión en el servidor SMTP
        conexion.login(user='correo@gmail.com', password= 'password aplicacion de terceros')
        #Enviar correo
        conexion.sendmail('correo@gmail.com', 'correo@gmail.com', msg.as_string())
        #Desconectar el servidor SMTP
        conexion.quit()
        return {'message': 'Correo electrónico enviado exitosamente'}, 200

    except Exception as e:
        print('Error al enviar el correo electrónico:', e)
        return {'message': 'Hubo un error al enviar el correo electrónico'}, 500
    

def send_cancellation(data):
    nombre = data['nombre']
    apellido = data['apellido']
    dni = data['dni']
    compra = data['compra']
    email = data['email']
    motivo = data['motivo']

    #Establecer conexion al servidor de correos SMTP
    conexion = smtplib.SMTP(host= 'smtp.gmail.com', port= 587)
    conexion.ehlo()

    # Crear el objeto MIMEText para el correo electrónico
    msg = MIMEText(f"Nombre: {nombre}\nApellido: {apellido}\nDNI: {dni}\nNumero de Compra: {compra}\nEmail: {email}\nMotivo: {motivo}")
    msg['Subject'] = 'Cancelación de Compra'
    msg['From'] = 'correo@gmail.com'
    msg['To'] = 'correo@gmail.com'

    try: 
        #Encriptacion TLS
        conexion.starttls()
        #Inicio sesión en el servidor SMTP
        conexion.login(user='correo@gmail.com', password= 'password aplicacion de terceros')
        #Enviar correo
        conexion.sendmail('correo@gmail.com', 'correo@gmail.com', msg.as_string())
        #Desconectar el servidor SMTP
        conexion.quit()
        return {'message': 'Correo electrónico enviado exitosamente'}, 200

    except Exception as e:
        print('Error al enviar el correo electrónico:', e)
        return {'message': 'Hubo un error al enviar el correo electrónico'}, 500


def send_purchase(data):
    dni = data['dni']
    nombre = data['nombre']
    apellido = data['apellido']
    telefono = data['telefono']
    direccion = data['direccion']
    localidad = data['localidad']
    provincia = data['provincia']
    cp = data['cp']
    email = data['email']
    nota = data['nota']
    articulo = data['articulo']
    total = data['total']
    num = data['numCompra']

    #Establecer conexion al servidor de correos SMTP
    conexion = smtplib.SMTP(host= 'smtp.gmail.com', port= 587)
    conexion.ehlo()

    # Crear el objeto MIMEText para el correo electrónico
    msg = MIMEText(f"Nombre: {nombre}\nApellido: {apellido}\nDNI: {dni}\nTelefono: {telefono}\nDirección: {direccion}\nLocalidad: {localidad}\nProvincia: {provincia}\nCodigo Postal: {cp}\nEmail: {email}\nNota: {nota}\n\n\nArticulos: {articulo}\nTotal: ${total}\nNumero de Compra: {num}")
    msg['Subject'] = 'Nueva Compra'
    msg['From'] = 'Tu email'
    msg['To'] = 'Tu mismo email u otro'

    try: 
        #Encriptacion TLS
        conexion.starttls()
        #Inicio sesión en el servidor SMTP
        conexion.login(user='Tu email', password= 'password email o password para aplicacion de terceros')
        #Enviar correo
        conexion.sendmail('tu email', 'tu email', msg.as_string())
        #Desconectar el servidor SMTP
        conexion.quit()
        return {'message': 'Correo electrónico enviado exitosamente'}, 200

    except Exception as e:
        print('Error al enviar el correo electrónico:', e)
        return {'message': 'Hubo un error al enviar el correo electrónico'}, 500
    


def send_newPass(email, token):
    conexion = smtplib.SMTP(host= 'smtp.gmail.com', port= 587)
    conexion.ehlo()

    # Codifica el enlace como UTF-8
    encoded_token = urllib.parse.quote(token)

    # Crear el objeto MIMEText para el correo electrónico y especifica la codificación
    msg_body = f"Utiliza este enlace para restablecer tu contrasena: {url_for('cambiar_contrasena', token=encoded_token, _external=True)}"
    # msg_body = f"Utiliza este enlace para restablecer tu contraseña: http://localhost:5173/new-password/{encoded_token}" #Si deseo cambiar la url exacta 
    msg = MIMEText(msg_body.encode('utf-8'), 'plain', 'utf-8')
    msg['Subject'] = 'Restablecer Contraseña'
    msg['From'] = 'correo@gmail.com'
    msg['To'] = email

    try: 
        # Encriptación TLS
        conexion.starttls()
        # Inicio sesión en el servidor SMTP
        conexion.login(user='correo@gmail.com', password= 'password aplicacion de terceros')
        # Enviar correo
        conexion.sendmail('correo@gmail.com', email, msg.as_string())
        # Desconectar el servidor SMTP
        conexion.quit()
        return {'message': 'Correo electrónico enviado exitosamente'}, 200

    except Exception as e:
        print('Error al enviar el correo electrónico:', e)
        return {'message': 'Hubo un error al enviar el correo electrónico'}, 500
