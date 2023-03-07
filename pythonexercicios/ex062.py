# melhorar o 61
p = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Agora digite a razão dela: '))
t = p
c = 1
to = 0
m = 10
while m != 0:
    to = to + m
    while c <= to:
        print('{} - '.format(t), end='')
        t += r
        c += 1
    print('PAUSA')
    m = int(input('Quantos termos mais você quer mostrar? '))
print('Progressão finalizada com {} termos mostrados!'.format(to))
