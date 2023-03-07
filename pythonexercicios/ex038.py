# Ler 2 numeros inteiros, mostrar qual numero é maior ou se são iguais
n1 = int(input('Digite aqui um valor inteiro: '))
n2 = int(input('Digite aqui outro valor inteiro: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('Os numéros são iguais!!')