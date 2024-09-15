from random import randint

numero_1a5 = randint(1,5)

numero_usuário = int(input('O computador "pensou" um número de 1 a 5. Tente advinhar: '))

if numero_1a5 == numero_usuário:
    print('Prabéns! O número é {}!'.format(numero_1a5))
else:
    print('Errou! Na verdade o número correto é {}'.format(numero_1a5))
