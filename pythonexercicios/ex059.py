print('Vamos fazer operações?')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
o = 0
while o != 5:
    o = int(input('''Escolha uma das opções: 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA 
    -> '''))
    if o == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif o == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif o == 3:
        if n1 > n2:
            print('O maior valor digitado é {}'.format(n1))
        if n2 > n1:
            print('O maior valor digitado é {}'.format(n2))
    elif o == 4:
        print('Recomeçando!')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif o == 5:
        print('FIM')
    else:
        print('Opção Inválida!')
