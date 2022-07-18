def ficha(nome='',golos=0):
    if nome == '':
        nome = '<desconhecido>'
    if golos != int:
        golos = 0
    print(f"O jogador {nome} fez {golos} golo(s) no campeonato")

nomeJog = input("Nome do Jogador: ")
goloJog = input("Número de Golos: ")
ficha(nomeJog,goloJog)

#Segunda maneira de executar
# def ficha(jog='<desconhecido>', golo=0):
#     print(f"O jogador {jog} fez {golo} golo(s) no campeonato.")

# n = str(input("Nome do Jogador: "))
# g = str(input("Número de Golos: "))
# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0
# if n.strip() == '':
#     ficha(gol=g)
# else:
#     ficha(n,g)