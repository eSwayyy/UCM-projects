'''Definir una función es_palindromo() que reconoce palíndromos (es decir,
palabras que tienen el mismo aspecto escritas invertidas), ejemplo:
es_palindromo ("radar") tendría que devolver True. '''

def es_palindromo(pal,indromo):
    pal=list(pal)
    indromo=list(indromo)
    indromo.reverse()
    if pal==indromo:
        print(True)
    else:
        print(False)
    return

pal=input("Ingrese una palabra:\n")
indromo=pal

es_palindromo(pal,indromo)