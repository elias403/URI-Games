peca1 = input()
val1 = peca1.split(' ')
a1=int(val1[1])
a2=float(val1[2])
peca2 = input()
val2 = peca2.split(' ')
b1=int(val2[1])
b2=float(val2[2])

calc = a1*a2 + b1*b2
print(f'VALOR A PAGAR: R$ {calc:.2f}')

'''
lista = input().split(' ')
a = lista[0]
b = lista[1]
c = lista[2]
print(a)
print(b)
print(c)
'''