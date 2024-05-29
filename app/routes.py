from flask import Blueprint, jsonify, request, redirect, url_for, render_template
from .models import db, Cliente, Gabinete
from .forms import ClienteForm


crud = Blueprint('crud', __name__)

def to_dict(model_instance):
    """
    Convierte un objeto SQLAlchemy en un diccionario.
    """
    return {column.name: getattr(model_instance, column.name) for column in model_instance.__table__.columns}

# Rutas CRUD para Cliente
@crud.route('/', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([to_dict(cliente) for cliente in clientes])

@crud.route('/clientes', methods=['GET'])
def mostrar_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@crud.route('/clientes/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if cliente:
        return jsonify(to_dict(cliente))
    else:
        return jsonify({'error': 'Cliente no encontrado'}), 404

# Implementa las demás rutas CRUD para Cliente, Gabinete y otros modelos...
@crud.route('/clientes/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        nuevo_cliente = Cliente(nombre=form.nombre.data, apellido=form.apellido.data, direccion=form.direccion.data,
                                telefono=form.telefono.data, correoelectronico=form.correoelectronico.data)
        db.session.add(nuevo_cliente)
        db.session.commit()
        return redirect(url_for('crud.get_clientes'))
    return render_template('index.html', form=form)

@crud.route('/clientes/<int:clienteid>/modificar', methods=['GET', 'POST'])
def modificar_cliente(clienteid):
    cliente = Cliente.query.get_or_404(clienteid)
    form = ClienteForm(obj=cliente)
    if form.validate_on_submit():
        form.populate_obj(cliente)
        db.session.commit()
        return redirect(url_for('crud.get_clientes'))
    return render_template('modificar_cliente.html', form=form, cliente=cliente)

@crud.route('/clientes/<int:clienteid>/eliminar', methods=['POST'])
def eliminar_cliente(clienteid):
    cliente = Cliente.query.get_or_404(clienteid)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('crud.mostrar_clientes'))
