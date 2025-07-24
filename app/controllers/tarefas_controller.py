from flask import Blueprint, jsonify, request, render_template, url_for, redirect
from app.services import tarefas_service

tarefas_bp = Blueprint('tarefas', __name__, url_prefix='/tarefas')


# Exibindo todas as tarefas
@tarefas_bp.route('/', methods=['GET'])
def exibir():
    tarefas = tarefas_service.lista_tarefas()
    return render_template("tarefas.html", tarefas=tarefas)


# Adicionando uma nova tarefa
@tarefas_bp.route('/', methods=['POST'])
def adicionar():
    texto = request.form.get('descricao')

    if texto:
        tarefas_service.adicionar_tarefa(texto)
    
    return redirect(url_for("tarefas.exibir"))


# Atualizando a tarefa para concluída
@tarefas_bp.route('/<int:id>/concluir', methods=['POST'])
def concluir(id):
    tarefas_service.marcar_concluida(id)

    return redirect(url_for("tarefas.exibir"))


# Removendo tarefaa
@tarefas_bp.route('/<int:id>', methods=['POST'])
def remover(id):
    tarefas_service.remover_tarefa(id)

    return redirect(url_for("tarefas.exibir"))