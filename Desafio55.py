maior = 0
menor = 0
for i in range(1,6):
    peso = float(input(f"Introduza o peso da {i}ª pessoa: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso é de {maior}\nO menor peso é de {menor}")
        