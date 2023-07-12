'''
Realizar un algoritmo que, dado un año, este indique si es un año bisiesto o
no. Las condiciones son las siguientes:
○ Si es divisible por 4 y no es divisible 100 es bisiesto.
○ Si un año es divisible entre 100 y además es divisible entre 400, también
resulta bisiesto.
'''

import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

año = int(input("Ingrese un año cualquiera: \n"))
modulo100 = año%100
modulo400 = año%400
modulo4 = año%4

if modulo100==0 and modulo400==0 or modulo100!=0 and modulo4==0:
    print(año, "es un año bisiesto")
else:
    print(año, "no es un año bisiesto")
