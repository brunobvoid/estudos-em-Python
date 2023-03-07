#ler Velocidade, testar se mais de 80kmh multa 7 por km excedido
va = float(input('A que velocidade o carro estava em km/h? '))
if va > 80:
    print('Você foi multado em R${}'.format((va-80)*7))
else:
    print('Tenha um bom dia e diriga com cuidado!')