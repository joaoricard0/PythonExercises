def area(larg, comp):
    Terreno = larg * comp
    print(f"A área do terreno {larg}m x {comp}m é de {Terreno:.1f}m2")

print("Calculo de Terrenos\n**********************")
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l,c)