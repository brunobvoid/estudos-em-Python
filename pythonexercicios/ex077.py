#criar tupla sem acentos mostrar as vogais dentro de cada palavra
t = ('LISTA', 'PROGRAMAÇAO', 'BOLA', 'HORARIO', 'CARRO', 'BALAO')
for p in t:
    print(f'\nNa palavra {p} temos ', end=' ')
    for l in p:
        if l.lower() in 'aeiou':
            print(l.lower(), end=' ')
