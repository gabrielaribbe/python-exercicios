# Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hip))
