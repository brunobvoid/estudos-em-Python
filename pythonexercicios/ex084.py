#ler nome e peso, guardar tudo em lista, mostrar quantidade de pessoas, lista de mais pesadas e de menos pesadas
princ = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    k = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while k not in 'SN':
        k = str(input('Opção Inválida, Quer continuar? ')).upper().strip()[0]
    if k == 'N':
        break
print(f'Você cadastrou ao todo {len(princ)} pessoas.')
print(f'O maior peso digitado foi de {maior}kg pertencente a ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso digitado foi de {menor}kg pertencente a ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
