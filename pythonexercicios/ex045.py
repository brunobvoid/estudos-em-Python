# Jogar Pedra Papel ou Tesoura
from random import randint
from time import sleep
i = ('Pedra', 'Papel', 'Tesoura')
c = randint(0, 2)
print('=' *36)
print('Vamos jogar Pedra, Papel ou Tesoura')
print('=' *36)
while True:
    u = int(input('''Faça sua escolha |
    0 - Pedra 
    1 - Papel 
    2 - Tesoura: '''))
    print('=' * 36)
    if c == 0:
        if u == 0:
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!!')
            print('-=' * 18)
            print('EMPATE!')
            break
        elif u == 1:
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!!')
            print('-=' * 18)
            print('{} ganha de {}, você venceu!!!'.format(i[u], i[c]))
            break
        elif u == 2:
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!!')
            print('-=' * 18)
            print('{} perde pra {}, você perdeu!!!'.format(i[u], i[c]))
            break
        else:
            print('Jogada Inválida, Tente Novamente!!')
    elif c == 1:
        if u == 0:
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!!')
            print('-=' * 18)
            print('{} perde pra {}, você perdeu!!!'.format(i[u], i[c]))
            break
        elif u == 1:
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!!')
            print('-=' * 18)
            print('EMPATE!')
            break
        elif u == 2:
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!!')
            print('-=' * 18)
            print('{} ganha de {}, você venceu!!!'.format(i[u], i[c]))
            break
        else:
            print('Jogada Inválida, Tente Novamente!!')
    elif c == 2:
        if u == 0:
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!!')
            print('-=' * 18)
            print('{} ganha de {}, você venceu!!!'.format(i[u], i[c]))
            break
        elif u == 1:
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!!')
            print('-=' * 18)
            print('{} perde pra {}, você perdeu!!!'.format(i[u], i[c]))
            break
        elif u == 2:
            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!!')
            print('-=' * 18)
            print('EMPATE!')
            break
        else:
            print('Jogada Inválida, Tente Novamente!!')
print('-=' * 18)
print('O computador escolheu {}'.format(i[c]))
print('Você escolheu {}'.format(i[u]))
print('-=' * 18)