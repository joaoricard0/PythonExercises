def dobro(preco = 0):
    res = preco * 2
    return res
def metade(preco = 0):
    res = preco /2
    return res

def dinh(preco = 0, euro = '€'):
    return f"{preco:.2f}{euro}".replace(".", ",")

def resumo(valor = 0, perMais = 0, perMenos = 0):
    soma = valor + (valor * perMais / 100)
    subtr = valor - (valor * perMenos / 100)
    mult = dobro(valor)
    div = metade(valor)
    print("*"*40)
    print(f"{'RESUMO TOTAL':^40}")
    print("*"*40)
    print(f"Aumento de {perMais}%: \t{dinh(soma):>16}")
    print(f"Diminuição de {perMenos}%: \t{dinh(subtr):>16}")
    print(f"Dobro do valor: \t{dinh(mult):>16}")
    print(f"A divisão do valor: \t{dinh(div):>16}")
    print("*"*40)

