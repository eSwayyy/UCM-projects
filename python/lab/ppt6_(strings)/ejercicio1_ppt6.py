'''
Escribir un programa que pida por teclado dos palabras, y a continuación, indique
si riman o no.
● Si coinciden las tres últimas letras debe indicar que si riman.
● Si coinciden sólo las dos últimas letras debe indicar que riman un poco.
● En caso contrario, debe indicar que no riman.
'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

palabra1=input("Escriba una palabra:\n")
palabra2=input("Escriba una palabra:\n")
#transforma el string a lista
list1=list(palabra1)
list2=list(palabra2)
#invertimos la lista
list1.reverse()
list2.reverse()
#dejamos solo las letras que nos interesan de la rima
del list1[3:]
del list2[3:]
if list1==list2:
    print("Las palabras riman")
else:
    del list1[2]
    del list2[2]
    if list1==list2:
        print("Las palabras riman un poco")
    else:
        print("Las palabras no riman")