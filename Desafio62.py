# for i in range(Inicio,Fim,intervalo):
#     print(f"{i}",end='->')
# print("Terminou")
Inicio = int(input("Introduza o número inicial:"))
intervalo = int(input("Introduza o intervalo:"))
termo = Inicio
mais = 10
total = 0
cont = 1
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo}",end='->')
        termo +=intervalo
        cont += 1
    print("pausa") 
    mais = int(input("Quantos números quer mostrar a mais?"))
print(f"Terminou\nFinalizou com {total} números mostrados")
