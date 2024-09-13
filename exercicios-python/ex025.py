nome = input('Digite um nome: ')

nome = nome.upper()
silva = nome.split().count('SILVA')
verificacao = silva > 0

print('Seu nome tem Silva? {}.'.format(verificacao))
