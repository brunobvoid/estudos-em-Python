n = c = s = 0
n = int(input('Digite um número [999 encerra]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número [999 encerra]: '))
print('Você digitou {} números e a soma deles é {}!'.format(c, s))
