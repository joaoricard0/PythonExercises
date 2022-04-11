lista = [[],[]]
num = 0
for i in range(0,7):
    num = int(input(f"Introduza o {i+1}º valor: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f"Os números digitados foram {lista}")
print(f"Os números pares foram {lista[0]}")
print(f"Os números impares foram {lista[1]}")
