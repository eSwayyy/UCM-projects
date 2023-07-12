'''● Realice un programa con funciones, tal que recorra una lista de números
aleatorios de tamaño indicado por el usuario y cuente la cantidad de números
pares y la cantidad de número impares. Muestre el resultado en pantalla.'''
largo=int(input("Que tan larga sera la lista?:\n"))
lista=[]
def ponernumeros(lista):
    i=0
    while i!=largo:
        lista.append(int(input("Ingrese un numero:\n")))
        i+=1
    print(lista)
    return lista
ponernumeros(lista)

def parImpar(lista):
    pares=0
    impares=0
    for i in lista:
        modulo=i%2
        if modulo==0:
            pares+=1
        elif modulo==1:
            impares+=1
    return pares, impares
pares,impares=parImpar(lista)
print(pares)
print(impares)


