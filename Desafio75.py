# conta_9 = 0
# num1 = int(input("Introduza o primeiro número: "))
# num2 = int(input("Introduza o segundo número: "))
# num3 = int(input("Introduza o terceiro número: "))
# num4 = int(input("Introduza o quarto número: "))
# tupla = (num1,num2,num3,num4)
# pares = 0
# n3 = 0
# for i in range(0, len(tupla)):
#     if tupla[i] == 9:
#         conta_9 +=1
#     if tupla[i]% 2 == 0:
#         pares += 1
#     if tupla[i] == 3:
#         n3 += 1
# print(f"A) O número 9 apareceu {conta_9} vezes")
# if n3 > 0:
#     print(f"B) O número 3 foi digitado na {tupla.index(i)+1}ª posição")
# else:
#     print(f"B) O número 3 não foi digitado em nenhuma posição")
# print(f"C) O números pares foram {pares}")

num = (int(input("Introduza o primeiro número: ")),int(input("Introduza o primeiro número: ")),
int(input("Introduza o primeiro número: ")),int(input("Introduza o primeiro número: ")))
print(f"Digitou os números {num}")
if num.count(9) == 0:
    print("O número 9 não apareceu nenhuma vez")
else:
    print(f"O número 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O número 3 apareceu na {num.index(3)+1}ª posição")
else:
    print("O número 3 não foi digitado em nenhuma posição")
print("Os valores pares são o ", end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end= ' ')