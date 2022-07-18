def leiaInt(num):
    while True:
        try:
            inteiro = int(input(num))
        except (ValueError, TypeError):
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrompida pelo utilizador.\033[m")
            return 0
        else:
            return inteiro
rec = 0
def autoIncrement():   
    global rec
    pStart = 1 #adjust start value, if req'd 
    pInterval = 1 #adjust interval value, if req'd
    if (rec == 0): 
        rec = pStart 
    else: 
        rec = rec + pInterval 
    return str(rec).zfill(1)

def linha(tam = 45):
    return "-"* tam

def cabecalho(txt):
    print(linha())
    print(txt.center(45))
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[36m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[33mSua opção: \033[m")
    return opc