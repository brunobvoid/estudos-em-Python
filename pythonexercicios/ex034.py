print('Vamos calcular o seu aumento')
s = float(input('Digite aqui o valor do seu salário: R$'))
if s > 1250:
    print('O valor atualizado do seu salário é de R${:.2f} com um aumento de 10%'.format(s+(s*(10/100))))
else:
    print('O valor atualizado do seu salário é de R${:.2f} com um aumento de 15%'.format(s+(s*(15/100))))
