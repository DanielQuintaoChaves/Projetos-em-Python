import math
n1 = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
print('O ângulo seno de {}° é {}'.format(n1, seno))
print('O ângulo cosseno de {}° é {}'.format(n1, cos))
print('O ângulo tangente de {}° é {}'.format(n1, tan))