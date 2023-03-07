s = c = m = d = 0
a = 'S'
while a in 'Ss':
    n = int(input('Digite um valor: '))
    c += 1
    s += n
    if c == 1:
        m = d = n
    else:
        if n > m:
            m = n
        if n < d:
            d = n
    a = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
me = s / c
print('-'*30)
print('''Você digitou {} números
A média entre eles é {}
O maior número digitado foi {}
O menor número digitado foi {}'''.format(c, me, m, d))

