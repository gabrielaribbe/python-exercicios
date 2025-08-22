# Criar um programa que leia um número qualquer e retorne sua porção inteira.

'''n = float(input('Digite um número: '))
from math import trunc
numint = trunc(n)
print('O valor digitado foi {} e sua porção inteira é {}.'.format(n, numint))'''

n = float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(n, int(n)))
