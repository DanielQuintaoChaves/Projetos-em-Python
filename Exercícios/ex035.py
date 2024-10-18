s1 = float(input('Digite o valor do segmento 1: '))
s2 = float(input('Digite o valor do segmento 2: '))
s3 = float(input('Digite o valor do segmento 3: '))aaqq

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar triângulo! ')

else:
    print('Os segmentos acima não podem formar triângulos! ')