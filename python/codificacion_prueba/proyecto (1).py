#Nombres: Bárbara Concha y Pablo Cáceres
#Sección 1

# Función para leer el contenido de un archivo
def archivo_original(nombre_archivo):
    archivo = open(nombre_archivo, 'r')  # Abre el archivo en modo lectura
    contenido = archivo.read().strip()  # Lee el contenido y lo guarda en 'contenido'
    archivo.close()  # Cierra el archivo
    return contenido  # Devuelve el contenido

# Función para leer el contenido de un archivo
def archivo_secreto(nombre_archivo):
    archivo = open(nombre_archivo, 'r')  # Abre el archivo en modo lectura
    contenido = archivo.read().strip()  # Lee el contenido y lo guarda en 'contenido'
    archivo.close()  # Cierra el archivo
    return contenido  # Devuelve el contenido

# Función para generar el mensaje codificado
def archivo_codificado(archivo_ocupado):
    abcedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", ",", ".", ":",";", "?", "-", "+", "*", "/"]

    recorrido = int(archivo_ocupado.split("#")[0])  # Obtiene el desplazamiento
    msj = archivo_ocupado.split("#")[1]  # Obtiene el mensaje
    msj = msj.upper() #Coloca todos los caracteres del string en mayúscula
    mensaje_codificado = str()  # Variable para almacenar el mensaje codificado

    C = 0  # Contador para determinar si se aplica desplazamiento adicional

    for i in msj:
        if i in abcedario:  # Verifica si el caracter está en el alfabeto
            lugar = abcedario.index(i)  # Obtiene la posición del caracter en el alfabeto
            nuevo_lugar = (lugar + recorrido)  # Calcula la nueva posición aplicando el desplazamiento

            if abs(nuevo_lugar) >= len(abcedario):  # Verifica si se debe aplicar un desplazamiento adicional
                nuevo_lugar = abs(nuevo_lugar) % len(abcedario)

            if (C) % 3 == 0:  # Aplica un desplazamiento adicional cada 3 caracteres
                if abs(nuevo_lugar+recorrido) >= len(abcedario):
                    nuevo_lugar = (
                        (abs(nuevo_lugar+recorrido)) % len(abcedario))
                    mensaje_codificado += abcedario[nuevo_lugar]
                else:
                    mensaje_codificado += abcedario[nuevo_lugar + recorrido]
            else:
                mensaje_codificado += abcedario[nuevo_lugar]

        C += 1  # Incrementa el contador

    texto = open("codificado.txt", "w")  # Abre el archivo "codificado.txt" en modo escritura
    texto.write(str(recorrido)+"#"+mensaje_codificado)  # Escribe el desplazamientoy el mensaje codificado en el archivo
    texto.close()  # Cierra el archivo
    return mensaje_codificado  # Devuelve el mensaje codificado

# Función para generar el mensaje descifrado
def archivo_descifrado(lo_rescatado_del_archivo):
    abcedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", ",", ".", ":",";", "?", "-", "+", "*", "/"]
   
    
    recorrido_2 = int(lo_rescatado_del_archivo.split("#")[0])  # Obtiene el desplazamiento
    msj_2 = lo_rescatado_del_archivo.split("#")[1]  # Obtiene el mensaje
    msj_2 = msj_2.upper() #Coloca todos los caracteres del string en mayúscula
    mensaje_descifrado = str()  # Variable para almacenar el mensaje descifrado

    C2 = 0  # Contador para determinar si se aplica desplazamiento adicional

    for i in msj_2:
        if i in abcedario:  # Verifica si el caracter está en el alfabeto
            lugar_2 = abcedario.index(i)  # Obtiene la posición del caracter en el alfabeto
            nuevo_lugar_2 = (lugar_2 - recorrido_2)  # Calcula la nueva posición aplicando el desplazamiento

            if abs(nuevo_lugar_2) >= len(abcedario):  # Verifica si se debe aplicar un desplazamiento adicional
                nuevo_lugar_2 = nuevo_lugar_2 % len(abcedario)

            if (C2) % 3 == 0:  # Aplica un desplazamiento adicional cada 3 caracteres
                if abs(nuevo_lugar_2-recorrido_2) >= len(abcedario):
                    nuevo_lugar_2 = (
                        ((nuevo_lugar_2-recorrido_2)) % len(abcedario))
                    mensaje_descifrado += abcedario[nuevo_lugar_2]
                else:
                    mensaje_descifrado += abcedario[nuevo_lugar_2 - recorrido_2]
            else:
                mensaje_descifrado += abcedario[nuevo_lugar_2]

        C2 += 1  # Incrementa el contador

    texto2 = open("decodificado.txt", "w")  # Abre el archivo "decodificado.txt" en modo escritura
    texto2.write(str(recorrido_2)+"#"+mensaje_descifrado)  # Escribe el desplazamiento y el mensaje descifrado en el archivo
    texto2.close()  # Cierra el archivo
    return mensaje_descifrado  # Devuelve el mensaje descifrado

# Funciones para mostrar los mensajes en la consola
def muestra_original(mensaje):
    print("Mensaje original:", mensaje)

def muestra_codificado(mensaje):
    print("Mensaje codificado:", mensaje)

def muestra_secreto(mensaje):
    print("Mensaje secreto:", mensaje)

def muestra_descifrado(mensaje):
    print("Mensaje descifrado:", mensaje)

if __name__ == "__main__":
    mensaje_original = archivo_original("original.txt")  # Lee el contenido del archivo "original.txt"
    muestra_original(mensaje_original)  # Muestra el mensaje originalen la consola.

    mensaje_codificado = archivo_codificado(mensaje_original)  # Genera el mensaje codificado a partir del mensaje original
    muestra_codificado(mensaje_codificado)  # Muestra el mensaje codificado en la consola

    mensaje_secreto = archivo_secreto("secreto.txt")  # Lee el contenido del archivo "secreto.txt"
    muestra_secreto(mensaje_secreto)  # Muestra el mensaje secreto en la consola

    mensaje_decodificado = archivo_descifrado(mensaje_secreto)  # Genera el mensaje descifrado a partir del mensaje secreto
    muestra_descifrado(mensaje_decodificado)  # Muestra el mensaje descifrado en la consola