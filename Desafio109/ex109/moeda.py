def aumentar(preco = 0, taxa = 0, formato = False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else dinh(res)
def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - (preco * taxa / 100)
    return res if not formato else dinh(res)
def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if not formato else dinh(res)
def metade(preco = 0, formato = False):
    res = preco /2
    return res if formato is False else dinh(res)

def dinh(preco = 0, euro = '€'):
    return f"{preco:.2f}{euro}".replace(".", ",")

