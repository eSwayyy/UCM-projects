'''Definir una función generar_n_caracteres() que tome un entero n y devuelva el
carácter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería
devolver "xxxxx". '''

def generar_n_caracteres(numero,caracter):
    i=0
    while i!=numero:
        print(caracter,end=(""))
        i+=1
    return

numero=int(input("Numero de caracteres:\n"))
caracter=input("Caracter:\n")

generar_n_caracteres(numero,caracter)