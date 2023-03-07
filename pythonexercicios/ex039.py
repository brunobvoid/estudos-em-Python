# Ler Ano de nascimento, mostrar alistamento exercito
from datetime import date
atual = date.today().year
n = int(input('Digite aqui o ano que vc nasceu: '))
idade = atual - n
if idade < 18:
    print('Seu alistamento é daqui a {} anos'.format(18-idade))
    print('Você tem {} e deverá se alistar em {}'.format(idade, (atual + (18-idade))))
elif idade == 18:
    print('Está na hora de se alistar!!!')
elif idade > 18:
    print('Seu alistamento foi a {} anos atrás'.format(idade-18))
    print('Você tem {} anos e deveria ter se alistado em {}'.format(idade, (atual - (idade-18))))