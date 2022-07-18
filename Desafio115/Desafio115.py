from modulos.interface import *
from modulos.arquivo import *
from time import sleep
import os

bd = 'Desafio115/basedados.txt'

if not FicheiroExiste(bd):
    criarFicheiro(bd)

while True:
    resp = menu(['Registar Utilizadores','Listar Utilizadores','Apagar Utilizadores', 'Apagar Ficheiro', 'Sair do Sistema'])
    if resp == 1:
        #opção de registar utilizador
        cabecalho('Novo Registo')
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        id = autoIncrement()
        registUser(bd, id, nome, idade)
        
    elif resp == 2:
        #opção de mostrar a listagem do ficheiro
        lerFicheiro(bd) 
    elif resp == 3:
        cabecalho('Apagar registo')
        id = int(input("Qual o id que deseja apagar?"))
        deleteUser(bd,id)
    elif resp == 4:
        cabecalho('Apagar ficheiro')
        resp = input("Tem a certeza?[S/N]").upper()[0]
        if resp == 'S':
            os.remove(bd)
    elif resp == 5:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        cabecalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)