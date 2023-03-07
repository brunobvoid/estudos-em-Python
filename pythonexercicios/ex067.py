# tabuada de vários numeros 1 de cada vez, flag: numero negativo
print('PROGRAMA TABUADA')
while True:
    n = int(input('Digite o valor: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('Programa Encerrado')
