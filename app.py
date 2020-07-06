from functools import wraps
from flask import Flask, render_template, request, redirect, session
from models.Cliente import Cliente
from models.Producto import Producto
from models.Pedido import Pedido
from models.Carrito import Carrito
##Es para registrarse, iniciar sesión y cerrar sesión
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
##url for % %
@app.route('/registro', methods=["get", "post"])
def registration():
    if request.method == "POST":
        user = Cliente(nombres=request.form["name"], email=request.form["email"], password=request.form["password"])
        estado_op = user.crear_cuenta()
        print(estado_op)
        if estado_op:
            user = Cliente.obtener_usuario(email=request.form["email"])
            if request.form["password"] == user.password:
                session['user_name'] = user.nombres
                session['user_email'] = user.email
                return redirect("/")
            else:
                error = 'Invalid password'
                return render_template('users/login.html', error=error)
        else:
            error = 'Invalid email'
            return render_template('users/register.html', error=error)

    return render_template('users/register.html', request=request)
#Ingresar datos de envio
@app.route('/datosenvio', methods=["get", "post"])
def datosenvio():
    return render_template('Ingresar_datos_envio.html', request=request)
#redireccion a pagina principal luego de pago
@app.route('/luegopago', methods=["get", "post"])
def luegopago():
    return redirect("/")
#Ingresar datos de pago
@app.route('/datospago', methods=["get", "post"])
def datospago():
    return render_template('Ingresar_datos_pago.html', request=request)
#Categorias
@app.route('/deportes', methods=["get", "post"])
def deportes():
    return render_template('deportes.html', request=request)

@app.route('/electrohogar', methods=["get", "post"])
def electrohogar():
    return render_template('electrohogar.html', request=request)

@app.route('/mascotas', methods=["get", "post"])
def mascotas():
    return render_template('mascotas.html', request=request)

@app.route('/supermercado', methods=["get", "post"])
def supermercado():
    return render_template('supermercado.html', request=request)

@app.route('/tecnologia', methods=["get", "post"])
def tecnologia():
    return render_template('tecnologia.html', request=request)

#-----------------------------------------------------------------------

@app.route('/canasta', methods=["get", "post"])
def canasta():
    return render_template('canastas_show_vacio.html', request=request)

@app.route('/carrito', methods=["get", "post"])
def carrito():
    email=session['user_email']
    carrito1=Carrito(1,'',0,email)
    ## Como deberia ser
    # 1. Verificar si el usuario tiene un pedido
    # 2. Si no tiene: crear un pedido para el usuario
    # 3. Crear linea de pedido(cod_prod, cod_pedido, cantidad)
    
    ## Si no tienen tiempo
    # Metanle defrente el precio de venta, para calcular el subtotal de la linea de pedido
    # Para el calcular el total del pedido, sumar los subtotales de las lineas de pedido de ese pedido
    # Codigo producto (finta)
    carrito_generado=carrito1.generarcarrito()
    if carrito_generado==False:
        print("No se genero carrito")


    if request.args.get('product_id')!=None:
        carrito_obtenido=carrito1.obtener_carrito(email)
        productos=carrito_obtenido.prod_nom()
        id_producto = request.args.get('product_id')
        if len(productos)<0:
            carrito_obtenido.prod_nom(id_producto)
        new_products=productos+','+id_producto



    return render_template('canastas_show_concosas.html', request=request)

@app.route('/Skullcandydetalle', methods=["get", "post"])
def detalleSkull():
    return render_template('productos_show.html', request=request)

@app.route('/historialpedidos', methods=["get", "post"])
def historialpedidos():
    return render_template('pedidos_index.html', request=request)


@app.route('/inicio-sesion', methods=["get", "post"])
def login():
    if request.method == "POST":
        print(request.form["email"])
        user = Cliente.obtener_usuario(email=request.form["email"])

        # Simple password validation
        if request.form["password"] == user.password:
            session['user_name'] = user.nombres
            session['user_email'] = user.email
            return redirect("/")
        else:
            error = 'Invalid password'
            return render_template('users/login.html', error=error)
    if session['user_name']!= None:
        return redirect('/')

    return render_template('users/login.html')

# Funcion solo permitir el ingreso si estas logueado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['user_name'] is None:
            return redirect('inicio-sesion')
        return f(*args, **kwargs)
    return decorated_function

@app.route('/logout')
@login_required
def logout():
    session['user_name'] = None
    session['user_email'] = None
    return redirect("/")

@app.route('/productos')
def products():
    filter = request.args.get('name')
    print(filter)
    product_list=Producto.obtener_productos(filter)

    return render_template("search.html",product_list=product_list) ##antes era products_list.html

@app.route('/producto/<string:codigo>')
def product_detail(codigo):
    product = Producto.obtener_producto(codigo)
    return render_template("productos_show.html", product=product)

@app.route("/categoria", methods =[ "get","post"])
def categoria_producto():
    cats=request.args.get('categoria')
    detalle_producto_categoria=Producto.obtener_producto_categoria(cats)
    return render_template("search.html", product_list = detalle_producto_categoria)

@app.route("/pago/<id_pedido>", methods = ["get","post"])
def pago(id_pedido):
    historialpedidos = Pedido.obtener_pedidos()
    for pedido in historialpedidos:
        if id_pedido == pedido[0]:
            return render_template("Pago.html", pedido = pedido)

if __name__ == "__main__": 
    ##es para que la aplicación corra en el servidor que creamos
    app.secret_key = "clave_super_ultra_secreta"

    app.run(debug=True)
