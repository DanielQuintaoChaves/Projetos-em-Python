s = (int(input('Digite o salário: ')))
a = s+s*0.15
ab = s+s*0.1
#ab salário > R$1250,00

if s<1250:
    print('Seu aumento novo salário é: R${}! '.format(a))

else:
    print('Seu novo salário é de: R${}! '.format(ab))

