# Emprestimo, LER valor da casa, salário do comprador, em qntos anos vai pagar, calcular prestação e não pode exceder 30% do salário
print('Olá vamos calcular o valor das parcelas do Empréstimo"')
casa = float(input('Digite aqui o valor total do imóvel em reais: R$'))
s = float(input('Agora me informa sua renda mensal por favor: R$'))
ano = int(input('Em quantos anos pretende pagar? '))
p = casa / (ano * 12)
if p > s * 30/100:
    print('O valor da parcela é {:.2f}'.format(p))
    print('O empréstimo não foi aprovado pois ultrapassou 30% do valor da sua renda mensal')
else:
    print('O valor da parcela será {:.2f}'.format(p))
    print('Parabéns o empréstimo foi APROVADO')

