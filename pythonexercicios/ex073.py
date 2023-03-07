camp = ('Arsenal', 'Manchester City', 'Manchester United', 'Tottenham', 'Newcastle', 'Liverpool','Fulham', 'Brighton',
        'Brentford', 'Chelsea', 'Aston Villa', 'Crystal Palace', 'Nottingham Forest', 'Leicester', 'Wolverhampton',
        'West Ham', 'Leeds United', 'Everton', 'Bournemouth', 'Southampton')
print(' ')
print('Colocação atual do Campeonato Inglês')
for c in range(20):
        print(c + 1 ,'-', camp[c])
print(' ')
print('Esses são os 5 primeiros colocados do Campeonato Inglês!')
for c in range(5):
        print(c + 1 ,'-', camp[c])
print(' ')
print('Esses são os ultimos 4 colocados do Campeonato Inglês!')
n = 20
for c in range(4):
        print(n, '-', camp[19-c])
        n -= 1
print(' ')
print('Aqui está a ordem Alfalbética dos times:')
print(sorted(camp))
print(' ')
for c in camp:
        if c == 'Chelsea':
                print(f'O Chelsea está na {camp.index(c)+1}ª posição!')
