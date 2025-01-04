# Importações
from Funções.metodos import adicionar, exibir

# Variavel
lista_tarefas = []

# Organização
print ('\n----- To-do list -----')

while True:
    escolha = input('\n   Nossas opções:\n'
                    '[ 1 ] Adicionar tarefas\n'
                    '[ 2 ] Remover tarefa\n'
                    '[ 3 ] Exibir tarefas\n'
                    '[ 4 ] Encerrar programa\n'
                    'Escolha: ')
    
    # Adicionando tarefas
    if escolha == '1':
        tarefas_adicionadas = adicionar()
        lista_tarefas.append(tarefas_adicionadas)
    
    # Removendo tarefas
    elif escolha == '2':
        try:
            removendo = int(input('\n=== Digite o número correspondente a tarefa que deseja remover: '))
            '''O valor 'removendo' precisa ser maior que 0 para poder remover(não existe 0 na lista)
            e o valor precisa ser menor ou igual a quantidade de tarefas que existe dentro da lista,
            não posso remover um item com um número que não tenha na lista'''
            if 0 < removendo <= len(lista_tarefas):
                del lista_tarefas[removendo - 1] # Se o usuario digitar '1' não remove o primeiro pq para remover o primeiro o indice precisa ser 0. por isso uso '- 1' tornando o número 1 em indice 0
                print('\n--- Tarefa removida com sucesso ---') 
            else:
                print ('\n--- Número inválido. Tente novamente. ---')
        except ValueError:
            print('\n===== ERRO: Digite o número do item da lista. =====')
        except:
            print('\n===== ERRO: não identificado. =====')

    # Exibindo tarefas
    elif escolha == '3': 
        print ('\n--- Tarefas ---\n') # Organização
        exibir(lista_tarefas)

    # Encerrando programa
    elif escolha == '4':
        print ('\n===== encerrando... =====\n')
        break
    
    # Caso digite algo que não seja 1, 2, 3 e 4
    else:
        print('\n===== Escolha os números apresentados. =====')