'''● Realice un programa que solicite al usuario una cadena String y, a
continuación, solicite al usuario un recorte de cadena en un intervalo
específico (desde la posición 1 hasta el largo del String).
● Por ejemplo, si se ingresa “Philip quiere que aprendan mucho”, con el
intervalo 5 a 15, el resultado será:
“ip quiere “'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

str=input("Ingrese una cadena de string:\n")
primerV=int(input("Ingrese el primer valor del intervalo:\n"))
segundoV=int(input("Ingrese el segundo valor del intervalo:\n"))

newStr = str[primerV-1:segundoV] 
print(newStr)