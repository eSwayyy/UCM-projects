#Ejercicio evaluación
#Integrantes: Joel Labra (20.974.562-3) - Cristian Monsalve (21.789.645-2)

"""El jefe del departamento de decodificación de Unidad de Contraespionaje Mundial (UCM), le pide que escriba un programa que 
permita a los espías cifrar y descifrar los mensajes que la agencia envía a sus colaboradores a través de Internet."""

#lee el mensaje original
def lee_original(original):
    archivo = open(original)
    original = archivo.read()
    return original 

#genera el codificado del mensaje original
def genera_codificado(original):
    #escribimos el alfabeto en una lista
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", ",", ".", ":", ";", "?", "-", "+", "*", "/"]
    #en caso de que el mensaje original esté en minúscula lo transformamos a mayúscula
    original=(str(original)).upper()
    originallist = (str(original)).split("-")
    #este if se usa si la clave ingresada es negativa
    if originallist[0] == "":
        originallist[0] = "-"
        originallist[0] = originallist[0] + originallist[1]
        originallist[1] = originallist[2]
        originallist.pop()
    clave = int(originallist[0])
    #reducimos o aumentamos la clave para evitar errores de fuera de rango de la lista alfabeto
    while clave > len(alfabeto):
        clave = clave - len(alfabeto)
    while clave < 0:
        clave = clave + len(alfabeto)
    codificado = ""
    for i in originallist[1][::]:
        contador = 0
        for j in alfabeto:
            #recorremos el alfabeto completo
            if i == j:
                contador = (len(alfabeto)+contador)%len(alfabeto)
                codificado = codificado+alfabeto[contador-clave]
            contador += 1
            
    posicion = 0
    codificado = list(codificado)

    #pasamos el codificado a una lista para modificarla
    while posicion != len(codificado):
        contador = 0
        for j in alfabeto:
            if posicion%5 == 0 and codificado[posicion] == j:
                contador = (len(alfabeto)+contador)%len(alfabeto)
                codificado[posicion] = alfabeto[contador-clave]
                break
            contador += 1
        posicion += 1
    #realizamos un for el cual genera el codificado final como un string    
    codificadofinal = ""
    for i in codificado:
        codificadofinal += i
    
    return codificadofinal

#lee el mensaje secreto
def lee_secreto(original):
    archivo = open(original)
    original = archivo.read()
    return original

#genera el descifrado del mensaje secreto
def genera_descifrado(secreto):
    #Escribimos el alfabeto en una lista
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", ",", ".", ":", ";", "?", "-", "+", "*", "/",]
    #en caso de que el mensaje secreto esté en minúscula lo transformamos a mayúscula
    secreto=(str(secreto)).upper()
    secretolist = (str(secreto)).split("#")
    clave = int(secretolist[0])
    #reducimos o aumentamos la clave para evitar errores de fuera de rango de la lista alfabeto
    while clave > len(alfabeto):
        clave = clave - len(alfabeto)
    while clave < 0:
        clave = clave + len(alfabeto)
    descifrado = ""
    for i in secretolist[1][::]:
    #Ignoramos los primeros 2 elementos de la lista para trabajar solo con los que necesitamos
        contador = 0
        for j in alfabeto:
        #Buscamos el indice del caracter en el alfabeto
            if i == j:
                contador = (contador + clave) % len(alfabeto)
                descifrado += alfabeto[contador]
                break
            contador += 1

    posicion = 0
    descifrado = list(descifrado)

    while posicion != len(descifrado):
        contador = 0
        for j in alfabeto:
            if posicion % 5 == 0 and descifrado[posicion] == j:
            #Aplicamos una regla distinta para las posiciones que sean multiplos de 5
                contador = (contador + clave) % len(alfabeto)
                descifrado[posicion] = alfabeto[contador]
                break
            contador += 1
        posicion += 1

    descifrado_final = ""
    for i in descifrado:
        descifrado_final += i
        #Concatenamos los caracteres para formar el mensaje final

    return descifrado_final
    


#esta función entrega el mensaje original
def muestra_original(original):
    print(original)
    return 

#esta función entrega el mensaje codificado
def muestra_codificado(original):
    escribir_codificado = original
    archivo = open("codificado.txt","w")
    archivo.write(escribir_codificado)
    print(escribir_codificado)
    return 

#esta función entrega el mensaje secreto
def muestra_secreto(secreto):
    print(secreto)
    return 

#esta función entrega el mensaje descifrado
def muestra_descifrado(secreto):
    escibir_descifrado = secreto
    archivo = open("descifrado.txt","w")
    archivo.write(escibir_descifrado)
    print(escibir_descifrado)
    return 





#Esta seccion es utilizada para ejecutar el programa y llamar a las funciones
mensaje_original = lee_original("original.txt")
muestra_original(mensaje_original)
mensaje_codificado = genera_codificado(mensaje_original)
muestra_codificado(mensaje_codificado)
mensaje_secreto = lee_secreto("secreto.txt")
muestra_secreto(mensaje_secreto)
mensaje_decodificado = genera_descifrado(mensaje_secreto)
muestra_descifrado(mensaje_decodificado)
