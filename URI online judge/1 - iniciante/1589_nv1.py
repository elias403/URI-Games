#Bob Conduite

T = int(input())
for casos in range(T):
    valor=input()
    separados=valor.split(' ')
    R1 = int(separados[0])
    R2 = int(separados[1])
    print(R1+R2)
