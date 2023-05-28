'''
Diseñe un algoritmo que resuelva la Conjetura de Collatz, método iterativo
que, por medio de operaciones consecutivas transforma un número a uno.
Las reglas son las siguientes:
○ Si el número es par, se divide entre 2.
○ Si el número es impar, se multiplica por 3 y se le suma 1.
'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
    
numero = int(input("Ingrese un numero entero:\n"))
modulo = numero%2
while numero > 1:
    if modulo == 0:
        numero = numero/2
    else:
        numero = numero*3+1
    modulo =numero%2
    print(numero)