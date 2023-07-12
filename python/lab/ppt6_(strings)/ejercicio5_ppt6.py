'''● Cree un programa donde se ingrese una cadena de String y entregue el
porcentaje de letras vocales que posee, del total de vocales entregue el
porcentaje de aparición de cada vocal y muestra cual es la vocal con mayor
frecuencia de la cadena.'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

str=input("Ingrese una frase:\n")
largo=len(str)
canta=str.count("a")
cante=str.count("e")
canti=str.count("i")
canto=str.count("o")
cantu=str.count("u")

total=canta+cante+canti+canto+cantu
total2=[]

total2.append(canta)
total2.append(cante)
total2.append(canti)
total2.append(canto)
total2.append(cantu)
print(total2)
porcenVocal= (total*100)/largo
porcenA=canta*100/largo
porcenE=cante*100/largo
porcenI=canti*100/largo
porcenO=canto*100/largo
porcenU=cantu*100/largo

vocales=["a","e","i","o","u"]
contador=0
pos=0
i=0
for n in total2:
    if n>i:
        i=n
        pos=contador
    contador+=1

print("=====================================\n")
print("Porcentaje de vocales en la frase===>", porcenVocal,"\n")
print("Porcentaje de vocal a===============>", porcenA,"\n")
print("Porcentaje de vocal e===============>", porcenE,"\n")
print("Porcentaje de vocal i===============>", porcenI,"\n")
print("Porcentaje de vocal o===============>", porcenO,"\n")
print("Porcentaje de vocal u===============>", porcenU,"\n")
print("Vocal con mas frecuencia============>", vocales[pos],"con una cantidad de", total2[pos-1], "apariciones" "\n")