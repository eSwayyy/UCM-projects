'''● Textos como "The quick brown fox jumps over the lazy dog" o "El veloz murciélago
hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de
paja". Son "pangramas", textos que contienen todas las letras de un cierto alfabeto,
quizá repetidas.
● Crear un programa que reciba varias frases y que diga si cada una de ellas es un
pangrama o no. Sólo deberás considerar las letras del alfabeto inglés (no considerar
las vocales acentuadas ni la eñe, entre otras), que podrán aparecer en mayúsculas o
en minúsculas.
● Para cada frase deberás responder SI cuando se trate de un pangrama o NO cuando
no lo sea.'''

def pangrama(x):
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    listaInterruptor=[]
    for i in x:
        interruptor=False
        for j in abecedario:
            if j==i:
                interruptor=True
                listaInterruptor.append(interruptor)
    for n in listaInterruptor:
        k=0
        while k!=

ppangrama=input("Ingresar una oracion: \n")
pangrama(ppangrama)