# Ler um preço e mostrar esse preço com 5% de desconto

preco = float(input('Qual o valor do produto? '))
desc = (preco * 0.05)
valordesc = preco - desc
print('O valor do produto com desconto de 5% é de: {:.2f} reais.'.format(valordesc))
