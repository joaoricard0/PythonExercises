salario = float(input("Qual o seu salário? " ))
if salario >= 1200:
    novoSal = salario * 1.1
    print(f"parabéns teve um aumento de 10% passando a receber {novoSal:.2f}€")
else:
    novoSal = salario * 1.15
    print(f"parabéns teve um aumento de 15% passando a receber {novoSal:.2f}€")