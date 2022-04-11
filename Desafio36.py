precoCasa = int(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
casaAnos = int(input("Em quantos anos estará a pagar a casa? "))
prestacao = precoCasa/(casaAnos*12)
sobraSal = salario * 0.3
if prestacao > sobraSal:
    print("Lamentamos mas o seu emprestimo não pode ser aprovado")
else:
    print("Parabéns! O seu emprestimo foi aprovado!")
print(f"Valor a pagar mensal é de {prestacao}")
print(f"Valor máximo que pode pagar é de {sobraSal}")