# 4 numeros aleatórios (d6) em um dicionário colocar o dicionário em ordem, o vencedor tirou o maior numero
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador_1': randint(1, 20),
        'jogador_2': randint(1, 20),
        'jogador_3': randint(1, 20),
        'jogador_4': randint(1, 20)}
ranking = list()
print('Valores sorteados!!!')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado!')
    sleep(0.8)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} no dado!')
    sleep(0.8)
