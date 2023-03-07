print('Escolha 3 números diferentes!')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais outro número: '))
# solução alternativa
'''if n1 > n2 and n1 > n3:
    print('{} é o maior'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} é o maior'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} é o maior'.format(n3))
if n1 < n2 and n1 < n3:
    print('{} é o menor'.format(n1))
if n2 < n1 and n2 < n3:
    print('{} é o menor'.format(n2))
if n3 < n2 and n3 < n1:
    print('{} é o menor'.format(n3))'''
# verif menor
m = n1
if n2 < n1 and n2 < n3:
    m = n2
if n3 < n1 and n3 < n2:
    m = n3
# verif maior
m2 = n1
if n2 > n1 and n2 > n3:
    m2 = n2
if n3 > n1 and n3 > n2:
    m2 = n3
print('O menor valor é {}'.format(m))
print('O maior valor é {}'.format(m2))
