Inicio = int(input("Introduza o número inicial:"))
intervalo = int(input("Introduza o intervalo:"))
Fim = Inicio + 10 * intervalo
for i in range(Inicio,Fim,intervalo):
    print(f"{i}",end='->')
print("Terminou")