# ler frase e verificar palindromo
f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
inv = ''
for l in range(len(j) -1, -1, -1):
    inv += j[l]
if inv == j:
    print('É um Palindromo!')
else:
    print('Não é um Palindromo!')
