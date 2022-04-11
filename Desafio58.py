from random import randint
from time import sleep
num = randint(0,10)
numUt = 1
tentativas = 0
while numUt != num:
    numUt = int(input("Adivinhe o número [0-10]: "))
    print("A processar...")
    sleep(2)
    tentativas += 1
    if num == numUt:
        print(f"Parabéns, acertou!! Foram precisas {tentativas} tentativas para acertar!")
    else:
        if num == numUt -1 or num == numUt +1:
            print("Está perto")