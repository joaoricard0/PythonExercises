equipa = list()
jogador = dict()
golos = [] # ou list()
while True:
    jogador.clear()
    jogador['Nome'] = input("Nome do Jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['Nome']} fez? "))
    golos.clear()
    for i in range(0, partidas): 
        golos.append(int(input(f"Quantos golos fez {jogador['Nome']} na {i+1}ª partida?")))
    jogador['Golos'] = golos[:]
    jogador['Total'] = sum(golos)
    equipa.append(jogador.copy())
    while True:
        resp = input("Quer continuar? [S/N]: ").upper()[0]
        if resp in 'SN':
            break
        print("Erro! Responda apenas S ou N")
    if resp == 'N':
        break
print("*."*25)
print("cod ", end='')
for i in jogador.keys():
    print(f" {i:<17}", end='')
print()
print("*."*25)
for k, v in enumerate(equipa):
    print(f"{k:>2}  ", end='')
    for d in v.values():
        print(f" {str(d):<17}", end='')
    print()
print("*."*25)
while True:
    busca = int(input("Indique cod Jogador (999 para terminar): "))
    if busca == 999:
        break
    if busca >= len(equipa):
        print(f"Erro! Não existe jogador com código {busca}! Tente Novamente")
    else:
        print(f" -Relatório do Jogador {equipa[busca]['Nome']}:")
        for i, g in enumerate(equipa[busca]['Golos']):
            print(f"   No Jogo {i+1} fez {g} golos.")
    print("*."*25)
print("Programa Teminado")
