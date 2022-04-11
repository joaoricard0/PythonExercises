temp = list()
principal = list()
maior = menor = 0
while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Peso: ")))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = input("Deseja continuar?[S/N]").upper()
    if resp not in 'S':
        break
print(f"O número de pessoas cadastradas foi de {len(principal)} pessoas")
print(f"O maior peso foi de {maior}Kg, peso de ", end='')
for p in principal:
    if p[1] == maior:
        print(f"{p[0]}", end='')
print(f"\nO menor peso foi de {menor}Kg, peso de ", end='')
for p in principal:
    if p[1] == menor:
        print(f"{p[0]}", end='')