l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l*a
t = area/2
print('A area da parede é {:.2f}m² e você vai precisar de {:.2f}l de tinta'.format(area, t))
