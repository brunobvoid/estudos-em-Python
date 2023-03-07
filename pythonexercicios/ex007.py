nome = input('Digite o nome do Aluno: ')
n1 = float(input('Agora digite a nota do primeiro período: '))
n2 = float(input('Agora digite a nota do segundo período: '))
m = (n1+n2)/2
print('A média de {} é {:.f1}'.format(nome, m))
