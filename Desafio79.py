lista = list()
while True:
    num =int(input("Introduza um valor: "))
    if num not in lista:
        print("Valor adicionado!")
        lista.append(num)
    else:
        print("Valor duplicado, não foi adicionado")
    resp = input("Deseja continuar?[S/N]").upper()
    if resp == 'N':
        break
lista.sort()
print(lista)
