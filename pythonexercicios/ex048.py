# soma dos numeros impares multiplos de 3 entre 1 e 500
soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma dos {} numéros impares multiplos de 3 é: {}'.format(cont, soma))
