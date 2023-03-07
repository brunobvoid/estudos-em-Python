v = int(input('Qual a distância da viagem em km? '))
if v <= 200:
    print('O valor da passagem é R${:.2f}'.format(v*0.50))
else:
    print('O valor da passagem é R${:.2f}'.format(v*0.45))