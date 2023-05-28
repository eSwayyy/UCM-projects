'''
Una tienda realiza un descuento del 13% sobre la compra, si son realizadas
en los meses de: marzo, abril o mayo.
Realice un algoritmo que reciba el precio de una compra, el mes (por número
o nombre) y, si corresponde, aplique el descuento indicando por pantalla el
precio final de la compra.
'''

import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

precio = int(input("Ingrese el precio de su recibo: "))
mes = int(input("Ingrese el mes en el que realizó la compra (En numero entero):\n"))
if mes>2 and mes<6:
    print(precio*0.87)
else: 
    print(precio)

