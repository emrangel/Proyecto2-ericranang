from flask import jsonify, Blueprint, render_template, current_app
from models.ingrediente import Ingrediente
from models.producto import Producto
from models.heladeria import Heladeria

heladeria_blueprint = Blueprint('heladeria_bp', __name__, url_prefix="/")

@heladeria_blueprint.route('/ingredientes')
def ingredientes():
    ingredientes = Ingrediente.query.all()
    return render_template("ingredientes.html", ingredientes = ingredientes)

@heladeria_blueprint.route('/productos')
def productos():
    productos = Producto.query.all()
    return render_template("productos.html", productos = productos)
