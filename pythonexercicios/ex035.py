r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 - r2 < r3 < r1 + r2 and r1 - r3 < r2 < r1 + r3 and r2 - r3 < r1 < r2 + r3:
    print('Com os valores sugeridos é possivel formar um triângulo')
else:
    print('Não é possível formar um triângulo')
    