Algo = input("Introduza algo: ")
print("O tipo primitivo é ",type(Algo))
print("É uma palvra? ", Algo.isalpha())
print("É um número? ", Algo.isnumeric())
print("Está em maiúsculas? ", Algo.isupper())
print("Está em minusculas? ", Algo.islower())
print("Só tem espaço? ", Algo.isspace())
print("É alfanumérico? ", Algo.isalnum())
print(f"Está capitalizada? {Algo.istitle()}") #exemplo convertido com format