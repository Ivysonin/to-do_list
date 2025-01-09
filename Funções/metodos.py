# Definindo cores usando sequência de escape ANSI
cor_verde = '\033[1;32m'
cor_ciano = '\033[1;36m'
cor_vermelho = '\033[31m'
reset_cor = '\033[0m' # Resetar a cor para o padrão

# adicionando tarefas
def adicionar() -> str:
    tarefas = input (f'\n{cor_ciano}--- Digite sua tarefa: {reset_cor}')
    return tarefas

# Exibindo tarefas
def exibir(lista : list) -> str: # Retorna str porque vai printar as tarefas
    contador = 1
    # Organização
    print(f'\n{cor_verde}----- Tarefas -----')
    for tarefas in lista:
        print(f'  {contador}. {tarefas}')
        contador += 1
    print(f'{reset_cor}')

# Removendo item da lista
def remover(lista : list) -> str:
    try:
        removendo = int(input(f'\n{cor_ciano}--- Digite o número correspondente a tarefa que deseja remover: {reset_cor}'))
        '''O valor 'removendo' precisa ser maior que 0 para poder remover(não existe 0 na lista)
        e o valor precisa ser menor ou igual a quantidade de tarefas que existe dentro da lista,
        não posso remover um item com um número que não tenha na lista'''
        if 0 < removendo <= len(lista):
            del lista[removendo - 1] # Se o usuario digitar '1' não remove o primeiro pq para remover o primeiro o indice precisa ser 0. por isso uso '- 1' tornando o número 1 em indice 0
            print(f'\n{cor_verde}----- Tarefa removida com sucesso -----{reset_cor}') 
        else:
            print (f'\n{cor_vermelho}===== Número inválido. Tente novamente. ====={reset_cor}')
    except ValueError:
        print(f'\n{cor_vermelho}===== ERRO: Digite o número do item da lista. ====={reset_cor}')
    except:
        print(f'\n{cor_vermelho}===== ERRO: não identificado. ====={reset_cor}')

def concluir(lista : list) -> str: # Retorna um indice sublinhado na lista
    def riscar_texto(tarefa):
        return ''.join([letra + '\u0336' for letra in tarefa]) # Separa cada 'letra' da 'tarefa' colocando traços entre eles, depois só juntar tudo com a função join()

    # Pegando o indice que o usuário quer concluir
    indice_para_concluir = int(input(f'\n{cor_ciano}--- Digite o número correspondente a tarefa que deseja concluir: {reset_cor}'))

    if 0 < indice_para_concluir <= len(lista):
        concluido = lista[indice_para_concluir - 1] # recebe o indice da lista-1 para ficar o indice exato que o usuario digitou(sempre vai ser um a menos)

        del lista[indice_para_concluir - 1] # Removendo o item da lista para não ficar um item sem concluir e um concluído

        # Organização
        print(f'\n{cor_verde}----- Tarefa concluída com sucesso -----{reset_cor}')
        
        return lista.append(riscar_texto(concluido)) # Adicionando a tarefa concluida para a lista
    else:
        print(f'\n{cor_vermelho}===== Número inválido. Tente novamente. ====={reset_cor}')