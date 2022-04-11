frase = input("Escreva algo:").strip().lower()
print(f"A letra a aparece {frase.count('a')} vezes")
print(f"O primeiro a aparece na posição {frase.find('a')+1}")
print(f"O ultimo a aparece na posição {frase.rfind('a')+1}")