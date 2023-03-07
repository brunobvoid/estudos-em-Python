'''s = 'S'
while s != 'M' and s != 'F':
    s = str(input('Informe o sexo [M/F]: ')).upper()
    if s != 'M' and s != 'F':
        print('Opção inválida, tente novamente!')
print('FIM')'''

s = str(input('Informe o sexo [M/F]: ')).strip().upper() [0]
while s not in 'MF':
    s = str(input('Opção Inválida, Informe seu sexo [M/F]: ')).strip().upper()[0]
print('FIM')
