def leiaInt(num):
    while True:
        try:
            inteiro = int(input(num))
        except (ValueError, TypeError):
            print("\033[31mERRO! Digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return inteiro

def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO! Digite um número real válido\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrompida pelo usuário.\033[m")
            return 0          
        else:
            return real