mediaIdade = 0
MaiorIdadeHomem = 0
idadeMenor = 0
NomeVelho =''
for i in range(0,4):
    nome = input("Introduza o nome: ")
    idade = int(input("Introduza a idade: "))
    sexo = input("Introduza o sexo [M/F]: ").upper()
    mediaIdade += idade/4
    if idade <= 20 and sexo == "F":
        idadeMenor +=1
    if i == 1 and sexo == "M":
        MaiorIdadeHomem = idade
        NomeVelho = nome
    if sexo == "M" and idade > MaiorIdadeHomem:
        MaiorIdadeHomem = idade
        NomeVelho = nome
    else:
        if idade > MaiorIdadeHomem:
            MaiorIdadeHomem = idade
print(f"Média de idades é de {mediaIdade}\nO homem mais velho tem: {MaiorIdadeHomem} e chama-se {nome}")
print(f"Existem {idadeMenor} mulheres com menos de 20 anos")