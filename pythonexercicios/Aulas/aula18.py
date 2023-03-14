'''t = list()
t.append('Gustavo')
t.append(40)
g = list()
g.append(t[:])
t[0] = 'Maria'
t[1] = 22
g.append(t[:])
print(g)

g = [['João', 19],['Maria', 28],['Joaquim', 13],['Pedro', 43]]
for p in g:
    print(p[0])'''

g = list()
d = list()
r = 'S'
while r in 'Ss':
    d.append(str(input('Nome: ')))
    d.append(int(input('Idade: ')))
    d.append(str(input('Como você se identifica?: ')))
    r = str(input('Deseja continuar? [S/N]')).strip()[0].upper()
    g.append(d[:])
    d.clear()
    while r not in 'SN':
        r = str(input('Opção Inválida! Deseja continuar? [S/N]')).strip()[0].upper()
        if r == 'N':
            break
for c in range(len(g)):
    print(f'{g[c][0]} tem {g[c][1]} anos e se identifica como {g[c][2]}!')
