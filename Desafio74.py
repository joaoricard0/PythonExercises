from random import choice, randint
# cont = menor = maior = 0
# for i in range(0,5):
#     numAle = (randint(1,10))
#     num = (numAle)
#     cont += 1
#     if cont == 1:
#         numAle = maior = menor
#     else:
#         if numAle < menor:
#             menor = numAle
#         if numAle > maior:
#             maior = numAle
#     print(num, end=' ')
# print(f"\nO número maior é {maior}\nO número menor é {menor}")

numAle = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print("O valores escolhidos ao acaso foram: ", end='')
for n in numAle:
    print(f"{n}", end=' ')
print(f"\nO número maior é {max(numAle)}\nO número menor é {min(numAle)}")