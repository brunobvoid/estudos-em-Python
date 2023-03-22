#aprimorar o ex anterior mostrando a soma dos valores pares a soma dos valores da 3 coluna e o maior valor da segunda linha
m = []
l = c = s = sc = maior = 0
for x in range(0, 9):
    m.append(int(input(f'Digite o numero na posição {l} x {c}: ')))
    if m[x] % 2 == 0:
        s = s + m[x]
    if c == 2:
        sc = sc + m[x]
    if l == 1:
       if m[x] > maior:
           maior = m[x]
    c += 1
    if c == 3:
        l += 1
        c = 0
print(f' [{m[0]:^6} {m[1]:^6} {m[2]:^6}]\n', f'[{m[3]:^6} {m[4]:^6} {m[5]:^6}]\n', f'[{m[6]:^6} {m[7]:^6} {m[8]:^6}]')
print(f'A soma dos valores pares é {s}')
print(f'A soma dos valores da terceira coluna é {sc}')
print(f'O maior valor da segunda linha é {maior}')