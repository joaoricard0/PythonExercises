from random import randint
from time import sleep
lista = list()
jogadas = list()
print("-"*30)
print("     Raspadinha")
print("-"*30)
jogo = int(input("Quantos jogos quer? "))
for i in range(jogo):
    for k in range(0,6):
        num = randint(1,60)
        jogadas.append(num)
    lista.append(jogadas[:])
    jogadas.clear()

# tot = 1
# while tot <= jogo:
#     cont = 0
#     while True:
#         num = randint(1,60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogadas.append(lista[:])
#     lista.clear()
#     tot += 1
print('*'* 5, f" Sorteando {jogo} jogos ",'*'*5)
for i, l in enumerate(lista):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
print('*'*7,"< Fim do jogo >",'*'*7)
