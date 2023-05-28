'''● Cree un programa donde sea posible ingresar una página de diario de vida,
el programa deberá comprobar que el escrito cumpla con los siguientes
estándares mínimos:
○ La primera palabra del escrito debe comenzar con mayúscula.
○ La primera palabra luego de un punto seguido deberá comenzar con
mayúscula'''

import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

pagina=input("Escriba su pagina:\n")
pagina=pagina.capitalize()
pagina=pagina.split(". ")
print(pagina)

contador=0

while(contador != len(pagina)):
    pagina[contador] = pagina[contador].capitalize()
    contador+=1

contador=0
string=""
while(contador != len(pagina)):
    string=string+pagina[contador]+". "
    contador= contador+1
print(string)