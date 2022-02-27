from funcoes import *

print('=-' * 21 + '=')
print("Bem-vindo ao Jack's To-do list.".center(43))
print('=-' * 21 + '=')

regulador = -1

while True:
    if verificarLista():
        if listaVazia():
            deletarLista()
            regulador = 0
        else:
            regulador = 1
    else:
        regulador = 0
    # Regulador 0: Lista vazia.
    if regulador == 0:
        opMenu = menu('Escrever na lista', 'Sair do programa')
        if opMenu == 1:
            escreverTarefas(str(input('Insira a tarefa > ')),
                            str(input('Insira a data > ')),
                            str(input('Insira a hora > ')),
                            str(input('Insira a descrição > ')))
            regulador = 1
        elif opMenu == 2:
            bye()

    if regulador == 1:
        opMenu = menu('Escrever na lista', 'Excluir alguma tarefa',  'Ler a lista', 'Sair do programa')
        if opMenu == 1:
            escreverTarefas(str(input('Insira a tarefa >')),
                            str(input('Insira a data >')),
                            str(input('Insira a hora >')),
                            str(input('Insira a descrição >')))
        elif opMenu == 2:
            excluirTarefa()
        elif opMenu == 3:
            mostrarTarefas()
        elif opMenu == 4:
            bye()
