#Ler frase, quantas letras a, qual a primeira e qual a ultima
f = str(input('Digite aqui a frase: ')).upper().strip()
print('A letra a aparece {} vezes'.format(f.count('A')))
print('A primeira letra a aparece na {}ª posição'.format(f.find('A')+1))
print('A ultima letra "a" aparece na {}ª posição'.format(f.rfind('A')+1))