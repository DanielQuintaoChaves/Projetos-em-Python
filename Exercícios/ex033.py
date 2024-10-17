n1 = (int(input('Digite o primeiro valor: ')))
n2 = (int(input('Digite o segundo valor: ')))
n3 = (int(input('Digite o terceiro valor: ')))
#m1 = menor
m1 = n1
if n2<n1 and n2<n3:
    m1 = n2
if n3<n1 and n3<n2:
    m1 = n3

#m2 = maior
m2 = n1
if n2>n1 and n2>n3:
    m2 = n2
if n3>n1 and n3>n2:
    m2 = n3
print ('O menor valor é {} e o maior valor é {}! '.format(m1 , m2))