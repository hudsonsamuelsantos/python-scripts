kms = int(input('Quantos km rodados? '))
dias = int(input('Quantos dias? '))

preco_dia = dias * 60
preco_kms = kms * 0.15
preco_total = preco_dia + preco_kms

print('O valor a pagar é de R$ {:.2f}.'.format(preco_total))
