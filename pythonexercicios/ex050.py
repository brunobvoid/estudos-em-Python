# ler 6 numeros inteiros e somar apenas os pares
s = 0
for c in range(1, 7):
    n = int(input('Digite aqui um número inteiro: '))
    if n % 2 == 0:
        s = s + n
print('A soma dos números pares é: {}'.format(s))
