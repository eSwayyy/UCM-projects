'''● Realice un programa con funciones que resuelva la conjetura de Collatz,
método iterativo que, por medio de operaciones consecutivas, hace
converger un número natural a 1.
● Las reglas son las siguientes:
○ Si el número es par, se divide entre 2.
○ Si el número es impar, se multiplica por 3 y se le suma 1.'''

numero=int(input("Inserte un numero:\n"))

def collatz(x):
    while x!=1:
        modulo= x%2
        if modulo==1:
            x=x*3+1
        else:
            x=x/2
        print(x)
    return 

collatz(numero)