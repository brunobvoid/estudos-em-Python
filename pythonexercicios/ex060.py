from math import factorial
n = int(input('Digite um numero para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
while n > 0:
    print('{}'.format(n,), end='')
    print(' x' if n > 1 else ' = ', end='')
    print(f if n == 1 else ' ', end='')
    n -= 1
print('\nFIM')
