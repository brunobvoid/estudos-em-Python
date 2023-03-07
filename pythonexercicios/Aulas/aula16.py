'''lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for c in range(0, len(lanche)):
    print(f'eu vou comer {lanche[c]}')
for comida in lanche:
    print(f'eu vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')
print(sorted(lanche))'''

a = (2, 5, 4)
b = (5, 8, 1 ,2)
c = b + a
print(c)
print(c.count(8))
print(c.index(5))

pessoa = ('Bruno', 28, 'M', 95,7)
del(pessoa)
