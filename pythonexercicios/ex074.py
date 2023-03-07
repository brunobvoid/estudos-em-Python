#Gerar uma TUPLA com 5 números aleatórios e mostrar o menor e o maior valor que contem na tupla
from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(n)
print(max(n))
print(min(n))
