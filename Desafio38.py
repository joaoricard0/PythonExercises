n1 = int(input("Indique um número: "))
n2 = int(input("Indique outro número: "))
if n1 > n2:
    print(f"O número {n1} é maior que {n2}")
elif n2 > n1:
    print(f"O número {n2} é maior que {n1}")
else:
    print(f"Os números {n1} e {n2} são iguais")