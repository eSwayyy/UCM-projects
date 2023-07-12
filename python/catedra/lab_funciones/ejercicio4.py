'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
contrario devuelve False. '''

def es_vocal(x):
    vocales=["a","e","i","o","u"]
    i=0
    parametro=False
    while i!=len(vocales):
        if x==vocales[i]:
            
            parametro=True
        i+=1
    if parametro==True:
        print(True)
    else:
        print(False)

caracter=input("Ingrese un caracter:\n")
caracter.lower
es_vocal(caracter)