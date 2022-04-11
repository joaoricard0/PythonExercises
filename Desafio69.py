idadeMaior = fem = masc = 0
while True:
    print("*"*30)
    print("     Cadastre uma pessoa")
    print("*"*30)
    idade = int(input("Idade:"))
    sexo = ' '
    while sexo not in 'mf':
        sexo = input("Sexo[M/F]: ").strip().lower()[0]  
        if idade > 18:
            idadeMaior += 1
        if  sexo =='f' and idade < 20:
            fem += 1
        if sexo == 'm':
            masc +=1
    escolha = ' '
    while escolha not in 'sn':       
        escolha = input("Deseja continuar?[S/N]").strip().lower()[0]
    if escolha == 'n':
        break
print(f"Foram registadas {idadeMaior} pessoas maiores de 18 anos\nForam registados {masc} homens\nForam registadas {fem} mulheres com menos de 20 anos")