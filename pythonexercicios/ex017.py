#ler cateto oposto e adjacente, calcular hipotenusa
import math
print('Vamos calcular a hipotenusa')
co = float(input('Digite aqui o valor do cateto oposto: '))
ca = float(input('Digite aqui o valor do cateto adjacente: '))
print('O valor da hipotenusa é {:.2f}'.format(math.hypot(co, ca)))
