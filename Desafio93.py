jogador = dict()
golos = []
GolTot = 0
jogador['Nome'] = input("Nome do Jogador: ")
# jogador['Golos'] = golos
# jogador['Partidas'] = int(input(f"Quantas partidas jogou {jogador['Nome']}? "))
# for i in range(jogador['Partidas']): 
#     gol = int(input(f"Quantos golos fez {jogador['Nome']} na {i+1} partida?"))
#     golos.append(gol)
#     GolTot += gol
# jogador['Total']= GolTot
# print(jogador)
# print(f"O nome do Jogador é {jogador['Nome']}\nA lista de golos foi {jogador['Golos']}\nO total de golos foi de {jogador['Total']} golos")
# print(f"O jogador {jogador['Nome']} jogou {jogador['Partidas']} partidas")
# for i in golos:
#     print(f"Na partida {golos.index(i)+1} marcou {i} golos")
partidas = int(input(f"Quantas partidas {jogador['Nome']} fez? "))
for i in range(0, partidas): 
     golos.append(int(input(f"Quantos golos fez {jogador['Nome']} na {i+1}ª partida?")))
jogador['Golos'] = golos[:]
jogador['Total'] = sum(golos)
print("*."*20)
print(jogador)
print("*."*20)
for k,v in jogador.items():
    print(f"O {k} é {v}")
print("*."*20)
print(f"O {jogador['Nome']} jogou {len(jogador['Golos'])} partidas")
for i,v in enumerate(jogador['Golos']):
    print(f"Na partida {i+1}, fez {v} golos.")
print(f"O {jogador['Nome']} fez {jogador['Total']} golos no total")