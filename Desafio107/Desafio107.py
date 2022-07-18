import moeda

for i in range(0,4):
    print("\n","*"*30)
    valor = int(input("Introduza um número: "))
    soma = moeda.aumentar(valor,10)
    subtr = moeda.diminuir(valor,15)
    mult = moeda.dobro(valor)
    div = moeda.metade(valor)
    print(f"Aumentando 10% é {soma}\nDiminuindo 15% é {subtr}\nA multiplicação do valor é {mult}\nA divisão do valor é {div}")