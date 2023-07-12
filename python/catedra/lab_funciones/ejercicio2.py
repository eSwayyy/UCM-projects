'''Definir una función max() que tome como argumento dos números y devuelva el
mayor de ellos. '''

def max(x,y):
    if x>y:
        print(x)
    else:
        print(y)

numero=int(input("Ingresar un numero\n"))
numero2=int(input("Ingresar un numero\n"))
max(numero, numero2)