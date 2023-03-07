# Ler varios numeros mostrar a quantidade e a soma
c = s = 0
while True:
    n = int(input('Digite um valor (999 para interromper o programa): '))
    if n == 999:
        break
    c += 1
    s += n
print (f'Você digitou {c} valores e a soma deles é {s}')
