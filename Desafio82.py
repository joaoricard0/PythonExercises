pares = list()
impares = list()
lista = list()
while True:
    lista.append(int(input("Introduza um Valor: ")))
    resp = input("Deseja continuar? [S/N]")
    if resp not in 'Ss':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v) 
    else:        
        impares.append(v)      
print(f"A sua lista é {lista}")
print(f"A sua lista de pares é {pares}")
print(f"A sua lista de impares é {impares}")