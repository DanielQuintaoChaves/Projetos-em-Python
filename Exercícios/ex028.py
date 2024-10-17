import random

n2 = (random.randrange(0, 5))

print ('Vou pensar um número de 0 a 5, tente descobrir! ')
n1 = (int(input('Tente descobrir, chute um número: ')))

if n1 == n2:
    print('Parabéns, o número que eu pensei foi mesmo o {}! '.format(n2))

else:
    print('Hahaha, errou otário, o número que eu pensei foi o {}! '.format(n2))

