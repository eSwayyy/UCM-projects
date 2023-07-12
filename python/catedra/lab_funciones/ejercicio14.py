'''Definir una función llamada histograma() que tome una lista de números enteros
e imprima un histograma en la pantalla. Ejemplo: histograma([4, 9, 7]) debería
imprimir lo siguiente:
****
*********
*******'''

def histograma(lista):
    for i in lista:
        print("*"*i)

lista=[]
i=1
while i!=0:
    numero=int(input("Ingrese numeros:\n(ingrese 0 para detener)\n"))
    lista.append(numero)
    if numero==0:
        i=0

histograma(lista)