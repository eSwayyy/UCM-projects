'''● Realice un programa en Python que genere un tablero de juego para
buscaminas, el cual deberá considerar:
○ Un tamaño de tablero definido por el usuario.
○ Una cantidad de minas definida por el usuario.
● Las minas deben ser localizadas de forma aleatoria y el resto de las
posiciones deberán indicar el número de minas que tienen alrededor (el de
caso de tener).'''
import random
x=random.randint(0,2)
y=random.randint(0,2)
columnas=int(input("¿Cuantas columnas desea?:\n"))
filas=int(input("¿Cuantas filas desea?:\n"))

def matriz(columnas, filas):
    matrix=""
    area=0
    while area!=filas:
        j=0
        while j!=columnas:
            matrix=matrix+input("Ingrese un numero al matrix:\n")
            if j!=columnas-1:
                matrix=matrix + "|"
            j+=1
        matrix=matrix+"\n"
        area+=1
    print(matrix)
matriz(columnas,filas)