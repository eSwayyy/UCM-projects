'''Escribir una función que, dado un string, retorne la longitud de la última palabra.
Se considera que las palabras están separadas por uno o más espacios.
También podría haber espacios al principio o al final del string pasado por
parámetro.'''

def long_ultp(x):
    x=x.split(" ")
    print(len(x[-1]))

x=input("Ingresa un string:\n")
long_ultp(x)