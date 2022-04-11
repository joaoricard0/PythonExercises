from math import pow,sqrt,hypot

cat1 = float(input("Introduza o valor do cateto 1: "))
cat2 = float(input("Introduza o valor do cateto 2: "))

# hipot = sqrt(pow(cat1,2) + pow(cat2,2))
hipot = hypot(cat1,cat2)

print(f"A Hipotenusa dos catetos {cat1} e {cat2} é de {hipot:.2f}")