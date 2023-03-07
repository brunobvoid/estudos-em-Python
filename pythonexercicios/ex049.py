# tabuada usando for
print('Tabuada de Multiplicação')
n = int(input('Digite aqui o número: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, (n * c)))
print('FIM')
