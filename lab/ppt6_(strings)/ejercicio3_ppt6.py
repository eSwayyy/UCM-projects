'''
● Realice un programa que lea tantas cadenas de String como el usuario
indique por teclado, a continuación, para cada cadena separe cada palabra
por espacio (“ ”) y muestre en pantalla dos mensajes:
○ El primero contiene todas las palabras que ocupan una posición impar
en el texto.
○ El segundo contiene todas las palabras que ocupan una posición par en
el texto.
● Ejemplo: “Hugo y Philip somos sus profes”
○ Mensaje 1: “Hugo Philip sus”
○ Mensaje 2: “y somos profes”
'''

import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
    
cant=int(input("Cuantas palabras desea ingresar?:\n"))
i=0
listaPalabras=[]
while i<cant:
    palabras=input("Ingrese la palabra deseada:\n")
    listaPalabras.append(palabras)
    i+=1
#print(listaPalabras) 
print("===Palabras pares===")
n=1
for i in listaPalabras:
    modulo=n%2
    if modulo==0:
        print(i, end=(" "))    
    n=n+1
print("\n===Palabras impares===")
n2=1
for i in listaPalabras:
    modulo=n2%2
    if modulo==1:
        print(i, end=(" "))    
    n2=n2+1
