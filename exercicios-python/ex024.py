cidade = input('Digite o nome da sua cidade: ')

cidade = cidade.upper()
verificacao = cidade.split()[0] == 'SANTO'

print('Sua cidade começa com "Santo"? {}'.format(verificacao))
