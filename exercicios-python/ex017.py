from math import hypot

c_oposto = float(input('Qual o comprimento do cateto oposto do triângulo? '))
c_adjacente = float(input('Qual o comprimento do cateto adjacente do triângulo? '))

hipotenusa = hypot(c_oposto, c_adjacente)

print('A hipotenusa do triângulo é igual a {}.'.format(hipotenusa))
