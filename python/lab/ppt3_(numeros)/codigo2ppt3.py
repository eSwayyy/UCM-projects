'''
 Realizar un algoritmo donde se ingrese el nombre de una asignatura junto a
 sus tres notas:
○ La primera pondera 50%
○ La segunda pondera 30%
○ La tercera pondera 20%.
 El programa deberá determinar si el alumno pasó o no la asignatura.
'''

import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

asignatura=input("Ingrese el nombre de su asignatura: ")
print("==================================")
nota1=float(input("Ingrese su primera nota(50%): "))
nota2=float(input("Ingrese su segunda nota(30%): "))
nota3=float(input("Ingrese su tercera nota(20%): "))

promedio= nota1*0.5 + nota2*0.3 + nota3*0.2
if promedio>= 4:
    print("El alumno pasa", asignatura)
else:
    print("El alumno no pasa", asignatura)