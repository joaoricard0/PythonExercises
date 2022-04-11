from re import A


n1 = int(input("Introduza o primeiro número: "))
n2 = int(input("Introduza o segundo número: "))
n3 = int(input("Introduza o terceiro número: "))
# if n1 < n2 and n1 < n3 and n2 < n3:
#     print(f"O menor número é {n1} e o maior é {n3}")
# elif n1 > n2 and n1 > n3 and n2 > n3:
#     print(f"O menor número é {n3} e o maior é {n1}")
# elif n1 < n2 and n1 < n3 and n2 > n3:
#     print(f"O menor número é {n1} e o maior é {n2}")
# elif n1 < n2 and n1 > n3 and n2 > n3:
#     print(f"O menor número é {n3} e o maior é {n2}")
# elif n1 > n2 and n1 < n3 and n2 < n3:
#     print(f"O menor número é {n2} e o maior é {n3}")
# else:
#     print(f"O menor número é {n2} e o maior é {n1}")
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f"O menor número é {menor} e o maior é {maior}")