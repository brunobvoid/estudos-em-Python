# Contagem Regressiva de 10 a 1 (1sec)
from time import sleep
print('Iniciando contagem regressiva!!')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('FIM')