d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km foram rodas com o carro? '))
p = d * 60 + km * 0.15
print('O total a pagar pelo aluguel é R${:.2f}.'.format(p))
