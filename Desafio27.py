nome = input("Indique um nome: ").strip()
name = nome.split()


print(f"Primeiro nome: {name[0].capitalize()}\nÚltimo nome: {name[len(name)-1].capitalize()}")
