# jogar par ou impar, só parar qndo perder, mostrar o total de vitórias consecutivas no final
import random
print('-'*10, 'JOGO PAR OU ÍMPAR', '-'*10)
c = s = 0
while True:
    k = str(input('Faça sua escolha [P/I] : ')).strip().upper()[0]
    n = int(input('Agora digite um número de 1 a 10: '))
    p = random.randint(0, 10)
    s = p + n
    if s % 2 == 0 and k == 'P':
        print('Você escolheu PAR, então eu sou ÍMPAR')
        print(f'Você escolheu: {n} Eu escolhi: {p} E a soma é: {s} deu PAR')
        print('Parabéns vc GANHOU!!')
        c += 1
    elif s % 2 != 0 and k == 'I':
        print('Você escolheu ÍMPAR, então eu sou PAR')
        print(f'Você escolheu: {n} Eu escolhi: {p} E a soma é: {s} deu ÍMPAR')
        print('Parabéns vc GANHOU!!')
        c += 1
    elif s % 2 == 0 and k == 'I':
        print('Você escolheu ÍMPAR, então eu sou PAR')
        print(f'Você escolheu: {n} Eu escolhi: {p} E a soma é: {s} deu PAR')
        print('Você perdeu!!')
        print(f'Você ganhou {c} vezes seguidas antes de perder')
        break
    elif s % 2 != 0 and k == 'P':
        print('Você escolheu PAR, então eu sou ÍMPAR')
        print(f'Você escolheu: {n} Eu escolhi: {p} E a soma é: {s} deu ÍMPAR')
        print('Você perdeu!!')
        print(f'Você ganhou {c} vezes seguidas antes de perder')
        break
