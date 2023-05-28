'''
Hacer un algoritmo que lea un número menor que 1000:
○ Si el número tiene un dígito, deberá elevarlo al cuadrado y mostrar su
resultado.
○ Si el número es de dos dígitos, multiplicarlo por dos y mostrar su resultado.
○ Si el número es de tres dígitos, restarle cien y mostrar el resultado.
○ En otro caso, mostrar la leyenda “Número no válido”.
'''

import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

numero = int(input("Ingrese un numero natural menor que mil: \n"))
if numero > 99 and numero < 1000:
    print(numero -100)
if numero > 9 and numero < 100:
    print(numero * 2)
if numero < 10: 
    print(numero ** 2)
if numero > 1000:
    print("Numero no valido")


