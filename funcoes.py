from time import sleep
import json
import os


def verificarLista():
    try:
        open('lista.json', 'r')
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True


def listaVazia():
    with open('lista.json', 'r') as lista:
        lista = json.load(lista)
        if len(lista) == 0:
            return True
        else:
            return False


def deletarLista():
    os.remove('lista.json')


def menu(*opcoes):
    print('=' * 43)
    print('MENU PRINCIPAL'.center(43))
    print('=' * 43)
    for x, opcao in enumerate(opcoes):
        print(f'[ {x + 1} ] > {opcao}.')
    print('=' * 43)
    quant = len(opcoes)
    resp = leiaMenu('Insira a opção desejada > ', quant)
    sleep(1)
    return resp


def leiaMenu(msg, quant):
    while True:
        try:
            resp = int(input(msg))
        except ValueError:
            print('Insira somente números inteiros.')
        else:
            if not 1 <= resp <= quant:
                print('Insira somente uma das opções acima, por favor.')
            else:
                return resp


def escreverTarefas(task, data, hora, descricao):
    if verificarLista():
        with open('lista.json', 'r') as lista:
            dicionario = json.load(lista)
            dicionario.append({
                'task': task,
                'data': data,
                'hora': hora,
                'descricao': descricao
            })
        with open('lista.json', 'w') as lista:
            json.dump(dicionario, lista)
    else:
        with open('lista.json', 'w') as lista:
            dicionario = [{
                'task': task,
                'data': data,
                'hora': hora,
                'descricao': descricao
            }]
            json.dump(dicionario, lista)


def mostrarTarefas():
    try:
        with open('lista.json', 'r') as lista:
            lista = json.load(lista)
            for x, tarefa in enumerate(lista):
                print(f'<------------ Tarefa {x + 1} ------------>')
                print(f'ID: {x + 1}')
                print(tarefa["task"] + '.')
                print(f'Data: {tarefa["data"]}.')
                print(f'Hora: {tarefa["hora"]}.')
                print(f'Descricao: {tarefa["descricao"]}.')
                print('<---------------------------------->')
                sleep(2.1)
                print()
    except (FileNotFoundError, FileExistsError):
        print('Arquivo de tarefas não encontrado.')


def excluirTarefa():
    mostrarTarefas()
    with open('lista.json', 'r') as lista:
        lista = json.load(lista)
        while True:
            try:
                opt = int(input('Insira o ID da tarefa para excluí-la > '))
            except ValueError:
                print('Insira somente números inteiros.')
            else:
                if 1 <= opt <= len(lista):
                    break
        del(lista[opt - 1])
    with open('lista.json', 'w') as arquivo:
        json.dump(lista, arquivo)


def bye():
    print('Saindo do programa, obrigado!')
    exit()
