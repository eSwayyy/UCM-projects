'''. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje
indicando si la dirección es válida o no, valiéndose de una función para decidirlo.
Una dirección se considerará válida si contiene el símbolo "@".'''

def evaluaMail1(correo):
    indice = correo.find('@')
    mensa = 'CORRECTO'
    if indice == -1:
        mensa = 'INCORRECTO'
    return mensa

def evaluaMail2(correo):
    cont = correo.count('@')
    mensa = 'INCORRECTO'
    if cont == 1:
        mensa = 'CORRECTO'
    return mensa


correo = input("Mail: ")
estado = evaluaMail1(correo)
print(estado)
estado = evaluaMail2(correo)
print(estado)