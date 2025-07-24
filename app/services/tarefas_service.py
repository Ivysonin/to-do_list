tarefas = []
contador_id = 1


# Exibir todas as tarefas
def lista_tarefas():
    global tarefas

    return tarefas


# Adicionando uma nova tarefa
def adicionar_tarefa(texto):
    global contador_id

    nova_tarefa = {
        'id':contador_id,
        'descricao':texto,
        'concluida':False
    }
    tarefas.append(nova_tarefa)
    contador_id += 1

    return nova_tarefa # A tarefa vai ser exibida ao usuário


# Marcando como conluída a tarefa
def marcar_concluida(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['concluida'] = True
            return tarefa # A tarefa vai continuar sendo exibida
    return None
    

# Removendo tarefa
def remover_tarefa(id):
    global tarefas
    '''
    1. listo as tarefa que estão em tarefas
    2. se o id da minha tarefa for diferente do id que eu quero remover, adiciona as tarefas a lista
    3. se não, não adiciono
    Fazendo assim quando exibir as tarefas novamente, exibir sem a tarefa que foi removida
    '''
    tarefas = [t for t in tarefas if t['id'] != id]
    return True # a tarefa foi removida com sucesso