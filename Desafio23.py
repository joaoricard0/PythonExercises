num = int(input("introduza um número de 0 a 9999: "))
uni = num //1%10
dez = num//10%10
cen = num//100%10
mil = num//1000%10
print(f"Analisando o numero {num}\nUnidades: {uni}\nDezenas: {dez}")
print(f"Centenas: {cen}\nMilhares: {mil}")