s = 0
cont = 0
for i in range(0,6):
    num = int(input("Introduza um número:"))
    if num % 2 == 0:
        s += num
        cont += 1
print(f"A soma entre os {cont} valores pares é {s}")