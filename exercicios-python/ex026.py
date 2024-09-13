frase = input('Digite uma frase: ').upper().strip()

print('Letras "A": {}.'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição: {}.'.format(frase.find('A')))
print('A letra "A" aparece pela última vez na posição: {}.'.format(frase.rfind('A')))
