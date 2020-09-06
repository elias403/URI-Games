valores = input().split(' ')
lista = list()
for x in valores:
    y=int(x)
    lista.append(y)
print(f'{max(lista)} eh o maior')