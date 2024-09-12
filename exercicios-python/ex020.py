from random import shuffle

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

ordem = [a1, a2, a3, a4]
shuffle(ordem)

print('A ordem sorteada foi: 1.{} 2.{} 3.{} 4.{}.'.format(ordem[0], ordem[1], ordem[2], ordem[3]))
