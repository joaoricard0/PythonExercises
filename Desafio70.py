total = barato = caros = cont = 0
Nomebarato = ' '
while True:
    print("*"*30)
    print("Loja do Zé")
    print("*"*30)
    nome = input("Produto: ")
    preco = int(input("Preço: "))
    cont += 1
    total += preco
    if preco > 1000:
        caros += 1
    if cont == 1 or preco < barato:
        barato = preco
        Nomebarato = nome  
    print("*"*30)
    escolha = ' '
    while escolha not in 'sn':
        escolha = input("Deseja continuar?[S/N]").strip().lower()[0]
    if escolha == 'n':
        break
print(f"O total gasto foi de {total}€\nExistem {caros} produtos acima de 1000€\nO nome do produto mais barato é {Nomebarato} e o seu preco é {barato}€")
