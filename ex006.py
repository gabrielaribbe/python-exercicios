# Mostrar o dobro, triplo e raiz quadrada de um número

n = int(input('Digite um número: '))
d = n*2
t = n*3
raiz=n**(1/2)
# raiz também pode ser calculado: pow(n, (1/2))
print('O dobro do número {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(n, d, t, raiz))
