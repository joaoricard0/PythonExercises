from datetime import date
registo = dict()
atual = date.today().year

registo['Nome'] = str(input("Nome: "))
registo['Nasc.'] = int(input("Ano de Nascimento: "))
registo['CTPS'] = int(input("Carteira de tranbalho (0 se não tiver):"))
idade = atual - registo['Nasc.']
if registo['CTPS'] != 0:
    registo['Contrat'] = int(input("Ano de Contratação: "))
    registo['Salario'] = int(input("Salário: "))
    registo['Reforma'] = idade + ((registo['Contrat'] + 36) - atual)
print("*."*30)
print(f"Nome é {registo['Nome']}\nIdade é de {idade} anos\nO CTPS é {registo['CTPS']}")
if registo['CTPS'] != 0:
    print(f"O ano de contratação foi em {registo['Contrat']}\nO salário é de {registo['Salario']}€\nA idade de reforma será com {registo['Reforma']} anos, no ano de {registo['Reforma']-idade+atual}")
for k,v in registo.items():
    print(f" - {k} com {v}")