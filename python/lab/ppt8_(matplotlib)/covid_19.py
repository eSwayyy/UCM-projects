import matplotlib.pyplot as plt
import numpy as np

archivo = open("covid19datos.csv")
ejex=[]
ejey=[]
ejey2=[]
ejey3=[]
#######################################
contador=0
for elem in archivo:
    elem=elem.rstrip("\n")
    elemL=elem.split(",")
    if contador!=0:
        ejex.append(elemL[0])
        ejey.append(int(elemL[6]))
        ejey2.append(int(elemL[2]))
        ejey3.append(int(elemL[5]))
    contador+=1
#######################################
#print(ejex)
#print(ejey)
#print(ejey2)
#print(ejey3)
#######################################
plt.plot(ejex, ejey, color="b", label="Confirmados")
plt.plot(ejex, ejey2, color="y", label="Fallecidos")
plt.plot(ejex, ejey3, color="r", label="Recuperados")
plt.grid()
plt.ylabel("y")
plt.xlabel("Regiones")
plt.title("Casos confirmados, fallecidos y recuperados")
plt.legend()
plt.show()