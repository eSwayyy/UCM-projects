'''Indicarle al usuario que ingrese un número entero e informar si es primo o no,
utilizando una función booleana que lo decida.'''

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