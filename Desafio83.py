express = input("Introduza a expressão: ")
container = []
for simb in express:
    if simb == '(':
        container.append(simb)
    elif simb == ')':
        if len(container) > 0:
            container.pop()
        else:
            container.append(simb)
            break
if len(container) == 0:
    print("A sua expressão está válida")
else:
    print("A sua expressão está inválida")
print(container)