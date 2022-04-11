from random import randint
from time import sleep
numUt = int(input("Adivinhe o número:"))
num = randint(0,5)
print("A processar...")
sleep(2)
if num == numUt:
    print("Parabéns, acertou!!")
else:
    print("Tente novamente")
    print(f"O número era {num}")