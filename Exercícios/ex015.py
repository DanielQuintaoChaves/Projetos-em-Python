d = int(input('Quantos dias alugados?'))
km = int(input('Quantos Km rodados?'))
v = ((d*60) + (km*0.15))
print ('O valor do aluguel é de: R${}'.format(v))