'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la
suma de sus dígitos (utilizando una función que realice dicha suma).'''

def suma(x):
    z=1
    y=0
    x=int(input("NUMERO:\n"))
    y=y+x
    print(y)
    if x==0:
        z=0

while z!=0:
    suma(x)
