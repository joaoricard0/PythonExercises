Inicio = int(input("Introduza o número inicial:"))
intervalo = int(input("Introduza o intervalo:"))
Final = 0
# for i in range(Inicio,Fim,intervalo):
#     print(f"{i}",end='->')
# print("Terminou")
while Final != 10:
    print(f"{Inicio}",end='->')
    Inicio +=intervalo
    Final += 1   
print("Terminou")