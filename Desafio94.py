from time import sleep
lista = list()
pessoa = {}
#fem = idadeMed =cont = 0
# sexo = ''
# while True:
#     nome = input("Nome: ")
#     sexo = input("Sexo[M/F]: ").lower()
#     if sexo != 'f' or sexo != 'm':       
#         print("Caracter errado, tente novamente")
#         sexo = input("Sexo[M/F]: ").lower()
#     idade = int(input("Idade: "))
#     pessoa['Nome'] = nome
#     pessoa['Sexo'] = sexo
#     pessoa['Idade'] = idade
#     lista.append(pessoa.copy())
#     cont += 1
#     resp = input("Deseja continuar?[S/N]").lower()
#     if resp == 'n':
#         print("Terminando programa...")
#         break
# print(f"Foram registadas {cont} pessoas")
# print(f"As mulheres registadas foram ", end='')
# for i in lista:
#     idadeMed +=i['Idade']
#     if i['Sexo'] == 'f':
#         fem += 1
#         print(f"{i['Nome']} ", end='')
# print(f"sendo no total {fem} mulheres")
# print(f"A média de idades é de {idadeMed/cont} anos")
# print("As pessoas com idade acima da média foram:")
# for i in lista:
#     if i['Idade'] >= (idadeMed/cont):
#         print(f"Nome: {i['Nome']}, Sexo: {i['Sexo']} , Idade: {i['Idade']};")
# sleep(1)
# print("Programa terminado,até breve!")
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = input("Nome: ")
    while True:
        pessoa['Sexo'] =input("Sexo [M/F]:").upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print("Erro! Digite apenas M ou F")
    pessoa['Idade'] = int(input("Idade: "))
    soma += pessoa['Idade']
    lista.append(pessoa.copy())
    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in 'SN':
            break
        print("Erro! responda apenas S ou N")
    if resp == 'N':
        break
print("*."*20)
print(f"Ao todo temos {len(lista)} pessoas registadas")
media = soma / len(lista)
print(f"A media de idades foi de {media} anos")
print(f"As mulheres registadas foram ", end='')
for p in lista:
    if p['Sexo'] in 'Ff':
        print(f"{p['Nome']} ", end='')
for p in lista:
    if p['Idade'] >= media:
        print("    ", end='')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print("Programa encerrando...")
sleep(1)
print("Programa terminado,até breve!")