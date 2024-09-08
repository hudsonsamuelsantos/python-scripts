preco = float(input('Qual o preço do produto? '))

desconto = (preco / 100) * 5
preco_promocional = preco - desconto

print('O preço do produto com 5% de desconto é {:.2f}!'.format(preco_promocional))
