'''Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de
ocurrencias del dígito en el número, utilizando para ello una función que calcule
la frecuencia.'''

def frecuencia(numero,digito):
    suma=0
    for i in numero:
        if i==digito:
            suma+=1
    return print(suma)

numero=(input("Ingrese un numero entero:\n"))
digito=(input("Ingrese un digito:\n"))

frecuencia(numero,digito)

