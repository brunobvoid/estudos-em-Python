#ler 4 nomes de alunos e sortear 1 deles
import random
a1 = input("Digite aqui o nome do primeiro aluno(a): ")
a2 = input("Digite aqui o nome do segundo aluno(a): ")
a3 = input("Digite aqui o nome do terceiro aluno(a): ")
a4 = input("Digite aqui o nome do quarto aluno(a): ")
print('O aluno(a) sorteado é: {}'.format(random.choice([a1, a2, a3, a4])))
