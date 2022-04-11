lista = list()
media = 0
while True:
    Nome = input("Nome: ")
    Nota1 = float(input("Nota 1: "))
    Nota2 = float(input("Nota 2: "))
    media = (Nota1 + Nota2)/2
    lista.append([Nome,[Nota1,Nota2], media])
    resp = input("Quer continuar? [S/N]").upper()
    if resp not in 'S':
        break
print("*"*30)
print(f"{'Nº':<5}{'NOME':<10}{'MÉDIA':>10}")
print("-"*25)
for i,a in enumerate(lista):
    print(f"{i:<4} {a[0]:<10} {a[2]:>8.1f}")
while True:
    print("*"*30)
    opcao = int(input("Qual aluno pretende mostrar notas? [999] -> Stop: "))
    if opcao == 999:
        print("Terminado o programa")
        break
    if opcao <= len(lista) - 1:
        print(f"Notas de {lista[opcao][0]} são {lista[opcao][1]}")