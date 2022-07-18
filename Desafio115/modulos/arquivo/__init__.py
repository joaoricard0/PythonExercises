from modulos.interface import *

def FicheiroExiste(fich):
    try:
        a = open(fich, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarFicheiro(fich):
    try:
        a = open(fich,'wt+')
        a.close()
    except:
        print("Houve um erro na criação do ficheiro!")
    else:
        print(f"Ficheiro {fich} criado com sucesso!")

def lerFicheiro(fich):
    try:
        a = open(fich,'rt')
    except:
        print("Erro ao ler o ficheiro!")
    else:
        cabecalho("Utilizadores registados")
        for linha in a:
            dado = linha.split(";")
            dado[2] = dado[2].replace('\n','')
            print(f"{dado[0]:>2} Nome: {dado[1]:>10}          Idade: {dado[2]:>2} anos")
        print(a.read())
    finally:
        a.close()

def registUser(fich, id, nome = 'desconhecido', idade = 0):
    try:
        a = open(fich, 'at')
    except:
        print("Houve um erro ao abrir o ficheiro!")
    else:
        try:
            a.write(f"{id};{nome};{idade}\n")
        except:
            print("Houve um erro ao gravar o novo registo!")
        else:
            print(f"Novo registo de {nome} adicionado!")
            a.close()

def deleteUser(fich, id):
    try:
        a = open(fich, 'r+')
        linhas = a.readlines()
    except:
        print("Houve um erro ao abrir o ficheiro!")
    else:
        try: 
            del linhas[id]
        except:
            print("Houve um erro ao apagar o registo!")
        else:
            new = open(fich, 'w+')
            for linha in linhas:
                new.write(linha)
            print(f"Registo apagado!")
            a.close()