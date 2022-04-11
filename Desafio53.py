frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for i in range(len(junto)-1, -1,-1):
    inverso +=junto[i]
print(f"O inverso de {junto} é {inverso}")
if junto == inverso:
    print("A frase é palindroma")
else:
    print("A frase não é palindroma")
