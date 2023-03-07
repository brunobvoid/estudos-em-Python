# LEr nome e preço, perguntar se quer continuar, mostrar total gasto, qntos produtos maiores que 1000 reais, e o nome do produto mais barato

c = s = m = cont = 0
menor = ' '
while True:
        nome = str(input('Informe o nome do produto: '))
        p = float(input('Informe o valor: R$'))
        cont += 1
        if p > 1000:
            c += 1
        if cont == 1 or p < m:
            m = p
            menor = nome
        s += p
        r = ' '
        while r not in 'SN':
            r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if r == 'N':
            break
print(f'''O total gasto foi {s:.2f}
{c} produtos custram mais que R$1000.00
o produto mais barato foi {menor} e custa {m:.2f}''')