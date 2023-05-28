'''Ejercicio 7
● Realizar un programa donde se solicite una cadena al usuario, a
continuación, el programa imprimirá la cadena invertida caracter a caracter y
una cadena invertida en grupos de 4 caracteres.
● Ejemplo:
○ Entrada: “Ingeniería en la UCM”
○ Salida: “ MCU al ne aíreinegnI”
          “ UCM laía ennierInge”'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

str=input("Ingrese un string:\n")
liststr=list(str)
#print(liststr)
liststr.reverse()
str2="".join(liststr)
#print(liststr)
print(str2)
listastr2=[]
primerInter=0
segundoInter=4

contador=0
while contador != len(str2):
    listastr2=listastr2+list([str2[primerInter:segundoInter]])
    contador+=1
    primerInter+=4
    segundoInter+=4

listastr2.reverse()
str3="".join(listastr2)
print(str3)