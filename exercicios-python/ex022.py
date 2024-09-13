nome_completo = input('Digite seu nome completo: ')

print('Uppercase: {}.'.format(nome_completo.upper()))
print('Lowwercase: {}.'.format(nome_completo.lower()))
print('O nome completo tem {} letras.'.format(len(nome_completo) - nome_completo.count(' ')))
print('O primeiro nome tem {} letras.'.format(len(nome_completo.split()[0])))