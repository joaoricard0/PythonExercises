nota1 = float(input("Introuduza a primeira nota: "))
nota2 = float(input("Introuduza a segunda nota: "))
nota3 = float(input("Introuduza a terceira nota: "))
nota4 = float(input("Introuduza a quarta nota: "))
nota5 = float(input("Introuduza a quinta nota: "))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
if media < 5:
    print(f"Lamento mas com a nota {media:.2f}, você foi reprovado")
elif media >=5 and media <= 6.9:
    print(f"Com a nota {media:.2f}, você está em recuperação")
else:
    print(f"Parabéns! com a nota {media:.2f}, você foi aprovado!")
