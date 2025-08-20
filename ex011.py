# Ler largura e altura de uma parede em metros e calcular a área.
# Informar a quantidade de tinta para pintá-la considerando que
# 1 litro de tinta pinta uma área de 2m².

l = float(input('Informe a largura da parede em metros: '))
a = float(input('Informe a altura da parede em metros: '))

mq = l * a
print('A parede possui {}m².'.format(mq))
litro = mq / 2
print('A quantidade necessária de tinta para pintar {}m² é de {} litros.'.format(mq, litro))
