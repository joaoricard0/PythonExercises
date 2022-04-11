from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
for i in range(0,4):
    jogo[f'Jogador {i+1}'] = randint(1,6)
for k,v in jogo.items():
    print(f"O {k} tirou {v}.")
    sleep(1)
    ranking = list()
print("*-"*20)
print("** Ranking de Jogadores **")
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f"{i+1}º Lugar: {v[0]} com {v[1]}.")
    sleep(1)