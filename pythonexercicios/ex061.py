p = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Agora digite a razão dela: '))
t = p
c = 1
while c <= 10:
    print('{} - '.format(t), end='')
    t += r
    c += 1
print('FIM')
