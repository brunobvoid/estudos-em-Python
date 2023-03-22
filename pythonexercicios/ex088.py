#fazer um programa que ajude em palpites da mega sena, perguntar qntos jogos quer, e sortear 6 numeros de 1 a 60 de acordo a quantidade de jogos
from random import randint
import time
l = list()
jogos = list()


print('-='*20)
print('     MEGA SENA     ')
print('-='*20)
n = int(input('Quantos jogos você quer gerar? '))
t = 1

while t <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in l:
            l.append(num)
            cont += 1
        if cont >= 6:
            break
    l.sort()
    jogos.append(l[:])
    l.clear()
    t += 1
print()
print('-=' * 4, f'  SORTEANDO {n} JOGOS  ', '-=' * 4)
for i, k in enumerate(jogos):
    time.sleep(1)
    print(f'Jogo {i+1}: {k}')
