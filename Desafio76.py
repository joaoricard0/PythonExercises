Listagem = ('Processador',150,
'Memória RAM',120,
'Disco SSD',50,
'Caixa Pc',55,
'Placa Gráfica',285,
'Fonte Alimentação',45,
'Disco HDD',45,
'Motherboard',95,
'Portátil',750,
'Rato',10,
'Monitor',130,
'Teclado',20)
print("*"*30)
print("      Listagem de Preços")
print("*"*30)
for i in range(0, len(Listagem)):
    if i % 2 == 0:
        print(f"{Listagem[i]:.<22}", end= ' ')
    else:
        print(f"{Listagem[i]:>6.2f}€")
