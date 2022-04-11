n = 1
while True:
    cont = 0
    n = int(input("Quer a tabuada de que valor? "))
    if n < 0:
        break
    while cont <= 10:
        res = cont * n
        print(f"{n} x {cont} = {res}")
        cont += 1     
print("Fim")
