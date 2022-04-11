altura = int(input("Introduza a sua altura em cm: "))
peso = float(input("Introduza o seu peso em kg: "))
imc = peso / (altura/100)**2
print(f"{imc:.1f}")
if imc < 18.5:
    print(f"O seu imc é {imc:.1f}. Você está abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print(f"O seu imc é {imc:.1f}. Você está com o peso ideal")
elif imc > 25 and imc <= 30:
    print(f"O seu imc é {imc:.1f}. Você está com sobrepeso")
elif imc > 30 and imc <= 40:
    print(f"O seu imc é {imc:.1f}. Você está com obesidade")
else:
    print(f"O seu imc é {imc:.1f}. Você está com obesidade mórbida")

# Outra forma de fazer
# if imc < 18.5:
#     print(f"O seu imc é {imc:.1f}. Você está abaixo do peso")
# elif 18.5 <= imc <= 25:
#     print(f"O seu imc é {imc:.1f}. Você está com o peso ideal")
# elif 25 < imc <= 30:
#     print(f"O seu imc é {imc:.1f}. Você está com sobrepeso")
# elif 30 < imc <= 40:
#     print(f"O seu imc é {imc:.1f}. Você está com obesidade")
# else:
#     print(f"O seu imc é {imc:.1f}. Você está com obesidade mórbida")