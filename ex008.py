# converter um valor em metros p/ centímetros e milímetros
# centímetro = dividir por 100
# milímetro = dividir por 1.000

metro = float(input('Digite um número em metros: '))
cm = metro * 100
mm  = metro * 1000
km = metro / 1000
hecta = metro / 10000
deca = metro / 10
deci = metro * 10
print('{} metros equivale a:\n{} centímetros \n{} milímetros \n{} quilometros \n{} hectares \n{} decâmetros \n{} decímetros'.format(metro, cm, mm, km, hecta, deca, deci))
