import matplotlib.pyplot as plt
import numpy as np

archivo = open("covid19datos.csv")
etiquetas=[]
ejex=[]
ejey=[]
ejey2=[]
ejey3=[]
#######################################
contador=0
for elem in archivo:
    elem=elem.rstrip("\n")
    elemL=elem.split(",")
    pos=0
    if contador!=0 and contador!=18:
        etiquetas.append(elemL[0])
        ejex.append(contador+1)
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
dist=np.arange(len(ejex))
an=len(ejex)/len(ejex)
width=0.4
fig, ax=plt.subplots()
ax.bar(dist+an, ejey3, width, color="g", label="Recuperados")
ax.bar(dist+an/1.3, ejey, width, color="orange", label="Confirmados")    
ax.bar(dist+an/1.6, ejey2, width, color="r", label="Fallecidos")

ax.set_title("Casos confirmados, fallecidos y recuperados")
ax.set_ylabel("Cantidad de personas")
ax.set_xlabel("Regiones")
ax.set_xticks(dist)
plt.legend()

plt.show()