from ex108 import moeda

for i in range(0,4):
    print()
    print("*"*30)
    valor = int(input("Introduza um número: "))
    soma = moeda.aumentar(valor,10)
    subtr = moeda.diminuir(valor,15)
    mult = moeda.dobro(valor)
    div = moeda.metade(valor)
    print("*"*30)
    print(f"Aumentando 10% é {moeda.dinh(soma)}\n\nDiminuindo 15% é {moeda.dinh(subtr)}\n\nA multiplicação do valor é {moeda.dinh(mult)}\n\nA divisão do valor é {moeda.dinh(div)}")