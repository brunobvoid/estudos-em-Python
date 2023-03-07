# Ler numero inteiro, escolher base de coinversão binário, octal ou hexadecimal

n = int(input('Digite o número para fazer a conversão: '))
while True:
    o = int(input('''1 - para BINÁRIO
2 - para OCTAL
3 - para HEXADECIMAL
Digite aqui: '''))
    if o == 1:
        print('{} em Binário é  igual a {}'.format(n, bin(n)[2:]))
        break
    elif o == 2:
        print('{} em Octal é igual a {}'.format(n, oct(n)[2:]))
        break
    elif o == 3:
        print('{} em Hexadecimal é igual a {}'.format(n, hex(n)[2:]))
        break
    elif o != (1, 2, 3):
        print('Opção inválida, tente novamente')


