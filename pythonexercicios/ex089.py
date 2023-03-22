#ler nome  2 notas, mostre um boletim mostrando a média e permita que o usuário possa mostrar as notas de cada aluno individualmente
lista = list()
aluno = list()
print('Cadastro de boletim')
while True:
    nome = (str(input('Nome: ')))
    n1 = (float(input('Nota 1: ')))
    n2 = (float(input('Nota 2: ')))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    k = str(input('Quer continuar? [S/N] ')).upper().strip()
    while k not in 'SsNn':
        k = str(input('Opção inválida, Quer continuar? [S/N] ')).upper().strip()
    if k == 'N':
        break
print('-='*20)
print(f'{"Nº.":<4}{"Nome":<10}{"Média":>10}')
for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='*20)
    a = int(input('Quer mostrar a nota de qual aluno? Digite o número do indice:  '))
    if a <= len(lista) - 1:
        print(f'Notas de {lista[a][0]} são {lista[a][1]}')
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while r not in 'SnNn':
        r = str(input('Opção Inválida, Deseja continuar? [S/N] ')).upper().strip()
    if r in 'N':
        break
print('>>>Finalizado<<<')