from random import randint
from secrets import choice
contUser = 0
contPc = 0
while not contPc > 0:
    print("="*30)
    print("Vamos Jogar Par ou impar")
    user = int(input("Diga um número: "))
    parimpar = input("Par ou ímpar[P/I]: ").upper()
    print("="*30)
    comp = randint(0,10)
    PC = choice(['I','P'])
    res = user + comp
    print(f"Jogou {user} e o computador {comp}. A soma é de {res}")
    if res % 2 == 0:
        par = res
        if parimpar == 'P':
            PC = 'I'
            print(f"{res} deu Par. Ganhou!")
            contUser +=1
            print("Vamos jogar novamente...")
        elif parimpar == 'I':
            PC = 'P'
            print(f"{res} deu Par. Perdeu!")
            contPc += 1
    if res % 2 == 1:
        impar = res
        if parimpar == 'I':
            PC = 'P'
            print(f"{res} deu impar. Ganhou!")
            contUser +=1
            print("Vamos jogar novamente...")
        elif parimpar == 'P':
            PC = 'I'
            print(f"{res} deu impar. Perdeu!")
            contPc += 1      
print(f"Terminou, conseguiu ganhar {contUser} vezes!!")
