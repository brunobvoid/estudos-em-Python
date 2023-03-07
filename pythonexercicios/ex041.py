# Ler Ano de nascimento do atleta e mostrar categoria até 9 MIRIM até 14 INFANTIL até 19 JUNIOR até 20 SENIOR acima MASTER
from datetime import date
atual = date.today().year
ano = int(input('Digite aqui o ano do seu nascimento: '))
idade = atual - ano
if idade <= 9:
    print('O atleta tem {} anos e está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e está na categoria INFANTIL'.format(idade))
elif idade <=19:
    print('O atleta tem {} anos e está na categoria JUNIOR'.format(idade))
elif idade <=25:
    print('O atleta tem {} anos e está na categoria SENIOR'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria MASTER'.format(idade))
