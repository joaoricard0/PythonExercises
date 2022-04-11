r1 = float(input("Introduza o comprimento da primeira recta: "))
r2 = float(input("Introduza o comprimento da segunda recta: "))
r3 = float(input("Introduza o comprimento da terceira recta: "))
if (r1 + r2) < r3 and (r3 + r2) < r1 and (r1 + r3) < r2:
    print("Estas retas não dão para fazer um triangulo")
else:
    print("Estas retas dão para fazer um triangulo")
    if r1 == r2 == r3:
        print("É um triangulo Equilatero")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("É um triangulo Isósceles")
    else:
        print("É um triangulo Escaleno")