'''● Realice un programa con funciones en Python, tal que permita el llenado
elemento a elemento, de una matriz de dimensión elegida por el usuario.'''

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