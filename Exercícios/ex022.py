n1 = str(input('Digite seu nome:')).strip()
print(('Seu nome em maiúsculo é: {} ').format(n1.upper()))
print(('Seu nome em maiúsculo é: {} ').format(n1.lower()))
dividido = (n1.split())
print(('Seu nome sem espaços tem {} letras!').format(len(n1) - n1.count(' ')))
print(('Seu primeiro tem {} letras! ').format(len(dividido[0])))