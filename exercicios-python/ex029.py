velocidade_do_veiculo = int(input('Qual a velocidade do veiculo? '))
velocidade_max = 80

if velocidade_do_veiculo > velocidade_max:
    valor_da_multa = float((velocidade_do_veiculo - velocidade_max) * 7)
    print('Foi multado em R${:.2f}!'.format(valor_da_multa).replace('.', ','))
else:
    print('Parabéns! Você está dentro do limite de velocidade!')
