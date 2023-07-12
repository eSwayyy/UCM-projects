'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo
la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"'''

def inversa(x):
    x=list(x)
    x.reverse()
    for i in x:
        print(i, end=(""))

cadena=input("Ingrese un string:\n")
inversa(cadena)