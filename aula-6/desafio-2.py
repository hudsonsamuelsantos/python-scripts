entrada = input('Digite algo: ')

print('O que você digitou é do tipo {}.'.format(type(entrada)))
print('É numérico? {}.'.format(entrada.isnumeric()))
print('É alfabético? {}.'.format(entrada.isalpha()))
print('É alfanumérico? {}.'.format(entrada.isalnum()))
print('Somente letras maiúsculas? {}.'.format(entrada.isupper()))
print('Somente letras minúsculas? {}.'.format(entrada.islower()))
