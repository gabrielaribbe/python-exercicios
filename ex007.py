# Ler duas notas, calcular média e mostrar.
nome = input('Qual o nome do aluno? ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A média das duas notas do aluno {} é {:.2f}'.format(nome, media))
