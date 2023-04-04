# ler nome e média e guardar situação do aluno se media 7 ou mais passou se não reprovou
aluno = dict()
aluno['nome'] = str(input('Digite o nome: '))
aluno['média'] = float(input(f'Informe a média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'O {k} é {v}')
