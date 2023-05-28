'''
Desarrolle un programa en Python, tal que, permita el ingreso de un acta de
notas. Para esto debe considerar:
○ El usuario debe ingresar el nombre del curso.
○ El usuario debe ingresar el nombre de sus alumnos junto a su nota.
○ Cuando el usuario determine que ya fueron ingresados todos los alumnos, el
programa entregará en pantalla toda la información ingresada.
'''

import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

curso = (input("Ingrese el nombre del curso:\n"))
alumnos = int(input("Que cantidad de alumnos desea ingresar:\n"))
listaAlumnos = []
i=0
print("Siendo el formato (Nombre;Nota)\n")
while i < alumnos:
    datos = input("Ingrese el nombre y nota del alumno:\n")
    listaAlumnos.append(datos)
    i=i+1
for i, l in enumerate(listaAlumnos):
    print(i, l)