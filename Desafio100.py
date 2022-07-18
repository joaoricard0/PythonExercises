from time import sleep
from random import randint
def sorteia(lista):
    for cont in range(0,5):
        n = randint(1,50)
        lista.append(n)
        print(f"{n} ", end='')
        sleep(0.5)
    print("fim")       
def somaPart(lista):
    par = 0
    for i in lista: 
        if i % 2 == 0:
            par += i
    print(f"A soma dos valores é de {par}")
numeros = list()
sorteia(numeros)
somaPart(numeros)
