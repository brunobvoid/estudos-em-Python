#ler varios numeros até parar, mostrar quandos numeros foram digitados, descrescente e se tem 5 na lista
l=[]
k = 'S'
while k in 'S':
    n = int(input('Digite um número: '))
    l.append(n)
    k = str(input('Quer continuar? [S/N] ')).strip().upper()
    while k not in 'SN':
        k = str(input('Opção inválida, Quer continuar? [S/N] ')).strip().upper()
print(f'Você digitou {len(l)} elementos.')
l.sort(reverse=True)
print(f'A lista em decrescente é {l}')
if 5 in l:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
