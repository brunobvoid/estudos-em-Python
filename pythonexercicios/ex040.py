# Ler 2 notas do aluno calcular média mostrar se menos de 5 REPROVADO se entre 5 e 6.9 RECUPERAÇÃO se 7 ou mais APROVADO

print('Olá vamos calcular sua média e saber se você foi aprovado?')
n1 = float(input('Digite aqui a nota do primeiro semestre: '))
n2 = float(input('Digite aqui a nota do segundo semestre: '))
m = (n1+n2)/2
if m < 5:
    print('Sua media foi, {:.1f} então você foi REPROVADO!' .format(m))
elif m == 5 or m < 7:
    print('Sua média foi {:.1f} logo você poderá fazer a Recuperação!' .format(m))
else:
    print('Parabéns você foi APROVADO com uma média de {:.1f}!'.format(m))
