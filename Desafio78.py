cont = 0
maior = menor = 0
num = list()
for i in range(0,5):
    num.append(int(input(f"Introduza o {i+1}º valor: ")))
    cont += 1
    if cont == 1:
        maior = menor = num[i]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]
print(f"A lista é {num}\nO valor maior é {maior} e está na posição ", end='')
for i, v in enumerate(num):
    if v == maior:
        print(f"{i+1}...", end='')
print(f"\nO valor menor é {menor} e está na posição ",end='')
for i,v in enumerate(num):
    if v == menor:
        print(f"{i+1}...", end='')

