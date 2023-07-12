'''Escribir una función sum() y una función multip() que sumen y multipliquen
respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4])
debería devolver 10 y multip([1,2,3,4]) debería devolver 24. '''

def sum(numero):
    suma=0
    for i in numero:
        suma=suma+i
    return print(suma)
        
def multpi(numero):
    multpipliacion=1
    for i in numero:
        multpipliacion=multpipliacion*i
    return print(multpipliacion)

i=int(input("Con cuantos numeros desea operar?:\n"))
j=0
lista=[]
while j!=i:
    k=int(input("Ingrese un numero: "))
    lista.append(k)
    j+=1

sum(lista)
multpi(lista)
