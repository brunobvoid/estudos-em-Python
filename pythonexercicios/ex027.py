#ler nome mostar primeiro e ultimo nome separados
n = str(input('Digite aqui seu nome completo: ')).strip()
ns = n.split()
print('Seu primeiro nome é {}'.format(ns[0]))
print('Seu último nome é {}'.format(ns[len(ns)-1]))
