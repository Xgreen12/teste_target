"""
 Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre sera a soma dos 2 valores anteriores
 (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
 ele caucule a sequência de Fibonacci e retorne uma menssagem avisando se o número informado pertence ou não a sequência.

"""


print('Sequência de Fibonacci')

n = int(input('Digite um número: '))

if n == 0:
    print('Pertence a sequência')
    exit(0)

f1 = 0
f2 = 1

while True:
    f = f1 + f2
    if n == f:
        print('{} pertence a sequencia'.format(n))
        break
    elif n < f:
        print('{} não pertence a sequencia'.format(n))
        break
    f1 = f2
    f2 = f
