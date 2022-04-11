print(f"{' LOJA DO CATANO ':=^40}")
preco = float(input("Introduza o valor do produto: "))
pagamento = input("Qual o metodo de pagamento? ")
if pagamento == "dinheiro" or pagamento == "cheque":
    print(f"Com desconto de 10% o preço a pagar é de {preco - preco*0.10}€")
elif pagamento == "cartao":
    print(f"Com desconto de 5% o preço a pagar é de {preco - preco*0.05}€")
elif pagamento == "2x":
    print(f"O preço a pagar é de {preco}€")
elif pagamento == "3x":
    print(f"Com juros de 20% o preço a pagar é de {preco + preco*0.20}€")
else:
    print("dados inválidos")