salario = float(input('Qual é o salário do funcionário? '))

aumento = (salario / 100) * 15
novo_salario = salario + aumento

print('O novo salário com aumento de 15% é {:.2f}'.format(novo_salario))
