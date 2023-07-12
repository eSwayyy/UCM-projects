'''
Realizar un algoritmo que, dado un número entero, indique en pantalla si este
es par o impar, si el número es igual a cero, se debe indicar que es igual a
cero.
'''

import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

numero = int(input("Ingrese un numero entero: "))
if numero == 0:
    print("El numero es igual a cero")
modulo = numero%2
if modulo ==1:
    print("El numero", numero, "es impar")
else:
    print("El numero", numero, "par")