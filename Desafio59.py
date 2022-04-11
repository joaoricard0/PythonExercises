from time import sleep
num1 = int(input("Introduza o primeiro número:"))
num2 = int(input("Introduza o segundo número:"))
menu = 0
while menu != 5:
    print("""Menu:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair Programa""")
    menu = int(input("Sua opção: "))
    if menu == 1:
        print(f"{num1} + {num2} = {num1+num2}")
    elif menu == 2:
        print(f"{num1} x {num2} = {num1*num2}")
    elif menu == 3:
        if num1 < num2:
            print(f"O {num1} é menor que o {num2}")
        else:
            print(f"O {num1} é maior que o {num2}")
    elif menu == 4:
        print("Informe de novo os valores:")
        num1 = int(input("Primeiro número:"))
        num2 = int(input("Segundo número:"))
    elif menu == 5:
        print("Finalizando..")
        sleep(2)
    else:
        print("Opção inválida. Tente novamente")
print("Programa terminado")