#ler 7 valores, mostrar uma lista com 2 listas de valores pares e impares em ordem crescente
princ = []
par = []
impar = []
for c in range(0, 7):
    princ.append(int(input('Digite um número: ')))
    if princ[c] % 2 == 0:
        par.append(princ[c])
    if princ[c] % 2 == 1:
        impar.append(princ[c])
princ.clear()
princ.append(sorted(par))
princ.append(sorted(impar))
print(f'A lista completa em ordem crescente separada em pares e impares é: {princ}')
