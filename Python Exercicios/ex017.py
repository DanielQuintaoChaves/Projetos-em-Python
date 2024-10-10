# O quadrado da hipotenusa é a soma do quadrado dos catetos
import math
co = (float(input('Digite o comprimento do Cateto Oposto:')))
ca = (float(input('Digite o comprimento do Cateto Adjacente:')))
hi = math.hypot(ca,co)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))