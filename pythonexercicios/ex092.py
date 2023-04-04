#ler nome, ano, carteira de trabalho guardar com idade, se acarteira for diferente de 0 o dicionário tbm recebe o ano de contratação e o salário
#calcule e acrescente a aposentadoria
from datetime import datetime
t = dict()
t['nome'] = str(input('Nome: '))
t['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
nasc = int(input('Ano de Nascimento: '))
t['idade'] = datetime.now().year - nasc
k = str(input('Possui Carteira de trabalho? [S/N] ')).upper().strip()
while k not in 'SsNn':
    k = str(input('Opção inválida! Possui Carteira de trabalho [S/N]? ')).upper().strip()
if k in 'Ss':
    t['ctps'] = int(input('Nº da Carteira de Trabalho: '))
    t['contratação'] = int(input('Ano de Contratação: '))
    t['salário'] = float(input('Salário: R$'))
    if t['sexo'] == 'M':
        t['aposentadoria'] = 65
    if t['sexo'] == 'F':
        t['aposentadoria'] = 62
print('-=' *30)
for k, v in t.items():
    print(f' -> {k} - {v}')
