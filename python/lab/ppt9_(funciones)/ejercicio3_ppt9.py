'''● Realizar un programa con funciones en Python, tal que permita determinar si
un número N ingresado por el usuario es primo o no.'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
    
def primos(X):
    if X<2:
        return False
    else:
        for i in range(2,X):
            modulo=X%i
        if(modulo==0):
            return False
        return True
    
res=primos(int(input("Ingrese el valor X\n")))
print(res)