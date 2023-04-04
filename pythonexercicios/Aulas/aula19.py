#dicionários
pessoas = {'nome': 'Bruno', 'sexo': 'M', 'idade': 28}
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
pessoas['nome'] = 'João'
print(pessoas)

br = []
estado1 = {'uf': 'Bahia', 'sigla': 'BA'}
estado2 = {'uf': 'Pernambuco', 'sigla': 'PE'}
br.append(estado1)
br.append(estado2)
print(estado1)
print(estado2)
print(br)
print(f'A sigla do estado {br[0]["uf"]} é {br[0]["sigla"]}')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla do Estado'))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' -')
    print()
