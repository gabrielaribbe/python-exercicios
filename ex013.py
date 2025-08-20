# Ler um salário e mostrar o valor com aumento de 15%

sal = float(input('Digite o salário do funcionário: '))
aumento = sal * 0.15
novosal = sal + aumento
print('O salário ajustado do funcionário, considerando aumento de 15% é: R$ {:.2f} reais.'.format(novosal))
