'''
Realizar un algoritmo que resuelva el cuadrado de los N primeros números
naturales. N es ingresado por el usuario.
'''
import os
os.system("cls")

n = int(input("Ingrese la cantidad de numeros naturales que quiera: \n"))
i = 0

while i <= n:
    print(i ** 2)
    i = i + 1
    