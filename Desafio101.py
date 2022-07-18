def vota(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 17:
        return f"Com {idade} anos: Não pode votar!"
    elif 18 <= idade <= 65:
        return f"Com {idade} anos: O Voto é obrigatório!"
    else:
        return f"Com {idade} anos: O Voto é opcional"

voto = int(input("Em que ano nasceu? "))
print(vota(voto))

    