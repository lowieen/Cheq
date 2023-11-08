from flask import Flask, jsonify, request, session, render_template, redirect, url_for, flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from flask_bcrypt import generate_password_hash, check_password_hash
import secrets
from flask import render_template
import uuid
from datetime import datetime
from send_email import send_email
from send_email import send_cancellation
from send_email import send_purchase
from send_email import send_newPass
from datetime import datetime, timedelta

app=Flask(__name__) 
CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = secrets.token_hex(32) # Asignar clave secreta generada aleatoriamente
db=SQLAlchemy(app)
ma=Marshmallow(app)

#defino tabla
class catalogo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Integer)
    stock=db.Column(db.Integer)
    tipo=db.Column(db.String(20))
    url_Image=db.Column(db.String(200))
    XS=db.Column(db.Integer)
    S=db.Column(db.Integer)
    M=db.Column(db.Integer)
    L=db.Column(db.Integer)
    XL=db.Column(db.Integer)
    XXL=db.Column(db.Integer)
    def __init__(self,nombre,precio,stock,tipo,url_Image,XS,S,M,L,XL,XXL):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        self.tipo=tipo
        self.url_Image=url_Image
        self.XS=XS
        self.S=S
        self.M=M
        self.L=L
        self.XL=XL
        self.XXL=XXL


class users(db.Model):
    email=db.Column(db.String(50), primary_key=True)
    password=db.Column(db.String(100), nullable=False)
    reset_token = db.Column(db.String(32), unique=True)
    reset_token_expiration = db.Column(db.DateTime)
    def __init__(self, email, password, reset_token, reset_token_expiration):
        self.email=email
        self.password=password
        self.reset_token=reset_token
        self.reset_token_expiration=reset_token_expiration


class pedido(db.Model):
    numero = db.Column(db.String(36), primary_key=True)
    dni = db.Column(db.Integer)
    productos = db.Column(db.String(200))
    importe = db.Column(db.String(50))
    def __init__(self, dni, productos, importe):
        self.dni = dni
        self.productos = productos
        self.importe = importe
        self.numero = self.generar_numero_pedido()

    def generar_numero_pedido(self):
        pedido_numero = str(uuid.uuid4().hex[:8])  # Tomar los primeros 8 caracteres del UUID
        fecha_actual = datetime.now()
        numero_de_pedido = f'{pedido_numero}-{fecha_actual.strftime("%Y%m%d%H%M%S")}'
        return numero_de_pedido


class datosUser(db.Model):
    email=db.Column(db.String(50), primary_key=True)
    nombre=db.Column(db.String(20))
    apellido=db.Column(db.String(20))
    dni=db.Column(db.String(10))
    cel=db.Column(db.String(20))
    def __init__(self, email, nombre, apellido, dni, cel):
        self.email=email
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.cel=cel

class direcUser(db.Model):
    email=db.Column(db.String(50), primary_key=True)
    provincia=db.Column(db.String(30))
    localidad=db.Column(db.String(30))
    calle=db.Column(db.String(30))
    codigo_postal=db.Column(db.String(10))
    piso=db.Column(db.String(10))
    dpto=db.Column(db.String(10))
    datos_extra=db.Column(db.String(50))
    def __init__(self, email, provincia, localidad, calle, codigo_postal, piso, dpto, datos_extra):
        self.email=email
        self.provincia=provincia 
        self.localidad=localidad 
        self.calle=calle 
        self.codigo_postal=codigo_postal 
        self.piso=piso 
        self.dpto=dpto 
        self.datos_extra=datos_extra 

with app.app_context():
    db.create_all() #damos contexto y creo tablas


class catalogoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','stock','tipo','url_Image','XS','S','M','L','XL','XXL')
producto_schema=catalogoSchema()
productos_schema=catalogoSchema(many=True)

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = users
user_schema=UsersSchema()
users_schema=UsersSchema(many=True)

class pedidoSchema(ma.SQLAlchemyAutoSchema): #forma automatica
    class Meta:
        model = pedido
pedido_schema = pedidoSchema()
pedidos_schema = pedidoSchema(many=True)

class datosUserSchema(ma.Schema):
    email = fields.Email(required=True)
    nombre = fields.Str()
    apellido = fields.Str()
    dni = fields.Str()
    cel = fields.Str()
dato_schema=datosUserSchema()
datos_schema=datosUserSchema(many=True)

class direcUsersSchema(ma.Schema):
    email = fields.Email(required=True)
    provincia = fields.Str()
    localidad = fields.Str()
    calle = fields.Str()
    codigo_postal = fields.Str()
    piso = fields.Str()
    dpto = fields.Str()
    datos_extra = fields.Str()
direc_schema=direcUsersSchema()
direcs_schema=direcUsersSchema(many=True)
#------------------USERS------------------
# OBTENER USERS
@app.route('/users',methods=['GET'])
def get_users():
    all_users=users.query.all()
    result=users_schema.dump(all_users)
    return jsonify(result)

# INICIO DE SESION Y VALIDACION USER
@app.route('/user', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if not email or not password:
        return jsonify({'error': 'Faltan el correo electrónico o la contraseña.'}), 400
    # filter_by() para verificar si el email recibido es igual al email de db
    # firs() devuelve el primer registro que cumple condicion del filter
    user = users.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'El correo electrónico o la contraseña son incorrectas.'}), 400
    # Generar un token de sesión o una cookie de sesión
    session['user_email'] = user.email
    return jsonify({'message': 'Inicio de sesión exitoso.'}), 200

# CIERRE DE SESION
@app.route('/user/logout', methods=['GET'])
def logout():
    session.pop('user_email', None)
    return jsonify({'message': 'Cierre de sesión exitoso.'}), 200


# AGREGAR USER
@app.route('/users',methods=['POST'])
def create_user():
    email=request.json['email']
    password=request.json['password']
    reset_token=request.json['reset_token']
    reset_token_expiration=request.json['reset_token_expiration']

    if usuario_existente(email):
        return jsonify({'error':'El correo electrónico ya está registrado.'}),400
    
    hashed_password = generate_password_hash(password).decode('utf-8')
    
    new_user = users(email, hashed_password, reset_token, reset_token_expiration)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 201


def usuario_existente(email):
    all_users=users.query.all()
    result=users_schema.dump(all_users)
    return any(usuario['email'] == email for usuario in result)



# MODIFICAR PASSWORD
#Checkeo de email si existe
@app.route('/restablecer-contrasena', methods=['POST'])
def solicitar_restablecer_contrasena():
    email = request.json.get('email')
    user = users.query.filter_by(email=email).first()

    if user:
        # Genera un token único
        token = secrets.token_hex(16)
        user.reset_token = token
        user.reset_token_expiration = datetime.utcnow() + timedelta(hours=1)
        db.session.commit()

        # Envía el correo electrónico con el token
        response, status_code = send_newPass(user.email, token)
        return jsonify(response), status_code



#Restablecer password
@app.route('/new-password/<token>', methods=['GET', 'POST'])
def cambiar_contrasena(token):
    user = users.query.filter_by(reset_token=token).first()

    if not user or user.reset_token_expiration < datetime.utcnow():
        flash('El enlace para restablecer la contraseña es inválido o ha expirado. Solicita un nuevo enlace.', 'error')
        # Redirige al usuario a la página
        # return redirect(url_for('home'))
        return redirect("http://localhost:5173/") #redireccionar a url especifica
    
    if request.method == 'GET':
        if user.reset_token is None:  # Verifica si el token ya se ha utilizado
            flash('El enlace para restablecer la contraseña ya ha sido utilizado.', 'error')
            # return redirect(url_for('/'))
            return redirect("http://localhost:5173/")

        return jsonify({'token': token})

    elif request.method == 'POST':
        new_password = request.json.get('password')
        hashed_password = generate_password_hash(new_password).decode('utf-8')

        if hashed_password:
            # Actualiza la contraseña del usuario
            user.password = hashed_password
            user.reset_token = None
            user.reset_token_expiration = None
            db.session.commit()
            # Devuelve una respuesta JSON para indicar el éxito
            return jsonify({'message': 'Contraseña restablecida con éxito'}), 200
        else:
            # Devuelve una respuesta JSON para indicar un error
            return jsonify({'error': 'Contraseña no válida'}), 400

    # Si no es una solicitud GET o POST, puedes devolver una respuesta de otro tipo si es necesario
    return jsonify({'error': 'Método no permitido'}), 405


#-----------------------PERFIL-----------------
# Ruta para crear un perfil

@app.route('/data', methods=['POST'])
def create_datosPersonales():
    email = request.json['email']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    dni = request.json['dni']
    cel = request.json['cel']
    # Verificar si el usuario ya existe
    existing_user = users.query.filter_by(email=email).first()
    if existing_user is None:
        return jsonify({'error': 'El usuario no existe'}), 400
    # Verificar si el perfil ya existe en la base de datos
    existing_profile = datosUser.query.filter_by(email=email).first()
    if existing_profile:
        return jsonify({'error': 'El perfil ya existe'}), 400
    # Crea el perfil en la base de datos utilizando los datos recibidos
    new_data = datosUser(email=email, nombre=nombre, apellido=apellido, dni=dni, cel=cel)
    db.session.add(new_data)
    db.session.commit()

    return jsonify({'message': 'Perfil creado exitosamente'}), 200

@app.route('/direc', methods=['POST'])
def create_direc():
    email = request.json['email']
    provincia = request.json['provincia']
    localidad = request.json['localidad']
    calle = request.json['calle']
    codigo_postal = request.json['codigo_postal']
    piso = request.json['piso']
    dpto = request.json['dpto']
    datos_extra = request.json['datos_extra']

    existing_user = users.query.filter_by(email=email).first()
    if existing_user is None:
        return jsonify({'error': 'El usuario no existe'}), 400

    existing_profile = direcUser.query.filter_by(email=email).first()
    if existing_profile:
        return jsonify({'error': 'El perfil ya existe'}), 400

    new_data = direcUser(email=email, provincia=provincia, localidad=localidad, calle=calle, codigo_postal=codigo_postal, piso=piso, dpto=dpto, datos_extra=datos_extra)
    db.session.add(new_data)
    db.session.commit()

    return jsonify({'message': 'Perfil creado exitosamente'}), 200


# Modificacion de datos
# datos usuario
@app.route('/data/<id>', methods=['PUT'])
def update_data(id):
    data = datosUser.query.get(id)
    if data:
        # Actualizamos los campos del registro con los nuevos datos enviados en la solicitud
        data.nombre = request.json['nombre']
        data.apellido = request.json['apellido']
        data.dni = request.json['dni']
        data.cel = request.json['cel']

        # Guardamos los cambios en la base de datos
        db.session.commit()

        # Devolvemos una respuesta exitosa
        return jsonify({'message': 'Registro actualizado exitosamente'}), 200
    else:
        # Si no se encuentra el registro con el ID proporcionado, devolvemos un error
        return jsonify({'message': 'No se encontró el registro'}), 404

# datos direc
@app.route('/direc/<id>', methods=['PUT'])
def update_direc(id):
    data = direcUser.query.get(id)
    if data:
        # Actualizamos los campos del registro con los nuevos datos enviados en la solicitud
        data.provincia = request.json['provincia']
        data.localidad = request.json['localidad']
        data.calle = request.json['calle']
        data.codigo_postal = request.json['codigo_postal']
        data.piso = request.json['piso']
        data.dpto = request.json['dpto']
        data.datos_extra = request.json['datos_extra']

        # Guardamos los cambios en la base de datos
        db.session.commit()

        # Devolvemos una respuesta exitosa
        return jsonify({'message': 'Registro actualizado exitosamente'}), 200
    else:
        # Si no se encuentra el registro con el ID proporcionado, devolvemos un error
        return jsonify({'message': 'No se encontró el registro'}), 404
    

# datos usuario
@app.route('/data',methods=['GET'])
def data():
    all_users=datosUser.query.all()
    result=datos_schema.dump(all_users)
    return jsonify(result)


# direc usuario
@app.route('/direc', methods=['GET'])
def direc():
    all_direc=direcUser.query.all()
    result=direcs_schema.dump(all_direc)
    return jsonify(result)


#-----------------------MAILS----------------------
@app.route('/send-email', methods=['POST'])
def handle_send_email():
    data = request.json
    response, status_code = send_email(data)
    return jsonify(response), status_code



@app.route('/cancellation', methods=['POST'])
def handle_send_cancellation():
    data = request.json
    response, status_code = send_cancellation(data)
    return jsonify(response), status_code



@app.route('/purchase', methods=['POST'])
def handle_send_purchase():
    data = request.json
    response, status_code = send_purchase(data)
    return jsonify(response), status_code


#---------------------DETALLES PRODUCTO-----------------
@app.route('/producto/<int:id>')
def mostrar_detalle_producto(id):
    producto = catalogo.query.get(id)
    if producto:
        return render_template(producto=producto)
    else:
        return "Producto no encontrado", 404


#----------------------PEDIDOS------------------------
@app.route('/pedido/<numero>')
def get_pedido(numero):
    compra=pedido.query.get(numero)
    if compra:
        return pedido_schema.jsonify(compra)
    else:
        return "Producto no encontrado", 404
    
@app.route('/pedido')
def get_pedidos():
    all_pedidos=pedido.query.all()
    result=pedidos_schema.dump(all_pedidos)
    return jsonify(result)


@app.route('/pedido',methods=['POST'])
def nuevo_pedido():
    dni = request.json[0]['dni']
    productos = request.json[0]['productos']
    importe = request.json[0]['importe']

    nuevo_pedido = pedido(dni, productos, importe)
    
    db.session.add(nuevo_pedido)
    db.session.commit()

    numero_pedido = nuevo_pedido.numero
    
    return jsonify({'message': 'Pedido creado exitosamente', 'numeroPedido': numero_pedido}), 200


@app.route('/stock/<id>',methods=['PUT'])
def desc_stock(id):
    talle = request.json.get('talle')
    nuevo_stock = request.json.get('stock')
    nuevo_stockT = request.json.get('stockTalle')

    producto = catalogo.query.get(id)
    producto.stock = nuevo_stock

    if hasattr(producto, talle):
        setattr(producto, talle, nuevo_stockT)

    db.session.commit()

    return producto_schema.jsonify(producto)



#-----------------------MODIFICAR------------
# OBTENER TODOS LOS PRODUCTOS
@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=catalogo.query.all()
    result=productos_schema.dump(all_productos)
    return jsonify(result)


# OBTENER UN PRODCUTO
@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=catalogo.query.get(id)
    return producto_schema.jsonify(producto)


# ELIMINAR UN PRODUCTO
@app.route('/producto/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=catalogo.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)


# AGREGAR UN PRODUCTO
@app.route('/productos',methods=['POST'])
def create_producto():
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['stock']
    tipo=request.json['tipo']
    url_Image=request.json['image']
    XS=request.json['XS']
    S=request.json['S']
    M=request.json['M']
    L=request.json['L']
    XL=request.json['XL']
    XXL=request.json['XXL']

    new_producto=catalogo(nombre,precio,stock,tipo,url_Image,XS,S,M,L,XL,XXL)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)


# MODIFICAR UN PRODUCTO
@app.route('/producto/<id>',methods=['PUT'])
def update_producto(id):
    #obtengo los nuevos valores introducidos
    nuevo_nombre=request.json.get('nombre')
    nuevo_precio=request.json.get('precio')
    nuevo_stock=request.json.get('stock')
    nuevo_tipo=request.json.get('tipo')
    nuevo_url_Image=request.json.get('image')
    nuevo_XS=request.json.get('XS')
    nuevo_S=request.json.get('S')
    nuevo_M=request.json.get('M')
    nuevo_L=request.json.get('L')
    nuevo_XL=request.json.get('XL')
    nuevo_XXL=request.json.get('XXL')

    producto = catalogo.query.get(id)
    producto.nombre = nuevo_nombre 
    producto.precio = nuevo_precio
    producto.stock = nuevo_stock
    producto.tipo = nuevo_tipo
    producto.url_Image = nuevo_url_Image
    producto.XS = nuevo_XS
    producto.S = nuevo_S
    producto.M = nuevo_M
    producto.L = nuevo_L
    producto.XL = nuevo_XL
    producto.XXL = nuevo_XXL
    db.session.commit()

    return producto_schema.jsonify(producto)


#programa principal
if __name__=='__main__':
    app.run(debug=True, port=5000)


