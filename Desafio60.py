# from math import factorial
# num = int(input("Introduza um número: "))
# f = factorial(num)
# print(f"O factorial de {num} é {f}")

# num = int(input("Introduza um número: "))
# contagem = num
# factorial = num
# while contagem != 1:
#     contagem -=1
#     factorial *= contagem
# print(f"O factorial de {num} é {factorial}")

# num = int(input("Introduza um número: "))
# cont = num
# fact = 1
# print(f"Calculando {num}! = ", end='')
# while cont > 0:
#     print(f"{cont}", end='')
#     print(' x ' if cont > 1 else ' = ', end='')
#     fact *= cont
#     cont -=1
# print(f"{fact}")
num = int(input("Introduza um número: "))
print(f"Calculando {num}! = ", end='')
print(f"{num} x ", end='')
for i in range(num-1,0,-1):
    print(f"{i}", end='')
    print(' x ' if i > 1 else ' = ', end='')
    num *= i
print(f"{num}")