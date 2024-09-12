from math import sin, tan, cos

angulo = float(input('Digite um ângulo em graus: '))

cosseno = cos(angulo)
seno = sin(angulo)
tangente = tan(angulo)

print('O ângulo de {} graus tem cosseno igual a {}, tangente {}, e seno {}.'.format(angulo, cosseno, tangente, seno))
