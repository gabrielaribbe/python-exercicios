# Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa.

co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hip = (co**2 + ca**2)**(1/2)

print('A hipotenusa é {:.2f}'.format(hip))
