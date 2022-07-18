def factorial(n, show=False):
    """
    -> Calcula o factorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do factorial de um número n.
    """
    f = 1
    for c in range(n,0,-1):
        if show == True:
            print(f"{c}", end='')
            print(' x ' if c > 1 else ' = ', end='')
        f *= c
    return f


print(factorial(5,show=False))
help(factorial)