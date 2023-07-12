'''● Realizar una función, tal que resuelva el cuadrado de los N primeros números
naturales.
● Realizar una función, tal que realice una sumatoria desde 1 hasta un número
N ingresado por el usuario.
● Realizar una función, tal que realice el factorial de un número N ingresado
por el usuario.'''

def factorial(x):
    i=x
    while i >1:
        x = x * (i-1)
        i=i-1
    print("El numero es:", x)
    return x

def cuadrados(y):
    i=0
    while i!=y+1:
        print(i**2)
        i+=1
    return cuadrados

def sumatoria(z):
    i=0
    suma=0
    while i!=z+1:
        suma=suma+i
        i+=1
    return suma

x=factorial(int(input("Ingrese un X\n")))
print(x)
y=cuadrados(int(input("Ingrese un Y\n")))
print(y)
z=sumatoria(int(input("Ingrese un z\n")))
print(z)
