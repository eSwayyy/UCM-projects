'''
Diseñe un algoritmo que lea dos números por teclado, a continuación, el
programa debe imprimir un mensaje que defina cual es mayor o si son
iguales.
'''

import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

print('Solo valido para numeros enteros:')
print("==================================")
a=int(input('Ingrese primer numero: '))
b=int(input('Ingrese segundo numero: '))

if a>b:
    print(a, "es mayor ")
if a==b:
    print("los numeros son iguales")
if a<b:
    print(b, "es mayor")
