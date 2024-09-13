n = input('Digite um número de 0 a 9999: ')[:4]

print('Unidade: {}.'.format(list(n)[3]))
print('Dezena: {}.'.format(list(n)[2]))
print('Centena: {}.'.format(list(n)[1]))
print('Milhar: {}.'.format(list(n)[0]))
