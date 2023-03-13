#digitar 5 valores e adicionar na lista ja na posição correta de forma que fique crescente
l = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > l[-1]:
        l.append(n)
        print(f'O número {n} foi adicionado no fim da fila...')
    else:
        p = 0
        while p < len(l):
            if n <= l[p]:
                l.insert(p, n)
                print(f'O valor {n} foi adicionado na posição {p}...')
                break
            p += 1
print(l)