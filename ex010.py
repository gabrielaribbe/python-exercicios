# Converter dinheiro em dólar
# Considerar US$1,00 = R$ 3,27

r = float(input('Informe o valor em R$: '))
d = r / 3.27
print('O valor de R$ {:.2f} equivale à US$ {:.2f} (dólares).'.format(r,d))