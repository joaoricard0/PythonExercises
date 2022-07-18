from time import sleep
def contador(ini,fim,passo): 
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("*"*30)
    print(f"Contagem de {ini} até {fim} de {passo} em {passo}")
    if ini > fim:
        while ini >= fim:
            print(f"{ini} ", end='')
            sleep(0.5)
            ini -= passo
        print("Fim")
    else:
        while ini <= fim:
            print(f"{ini} ", end='')
            sleep(0.5)
            ini += passo
        print("Fim")
print("Contagem personalizada")
ini = int(input("Número Inicial: "))
fim = int(input("Número Final: "))
passo = int(input("Número a passo: "))
contador(1,10,1)
contador(10,0,2)
contador(ini,fim,passo)

