#aprimorar o ex anterior mostrando a soma dos valores pares a soma dos valores da 3 coluna e o maior valor da segunda linha
m = []
l = 1
c = 1
for x in range(1, 10):
    m.append(int(input(f'Digite o numero na posição {l} x {c}: ')))
    c += 1
    if c == 4:
        l += 1
        c = 1
print(f' [{m[0]:^6} {m[1]:^6} {m[2]:^6}]\n', f'[{m[3]:^6} {m[4]:^6} {m[5]:^6}]\n', f'[{m[6]:^6} {m[7]:^6} {m[8]:^6}]')
for x in range(1, 10):
