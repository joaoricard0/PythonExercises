viagem = int(input("Qual a distância da sua viagem?"))
print(f"Você fará uma viagem de {viagem:.2f} km")
if viagem <= 200:
    preco = 0.2*viagem
else:
    preco = 0.15*viagem
    #preco = 0.2*viagem if viagem <= 200 else viagem * 0.15 - outra maneira de fazer
print(f"A sua viagem terá um custo de {preco:.2f} euros")