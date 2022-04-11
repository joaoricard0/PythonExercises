escolha = 'S'
maior = menor = contador = soma = 0
while escolha in 'Ss':
    num = int(input("Digite um número: "))  
    soma += num
    contador += 1
    if contador == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    escolha = input("Deseja continuar?[S/N]").upper()
media = soma / contador  
print(f"Foram digitados {contador} e a sua média é de {media:.2f}")
print(f"O número maior é {maior} e o menor é {menor}")