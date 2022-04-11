cont = 0
OrdList = list()
for i in range(0,5):
    num =int(input(f"Introduza o {i+1}º valor: "))
    if i == 0 or num > OrdList[-1]:
        OrdList.append(num)
        print("Valor adicionado ao fim da lista...")
    else:
        pos = 0
        while pos < len(OrdList):
            if num <= OrdList[pos]:
                OrdList.insert(pos,num)
                print(f"Adicionado na {pos+1}ª posição da lista...")
                break
            pos += 1
print("-=" *20)
print(f"O valores por ordem são {OrdList}")
