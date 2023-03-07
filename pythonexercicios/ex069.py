# Ler Idade e sexo de varias pessoas, perguntar se quer continuar ou n, mostrar maiores de idade, qntos homens e qntas mulheres < 20 anos
cm = ch = ci = 0
while True:
    i = int(input('Digite a idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Iforme o sexo [M/F]: ')).strip().upper()[0]
    k = ' '
    while k not in 'SN':
        k = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if i >= 18:
        ci += 1
    if s == 'M':
        ch += 1
    if i < 20 and s == 'F':
        cm += 1
    if k == 'N':
        break
print(f'{ci} pessoas são maiores de idade!')
print(f'{ch} pessoas são do sexo masculino!')
print(f'{cm} pessoas são do sexo feminino com menos de 20 anos!')

