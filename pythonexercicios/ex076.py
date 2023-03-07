#tupla unica com produtos e preços, mostrar de forma tabular
l = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
     'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 12.30, 'Livro', 34.90)
print('_' * 40)
print(f'{"TABELA DE PREÇOS":^40}')
print('_' * 40)
for p in range(0, len(l)):
    if p % 2 == 0:
        print(f'{l[p]:.<30}', end='')
    else:
        print(f'R$ {l[p]:>6.2f}')