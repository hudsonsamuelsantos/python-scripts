largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))

area = largura * altura
litros_de_tinta  = area / 2

print('Você precisará de {:.1f} litros de tinta!'.format(litros_de_tinta))
