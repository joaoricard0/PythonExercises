from datetime import date
ano = int(input("Indique o seu ano de nascimento: "))
idade = date.today().year - ano
if  idade <= 17:
    print(f"Ainda falta {18-idade} anos para o alistamento")
elif idade >= 18 and idade <= 20:
    print("Esta na altura de se alistar")
else:
    print(f"A sua altura para alistamento já passou a {idade-20} anos")