from datetime import date
ano = int(input("Introuduza o seu ano de nascimento: "))
idade = date.today().year - ano
if idade <= 9:
    print("A sua categoria é Mirim")
elif idade <= 14:
    print("A sua categoria é Infantil")
elif idade <= 19:
    print("A sua categoria é Junior")
elif idade <= 25:
    print("A sua categoria é Sênior")
else:
    print("A sua categoria é Master")