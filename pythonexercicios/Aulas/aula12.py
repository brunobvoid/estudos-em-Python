nome = str(input('Qual é seu nome? '))
nm = nome.upper()
if nm == 'BRUNO':
    print('Que nome bonito!')
elif nm == 'PEDRO' or nm == 'JOÃO' or nm == 'JOSÉ':
    print('Seu nome é bem popular!')
elif nm in ' ANA MARIA JULIANA PAULA':
    print('Seu nome é bem popular entre os nomes femininos!')
else:
    print('Seu nome é bem normal.')
print ('Tenha um bom dia, {}!'.format(nome))