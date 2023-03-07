import random
n = random.randint(0, 10)
print('Pensei em um número de 0 a 10, consegue advinhar qual foi?')
a = False
c = 0
while not a:
    u = int(input('Qual o seu palpite? '))
    c += 1
    if u == n:
        a = True
    else:
        if u < n:
            print('Errou, é um pouco mais!!')
        else:
            print('Errou, é um pouco menos!!')
print('Parabéns vc acertou, o número era {}, e levou {} tentativas.'.format(n, c))
