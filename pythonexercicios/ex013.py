nome = input('Digite seu nome: ')
s = float(input('Agora digite o valor do seu salário atual: R$'))
sa = s + (s*15/100)
print('Parabéns {} você recebeu um aumento e agora seu salário é {}'.format(nome, sa))