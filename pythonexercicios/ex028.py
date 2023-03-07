#Gerar Numero de 0 a 5, usuário advinhar, errou ou acertou
import random
import time
n = random.randint(0, 5)
u = int(input('De 0 a 5, advinha em que número estou pensando? '))
print('PROCESSANDO...')
time.sleep(3)
if u == n:
    print('Parabéns vc acertou, o número era {}'.format(n))
else:
    print('ERRRRRRRRRRRRROOOOU!!!!!!!!')
    print('Eu pensei no número {}'.format(n))
