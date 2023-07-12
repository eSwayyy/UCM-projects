'''Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la
primera letra de cada palabra a mayúscula y las demás letras a minúscula,
dejando inalterados los demás caracteres. Precondición: el separador de
palabras es el espacio: " ".'''

def titulo(x):
    x=x.title()
    print(x)

x=input("Ingrese un string:\n") 
titulo(x)   