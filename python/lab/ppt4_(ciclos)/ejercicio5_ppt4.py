'''
Diseñe un programa en Python, tal que, presente un menú con las siguientes
opciones:
- Calcular el factorial de un número.
- Calcular la suma de un conjunto de números ingresados por el usuario.
- Calcular el promedio de un conjunto de números ingresados por el usuario.
- Salir (el menú se debe volver a mostrar al terminar otra acción acción)
'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

def factorial():
    numeroFactorial = int(input("Ingrese un numero entero:\n"))
    i=numeroFactorial
    while i > 1:
        numeroFactorial = numeroFactorial * (i-1)
        i=i-1
    print("El numero es:", numeroFactorial)

def sumas():
    num=int(input("¿Que cantidad de numeros desea sumar?\n"))
    i2=0
    cant_num=[]
    suma= 0
    while i2 < num:
        numero=int(input("Ingrese un numero entero: "))
        cant_num.append(numero)
        i2=i2+1
    sumaDeEnteros=sum(cant_num)
    print("La suma es:",sumaDeEnteros)

def promedio():
    pro=int(input("¿Que cantidad de numeros desea promediar\n"))
    i3=0
    suma2= 0
    promedio=[]
    while i3 < pro:
        numero2=int(input("Ingrese un numero entero: "))
        promedio.append(numero2)
        i3=i3+1
    sumaProvisional=sum(promedio)
    sumaFinal=sumaProvisional/pro
    print("Su promedio es:", sumaFinal)



while True:
    print("=====MENU PRINCIPAL=====")
    print("1. Factorial de un numero")
    print("2. Suma de n cantidad de numeros")
    print("3. Calcular promedio de n numeros")
    print("4. Salir")
    opcion=int(input("Ingrese una opcion: "))
    if opcion==1:
        factorial()
    elif opcion==2:
        sumas()
    elif opcion==3:
        promedio()
    elif opcion==4:
        break
    else:
        print("opcion invalida")
    


