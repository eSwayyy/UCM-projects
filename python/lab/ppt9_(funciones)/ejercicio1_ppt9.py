'''Realizar un programa en Python, tal que lea un número N y recorra todos los
números enteros desde 0 hasta N.'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

def funcion(x):
    i=0
    while i!=x+1:
        print(i)
        i+=1
    return funcion
x=int(input("Ingresa el valor n\n"))
res=funcion(x)
print(res) 