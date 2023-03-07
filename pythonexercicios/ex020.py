#ler 4 nomes de alunos e sortear uma ordem e mostrar a ordem sorteada
import random
a1 = input("Digite aqui o nome do primeiro aluno(a): ")
a2 = input("Digite aqui o nome do segundo aluno(a): ")
a3 = input("Digite aqui o nome do terceiro aluno(a): ")
a4 = input("Digite aqui o nome do quarto aluno(a): ")
l = [a1, a2, a3, a4]
random.shuffle(l)
print('A ordem de apresentação será: {}'.format(l))
