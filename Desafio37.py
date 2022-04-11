num = int(input("Digite um número para conversão: "))
print("""Escolha uma das bases de conversão:
[1] Conversor binário:
[2] Conversor octal:
[3] Conversor hexadecimal:""")
opcao = int(input("Sua opcao: "))
if opcao == 1:
    print(f"{num} convertido em binário é igual a {bin(num)}")
elif opcao == 2:
    print(f"{num} convertido em octal é igual a {oct(num)}")
elif opcao == 3:
    print(f"{num} convertido em hexadecimal é igual a {hex(num)}")
else:
    print("Opcao errada")