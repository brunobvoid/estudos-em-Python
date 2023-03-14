#ler uma expressão matemática e analisar se esta valida a expressão
s = []
e = str(input('Digite aqui a expressão matemática: '))
for v in e:
    if v == '(':
        s.append('(')
    elif v == ')':
        if len(s) > 0:
            s.pop()
        else:
            s.append(')')
            break
if len(s) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
