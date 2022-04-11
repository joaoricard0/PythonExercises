nota500 = nota200 = nota100 = nota50 = nota20 = nota10 = nota5 = 0
print("="*30)
print("         Banco do Zé")
print("="*30)
valor = int(input("Qual o valor que deseja levantar? "))
print(f"O valor de {valor}€ deu:")
while valor != 0:   
    if valor >= 500:
        nota500 += 1
        valor -= 500
    else:
        if valor >=200:
            nota200 +=1
            valor -= 200
        else:
            if valor >=100:
                nota100 += 1
                valor -= 100
            else:
                if valor >= 50:
                    nota50 += 1
                    valor -= 50
                else:
                    if valor >= 20:
                        nota20 += 1
                        valor -= 20
                    else:
                        if valor >= 10:
                            nota10 += 1
                            valor -= 10
                        else:
                            if valor >= 5:
                                nota5 += 1
                                valor -= 5
                                print(f"{nota5} notas de 5€")
if nota500 >= 1:
    print(f"{nota500} notas de 500€")
if nota200 >= 1:
    print(f"{nota200} notas de 200€")
if nota100 >= 1:
    print(f"{nota100} notas de 100€")
if nota50 >= 1:
    print(f"{nota50} notas de 50€")
if nota20 >= 1:
    print(f"{nota20} notas de 20€")
if nota10 >= 1:
    print(f"{nota10} notas de 10€")
print("="*30)
print("Obrigado, volte sempre ao Banco do Zé! Tenha um bom dia!")