#ler 4 valores pelo teclado guardar numa tupla:
#MOSTRAR quantas vezes apareceu o 9, posição do primeiro numero 3 quantos foram pares
n = (int(input('Digite um número: ')), int(input('Digite um número: ')),
     int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'O número 9 apareceu {n.count(9)} vezes!')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+1}ª posição!')
else:
    print('O número 3 não foi digitado!')
print('Os valores digitados foram:', end=' ')
for x in n:
    if x % 2 == 0:
        print(x, end=' ')
