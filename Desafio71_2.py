print("="*30)
print("         Banco do Zé")
print("="*30)
valor = int(input("Qual o valor a levantar? "))
total = valor
nota = 500
totalNotas = 0
while True:
    if total >= nota:
        total -= nota
        totalNotas += 1
    else:
        if totalNotas > 0:
            print(f"Total de {totalNotas} notas de {nota}€")
        if nota == 500:
            nota = 200
        elif nota == 200:
            nota = 100
        elif nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        totalNotas = 0
        if total == 0:
            break
print("="*30)
print("Obrigado pela sua preferência. Volte sempre ao Banco do Zé")