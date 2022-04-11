Qtd = res = num = 0
while num != 999:
    num = int(input("Digite um número: "))
    if num != 999:
        res += num
        Qtd +=1
print(f"Foram digitados {Qtd} números e a sua soma é {res}")