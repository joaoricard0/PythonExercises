from time import sleep
def maior(*num):
    maior = 0
    print(f"Foram analisados {len(num)} números sendo eles ", end='')
    for i in num:
        if i == 0:
            maior = i
        elif i > maior:
            maior = i
        print(f"{i} ", end='')
        sleep(1)
    print(f"e o maior sendo {maior}")


maior(6,78,54,69,23,14,17,25,19,26,48)

maior(2,3,8)

maior(4,9,7,6,8)

maior(6,3,12,15,42,28)