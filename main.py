# Importações
from Funções.metodos import adicionar, exibir, remover, concluir

# Variavel
lista_tarefas = []

# Organização
print ('\n----- To-do list -----')

while True:
    escolha = input('\n   Nossas opções:\n'
                    '[ 1 ] Adicionar tarefas\n'
                    '[ 2 ] Remover tarefa\n'
                    '[ 3 ] Exibir tarefas\n'
                    '[ 4 ] Marcar como concluído\n'
                    '[ 5 ] Encerrar programa\n'
                    'Escolha: ')
    
    # Adicionando tarefas
    if escolha == '1':
        tarefas_adicionadas = adicionar()
        lista_tarefas.append(tarefas_adicionadas)
    
    # Removendo tarefas
    elif escolha == '2':
        remover(lista_tarefas)

    # Exibindo tarefas
    elif escolha == '3': 
        exibir(lista_tarefas)

    # Concluindo tarefas
    elif escolha == '4':
        concluir(lista_tarefas)

    # Encerrando programa
    elif escolha == '5':
        print ('\n===== encerrando... =====\n')
        break
    
    # Caso digite algo que não seja 1, 2, 3 e 4
    else:
        print('\n===== Escolha os números apresentados. =====')