# Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice
a1 = str(input('Informe o nome do primeiro aluno: '))
a2 = str(input('Informe o nome do segundo aluno: '))
a3 = str(input('Informe o nome do terceiro aluno: '))
a4 = str(input('Informe o nome do quarto aluno: '))
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
