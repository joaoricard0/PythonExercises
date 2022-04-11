maior = coluna = pares = 0
matrix = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))
print("*"*20)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matrix[l][c]:^5}]", end='')
        if matrix[l][c] % 2 == 0:
            pares += matrix[l][c]      
    print()
print("*"*20)
print(f"A soma dos valores pares é {pares}")
#coluna = matrix[0][2] + matrix [1][2] + matrix[2][2]
for l in range(0,3):
    coluna += matrix[l][2]
print("*"*20)
print(f"A soma dos valores da terceira coluna é {coluna}")
for c in range(0,3):
    if c == 0:
        maior = matrix[1][c]
    elif matrix[1][c] > maior:
            maior = matrix[1][c]
print(f"O maior valor da segunda linha é {maior}")