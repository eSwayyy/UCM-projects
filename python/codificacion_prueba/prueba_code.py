#Integrantes: Alonso Vergara(21.825.897-2) Francisco Uribe(21.72.827-7)

#Lectura del mensaje
def lee_original(original):
    if __name__ == "__main__":
        #abrir el archivo de texto
        archivo=open("original.txt","r")
        #leer el texto del archivo
        original=archivo.read()
    return original
    
lee_original("original.txt")
#Genera el codificado del mensaje original
def genera_codificado(original): 
    alfabeto=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", ",", ".", ":", ";", "?", "-", "+", "*", "/"] 
    #Para casos con textos con minusculas
    original=(str(original)).upper()
    originallist = (str(original)).split("#")
    clave = int(originallist[0])
    #Metodo por si la clave es mayor a la lista || O si es negativa
    while clave > len(alfabeto):
        clave = clave - len(alfabeto)
    while clave < 0:
        clave = clave + len(alfabeto)
    codigo = ""
    #Recorremos letra por letra la lista del texto
    for letra in originallist[1]:
        contador=0
        #Recorremos el alfabeto para encontrar la igualdad con cada una de las letras del texto
        for caracter in alfabeto:
            if letra==caracter:
                contador=(contador+clave)%len(alfabeto)
                codigo=codigo+alfabeto[contador]
                break
            contador+=1
    pos=0
    codigo=list(codigo)
    #Recorremos el texto por posiciones
    while pos!=len(codigo):
        contador=0
        #Recorremos el alfabeto, queremos encontrar la igualdad con cada letra y las que sean multiplos de 2
        for caracter in alfabeto:
            if codigo[pos]==caracter and pos%2==0:
                contador=(contador-clave)%len(alfabeto)
                codigo[pos]=alfabeto[contador]
                break
            contador+=1
        pos+=1
    codigofinal=""
    #Metodo para escribir en string nuestro codigo en lista
    for i in codigo:
        codigofinal=codigofinal+i
    return codigofinal

def muestra_original(original): 
    print(original)
    return 
#Creacion del archivo 
def muestra_codificado(original):
    code=original
    archivo=open("codificado.txt", "w")
    archivo.write(code)
    print(original)
    return 
#Lectura del archivo de texto
def lee_secreto(secreto):
    if __name__ == "__main__":
        #abrir el archivo de texto                
        archivo=open("secreto.txt","r")
        #leer el texto del archivo        
        secreto=archivo.read()
    return secreto
#Genera la traduccion del mensaje secreto
def genera_descifrado(secreto): 
    alfabeto=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", ",", ".", ":", ";", "?", "-", "+", "*", "/"] 
    #Para casos con textos con minusculas
    secreto=(str(secreto)).upper()
    secretlist = (str(secreto)).split("#")
    clave = int(secretlist[0])   
    #Metodo por si la clave es mayor a la lista || O si es negativa
    while clave > len(alfabeto):
        clave = clave - len(alfabeto)
    while clave < 0:
        clave = clave + len(alfabeto) 
    codigo=""
    #Recorremos letra por letra la lista del texto
    for letra in secretlist[1]:
        contador=0
        #Recorremos el alfabeto para encontrar la igualdad con cada una de las letras del texto
        for caracter in alfabeto:
            if letra==caracter:
                contador=(contador-clave)%len(alfabeto)
                codigo=codigo+alfabeto[contador]
                break
            contador+=1

    pos=0
    codigo=list(codigo)
    #Recorremos el texto por posiciones
    while pos!=len(codigo):
        contador=0
        #Recorremos el alfabeto, queremos encontrar la igualdad con cada letra y las que sean multiplos de 2
        for caracter in alfabeto:
            if codigo[pos]==caracter and pos%2==0:
                contador=(contador+clave)%len(alfabeto)
                codigo[pos]=alfabeto[contador]
                break
            contador+=1
        pos+=1
    codigofinal=""
    #Metodo para escribir en string nuestro codigo en lista
    for i in codigo:
        codigofinal=codigofinal+i
    return codigofinal

def muestra_secreto(secreto): 
    print(secreto)
    return
#Creacion del archivo 
def muestra_descifrado(secreto): 
    code=secreto
    archivo=open("descifrado.txt", "w")
    archivo.write(code)
    print(secreto)
    return

mensaje_original = lee_original("original.txt") 
muestra_original(mensaje_original) 
mensaje_codificado = genera_codificado(mensaje_original) 
muestra_codificado(mensaje_codificado) 
mensaje_secreto = lee_secreto("secreto.txt") 
muestra_secreto(mensaje_secreto) 
mensaje_decodificado = genera_descifrado(mensaje_secreto) 
muestra_descifrado(mensaje_decodificado) 