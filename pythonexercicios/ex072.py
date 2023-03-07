t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
c = 'S'
while c in 'S':
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {t[n]}')
        c = str(input('Quer continuar [S/N]? ')).strip().upper()
    else:
        print('Opção Inválida! ', end='')
