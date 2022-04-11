nome = input("Introduza um nome: ").strip()

print(f"O seu nome em maiusculas é {nome.upper()} ")
print(f"O seu nome em minusculas é {nome.lower()}")
print(f"O seu nome tem {len(nome)} letras")
divid = nome.split()
print(f"O seu nome primeiro é {(divid[0])} e ele tem {len(divid[0])} letras")
print(f"O seu primeiro nome tem {nome.find(' ')} letras")