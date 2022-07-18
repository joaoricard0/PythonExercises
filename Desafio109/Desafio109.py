from ex109 import moeda


print("*"*30)
valor = float(input("Introduza um número: "))
soma = moeda.aumentar(valor,10)
subtr = moeda.diminuir(valor,15)
mult = moeda.dobro(valor)
div = moeda.metade(valor)
print(f"Aumentando 10% é {moeda.dinh(soma)}")
print(f"Diminuindo 15% é {moeda.dinh(subtr)}")
print(f"A multiplicação do valor é {moeda.dinh(mult)}")
print(f"A divisão do valor é {moeda.dinh(div)}")