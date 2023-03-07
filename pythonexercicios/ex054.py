# ler 7 anos de nascimento mostrar qntas tem 18+ e quantas não tem ainda
from datetime import date
atual = date.today().year
m = 0
n = 0
for c in range(1, 8):
    ano = int(input('Digite aqui o ano do seu nascimento: '))
    if atual - ano >= 18:
        m = m + 1
    else:
        n = n + 1
print('{} pessoas são maiores de idade e {} são menores'.format(m, n))
