# ler primeiro termo e a razão de uma PA e mostrar os 10 primeiros termos
p = int(input('Digite o primeiro termo da progressão aritmética: '))
r = int(input('Agora digite a razão dela: '))
d = p + 10 * r
for p in range(p, d, r):
    print(p, end=' - ')
print('FIM')
