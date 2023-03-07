# numero primo
t = 0
n = int(input('Digite aqui o numero: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if t == 2:
    print('\nÉ PRIMO!')
else:
    print('\nNão é primo!')