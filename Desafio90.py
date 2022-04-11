Aluno = dict()
Aluno['Nome'] = str(input("Nome: "))
Aluno['Média'] = float(input(f"Média de {Aluno['Nome']}: "))
print(f"O nome do Aluno é {Aluno['Nome']}\nA nota média de {Aluno['Nome']} é de {Aluno['Média']}")
if Aluno['Média'] < 10:
    Aluno['Situação'] = 'Reprovado'
    print(f"A situação de {Aluno['Nome']} é de {Aluno['Situação']}")
else:
    Aluno['Situação'] = 'Aprovado'
    print(f"A situação de {Aluno['Nome']} é de {Aluno['Situação']}")
# for k, v in Aluno.items():
#     print(f" - {k} é de {v}")