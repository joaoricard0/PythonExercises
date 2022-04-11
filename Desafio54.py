from datetime import date
actual = date.today().year
somaMaior = 0
somaMenor = 0
for i in range(1,8):
    nascimento = int(input(f"Digite a data de nascimento da {i}ª pessoa: "))
    idade = actual - nascimento
    if idade >= 18:
        somaMaior += 1
        
    else:
        somaMenor += 1
print(f"Houve {somaMaior} pessoas maiores de idade")
print(f"Houve {somaMenor} pessoas menores de idade")