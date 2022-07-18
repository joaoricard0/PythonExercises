from time import sleep
c = ('\033[m',      #0 - sem cor
    '\033[1;30;41m',#1 - vermelho
    '\033[1;32;42m',#2 - verde
    '\033[1;30;43m',#3 - amarelo
    '\033[1;32;46m',#4 - azul
    '\033[1;30;45m',#5 - roxo
    '\033[0;30;47m'    #6 - branco
    )


def ajuda(com):
    titulo(f"Acessando o manual do comando \'{com}\'",4)
    print(c[6])
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor])
    print('~' * tam)
    print(f"  {msg}")
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Porgrama Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)
titulo('PROGRAMA TERMINADO', 1)