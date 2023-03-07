#ler 5 numeros e dizer o menor e o maior
me = 0
ma = 0
for c in range(1, 6):
    p = int(input('Digite aqui o numero: '))
    if c == 1:
        me = p
        ma = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print('O menor foi {}, e o maior foi {}'.format(me, ma))
