#ler varios numeros, depois criar 2 listas extras com numeros pares e outra com numeros impares
l1 = []
l2 = []
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        l2.append(n)
    else:
        l1.append(n)
    k = str(input('Quer continuar? [S/N]')).strip()[0].upper()
    while k not in 'SN':
        k = str(input('Opção inválida, deseja continuar? [S/N]')).strip()[0].upper()
    if k == 'N':
        break
print(f'Essa é a lista de números PARES: {l2}')
print(f'Essa é a lista de números IMPARES: {l1}')