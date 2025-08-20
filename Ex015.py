# Ler quantidade de KM percorrido por um carro alugaddo
# Ler quantidade de dias pelos quais foram alugados.
# Calcular preço a pagar, sabendo que custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de KM rodado: '))
dia = int(input('Digite a quantidade de dias de aluguel: '))

valorkm = km * 0.15
valordia = dia * 60
total = valorkm + valordia
print('O valor a pagar considerando {} KM rodados e {} dias de aluguel é de: R$ {:.2f}'.format(km, dia, total))
