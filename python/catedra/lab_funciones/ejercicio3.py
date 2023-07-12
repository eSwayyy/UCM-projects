'''. Definir una función max_de_tres(), que tome tres números como argumentos y
devuelva el mayor de ellos.'''

def max_de_tres(x,y,z):
    lista=[x,y,z]
    lista.sort(reverse=True)
    print(lista[0])

num1=int(input("Ingrese un numero:\n"))
num2=int(input("Ingrese un numero:\n"))
num3=int(input("Ingrese un numero:\n"))

max_de_tres(num1,num2,num3)