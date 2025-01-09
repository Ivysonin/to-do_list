# Importações
from Funções.metodos import adicionar, exibir, remover, concluir

# Definindo cores usando sequência de escape ANSI
cor_ciano = '\033[1;36m'
cor_verde = '\033[1;32m'
cor_vermelho = '\033[31m'
cor_amarelo = '\033[33m'
reset_cor = '\033[0m' # Resetar a cor para o padrão

# Variavel
lista_tarefas = []

# Organização
print ('\n----- To-do list -----')

while True:
    print(f'\n     Nossas opções:')
    print('[ 1 ] Adicionar tarefas')
    print('[ 2 ] Remover tarefa')
    print('[ 3 ] Exibir tarefas')
    print('[ 4 ] Marcar como concluído')
    print('[ 5 ] Encerrar programa')
    escolha = input((f'{cor_ciano}=== Escolha: {reset_cor}'))
    
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
        print(f'\n{cor_vermelho}===== Encerrando... ====={reset_cor}\n')
        break
    
    # Caso digite algo que não seja 1, 2, 3 e 4
    else:
        print(f'\n{cor_vermelho}===== Escolha os números apresentados. ====={reset_cor}')