l = []
for c in range(0, 5):
    l.append(int(input('Digite um valor: ')))
print(f'O maior valor digitado foi {max(l)} e está na posição ', end='')
for i, v in enumerate(l):
    if v == max(l):
        print(f'{i+1}... ', end='')
print()
print(f'O menor valor digitado foi {min(l)} e está na posição ', end='')
for i, v in enumerate(l):
    if v == min(l):
        print(f'{i+1}... ', end='')