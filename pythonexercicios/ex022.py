# Ler Nome completo, mostrar Nome todo maiúsculo, minúsculo, Qnts letras sem os espaços, qnts letras primeiro nome
nome = str(input('Digite seu nome completo aqui: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
s = nome.split()
print(len(s[0]))
