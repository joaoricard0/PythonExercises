lista = list()
while True:
    lista.append(int(input("Introduza um valor: ")))
    resp = input("Deseja continuar? [S/N]")
    if resp not in 'Ss':
        break
print(f"A lista é {lista}")
print(f"Foram digitados {len(lista)} valores")
lista.sort(reverse=True)
print(f"A lista em ordem decrescente fica {lista}")
if 5 in lista:
    print("O número 5 foi encontrado")
else:
    print("O número 5 não foi encontrado")