'''num = [2, 5, 7, 9]
num[2] = 3
num.append(7)
#num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
print(num)
print(f'Essa Lista tem {len(num)} elementos.')

l = []
l.append(5)
l.append(9)
l.append(4)
for c, v in enumerate(l):
    print(f'Na posição {c+1} encontrei o valor {v}.')'''

a = [2, 5, 7, 9]
b = a[:]
b.insert(4, a[3])
print(f'Lista A: {a}')
print(f'Lista B: {b}')