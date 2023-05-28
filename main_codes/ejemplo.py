ejemplo = "hola. como. estan"
lista = ejemplo.split(".")

contador= 0

while(contador != len(lista)):
    lista[contador] = lista[contador].capitalize()
    contador+=1

contador=0

string=""
while(contador != len(lista)):
    string=string+lista[contador]+". "
    contador= contador+1
print(string)