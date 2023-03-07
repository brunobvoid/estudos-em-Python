#ler angulo, calcular seno, cosseno e tangente
import math
print('Vamos caucular o seno cosseno e tangente')
a = float(input('Digite aqui o valor do angulo em graus: '))
x = math.radians(a)
print('Segue os valores referentes ao angulo de {}º\n O seno é {:.5f} \n O cosseno é {:.5f} \n A tangente '
      'é {:.5f}'.format(a, (math.sin(x)), (math.cos(x)), (math.tan(x))))