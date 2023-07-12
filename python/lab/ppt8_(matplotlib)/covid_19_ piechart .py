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
ax.pie(ejey, labels=etiquetas, autopct="%0.1f %%")
ax.set_title("Casos confirmados")
plt.legend(loc='lower right')
plt.show()