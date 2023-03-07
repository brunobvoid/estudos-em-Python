# ler nome idade e sexo 4 vezes
soma = 0
velho = ''
idd = 0
m = 0
for c in range(1, 5):
    n = input('Nome: ')
    i = int(input('Idade: '))
    s = str(input('Sexo, M ou F: '))
    soma += i
    if c == 1 and s in 'Mm':
        idd = i
        velho = n
    if s in 'Mm' and i > idd:
        idd = i
        velho = n
    if s in 'Ff' and i < 20:
        m +=1
print('A média de idade do grupo é {}'.format(soma / 4))
print('O Homem mais velho tem {} e se chama {}'.format(idd, velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(m))
