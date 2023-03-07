# Simular Caixa Eletronico, Perguntar valor será sacado, mostrar qual quantidade de cada cedula será sacada
valor = int(input('Quanto dseja sacar? R$'))
ced = 200
tc = 0
while True:
    if valor >= ced:
        valor -= ced
        tc += 1
    else:
        if tc > 0:
            print(f'Total de {tc} cédulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced ==2:
            ced = 1
        tc = 0
        if valor == 0:
            break