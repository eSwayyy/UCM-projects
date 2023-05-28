'''
Un mensaje ha llegado al mail con errores, diseñe un programa que sea capaz de
corregir estos correos defectuosos, donde el sistema ha reemplazado
erróneamente los espacios por comas y las comas por #.
Un ejemplo de mensaje erróneo es:
 “La,cantimplora,se,calentó#tomar,agua,así,no,tiene,gracia”
'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')
    
mail=input("Inserte su mail erroneo:\n")
mailNuevo=mail.replace(",", " ")
mailNuevo2=mailNuevo.replace("#",",")

print(mailNuevo2)