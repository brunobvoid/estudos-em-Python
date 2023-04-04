#ler nome do jogador e qntidade de partidas, perguntar quantidade de gols feitos em cada partida entregar aproveitamento
jogador = dict()
gols = list()
c = 1
jogador['nome'] = str(input('Nome do Jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, n+1):
    gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na {c}ª partida? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 25)
print(jogador)
print('-=' * 25)
for k, v in jogador.items():
    print(f'    {k} -> {v}')
print('-=' * 25)
print(f'O Jogador {jogador["nome"]} jogou {n} partidas.')
for i, v in enumerate(gols):
    print(f'  -> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {sum(gols)} gols.')
