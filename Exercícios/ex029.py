v = (int(input('Digite a velocidade: ')))
m = v-80

if v>80:
    print ('Você foi multado em: R${},00! '.format(m*7))

else:
    print ('Parabéns, você estava dentro do limite de velocidade! ')