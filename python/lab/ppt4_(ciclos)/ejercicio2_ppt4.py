'''
Realice un algoritmo que reciba un número natural, y a continuación,
determine si es primo o no.
'''
import os
os.system("cls")

numero = int(input("Ingrese un numero natural: "))
if numero == 1:
    print("El numero no es primo")
else: 
    if(numero == 2):
        print("El numero no es primo")
    else:
        divisor=2
        bandera=True
        while(divisor<numero):
            modulo=numero%divisor
            if modulo==0:
                    bandera=False
                    divisor=divisor+1
    if bandera==True:
        print("el numero es primo")
    else:
        print("el numero no es primo")