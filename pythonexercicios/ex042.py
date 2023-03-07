# ex35 mostrar se o triangulo é Equilatero, Isosceles (dois lados iguais) ou Escaleno
print('Vamos saber mais sobre um triangulo!!')
a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('Com os valores sugeridos é possivel formar um triângulo')
    if a == b == c:
        print('E esse triângulo é EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('E esse triângulo é ISÓSCELES')
    elif a != b and a != c and b != c:
        print('E esse triâgulo é ESCALENO')
else:
    print('Não é possível formar um triângulo')
