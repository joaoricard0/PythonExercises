sexo = 'G'
while 'F' != sexo != 'M':
    sexo = input("Introduza o seu sexo: ").upper()
if sexo == 'M':
    sexo = "Masculino"
if sexo == 'F':
    sexo = "Feminino"
print(f"O seu sexo é {sexo}")
# sexo = 'G' Outra forma
# while sexo not in "MmFf":
#     sexo = input("Introduza o seu sexo: ")
# if sexo == 'M':
#     sexo = "Masculino"
# if sexo == 'F':
#     sexo = "Feminino"
# print(f"O seu sexo é {sexo}")

