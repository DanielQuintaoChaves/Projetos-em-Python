p = (float(input('Qual a distância em km? :')))

if p>200:
    print('O preço da passagem é de {} reais! '.format(p*0.45))

else:
    print('O preço da passagem é de {} reais! '.format(p*0.5))