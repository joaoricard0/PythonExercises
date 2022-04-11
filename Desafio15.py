Carro = input("Qual o carro que usou? ").lower()
km = float(input("Quantos Km fez? "))
dia = int(input("Quantos dias de aluguer? "))
if Carro == "mercedes" or Carro == "1":
    custo = 60*dia + 0.15*km
elif Carro == "bmw" or Carro == "2":
    custo = 70*dia + 0.20*km
elif Carro == "tesla" or Carro == "3":
    custo = 80*dia + 0.30*km
elif Carro == "toyota" or Carro == "4":
    custo = 30*dia + 0.10*km
elif Carro == "renault" or Carro == "5":
    custo = 25*dia + 0.10*km
else:
    print("Dados inválidos")
IVA = custo * 0.23
custoFinal = custo + IVA
print(f"O total é de: {custo:.2f}€\nIVA: {IVA:.2f}€\ncusto final a pagar é de {custoFinal:.2f}€")