# adicionando tarefas
def adicionar() -> str:
    tarefas = input ('\n=== Digite sua tarefa: ')
    return tarefas

# Exibindo tarefas
def exibir(lista : list) -> str: # Retorna str porque vai printar as tarefas
    contador = 1
    print ('\n--- Tarefas ---\n') # Organização
    for tarefas in lista:
        print(f'{contador}. {tarefas}')
        contador += 1

# Removendo item da lista
def remover(lista : list) -> str:
    try:
        removendo = int(input('\n=== Digite o número correspondente a tarefa que deseja remover: '))
        '''O valor 'removendo' precisa ser maior que 0 para poder remover(não existe 0 na lista)
        e o valor precisa ser menor ou igual a quantidade de tarefas que existe dentro da lista,
        não posso remover um item com um número que não tenha na lista'''
        if 0 < removendo <= len(lista):
            del lista[removendo - 1] # Se o usuario digitar '1' não remove o primeiro pq para remover o primeiro o indice precisa ser 0. por isso uso '- 1' tornando o número 1 em indice 0
            print('\n--- Tarefa removida com sucesso ---') 
        else:
            print ('\n--- Número inválido. Tente novamente. ---')
    except ValueError:
        print('\n===== ERRO: Digite o número do item da lista. =====')
    except:
        print('\n===== ERRO: não identificado. =====')