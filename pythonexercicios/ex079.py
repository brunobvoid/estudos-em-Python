#Ler valores até parar, não adicionar valores repetidos, mostrar em ordem crescente
l = list()
k = ' '
i = 0
while True:
    n = (int(input('Digite um número: ')))
    if n not in l:
        l.append(n)
    else:
        print('Valor duplicado, não será adicionado!')
    k = str(input('Quer continuar? [S/N] ')).strip().upper()
    while k not in 'SsNn':
       k = str(input('Opção Inválida! Quer continuar? [S/N] ')).strip().upper()
    if k in 'Nn':
        break
print(sorted(l))
