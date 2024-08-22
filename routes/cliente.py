from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """ lista os clientes """
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes = clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    
    data = request.json

    novo_usuario = Cliente.create(
        nome = data ['nome'],
        email = data['email'],
    )

    return render_template('item_cliente.html', cliente=novo_usuario )

@cliente_route.route('/new')
def form_cliente():
    """ formulário para cadastrar cliente """
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ exibir os detalhes do cliente """
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente = cliente)

@cliente_route.route('/<int:cliente_id>/edit', endpoint ='form_edit_cliente')
def form_edit_cliente(cliente_id):
    """ edita um cliente """
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente = cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    """ atualizar informacoes do cliente """
    data = request.json
    
    # obter usuario pelo id
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data ['nome']
    cliente_editado.email = data ['email']
    cliente_editado.save()
  
    # editar usuario
    return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    """ deleta as informações de um cliente """
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.delete_instance()
    return {'Deletado!'}

