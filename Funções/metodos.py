# adicionando tarefas
def adicionar():
    tarefas = input ('\n=== Digite sua tarefa: ')
    return tarefas

# Exibindo tarefas
def exibir(lista : list) -> str: # Retorna str porque vai printar as tarefas
    contador = 1
    print ('\n--- Tarefas ---\n') # Organização
    for tarefas in lista:
        print(f'{contador}. {tarefas}')
        contador += 1