primo = int(input("Introduza um número:"))
tot = 0
for i in range(1,primo + 1):
    if primo % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f"{i} ",end='')
print(f"- O número {primo} foi divisivel {tot} vezes logo ", end='')
if tot == 2:
    print(f"o número {primo} é primo")
else:
    print(f"o número {primo} não é primo")