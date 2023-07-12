#Programa que tratará de realizar un análisis sobre un set de datos y graficar
import matplotlib.pyplot as plt
import numpy as np

def graficar(ejeX, ejeY):
    plt.plot(ejeX, ejeY, linewidth=4, color=(0.5,0,0.5)) 
    plt.xlabel('Año')
    plt.ylabel('cantidad de juegos lanzados')
    plt.title('Juegos de Nintendo lanzados por año')
    plt.grid()
    plt.show()

if __name__ == "__main__":

    ejeX=[]
    ejeY=[]
    datos=[]
    archivo=open("df_4.csv", encoding="utf8")
    ciclo=0
    for elem in archivo:
        elem=elem.rstrip("\n")
        elemL=elem.split(",")
        i=0
        while(i<len(elemL)):
            if(i==2 and ciclo!=0):
                elemL[i]=elemL[i].lstrip("August ")
                datos.append(elemL[i][0:4])
            i=i+1
        print(datos)
        ciclo=ciclo+1
    
    ejeX=sorted(list(set(datos)))
    ejeY=[]
    ciclo=0
    for elem in ejeX:
        ejeY.append(0)
        for elem2 in datos:
            if(elem.count(elem2)):
                ejeY[ciclo]=ejeY[ciclo]+1
        
        ejeX[ciclo]=int(ejeX[ciclo])
        ciclo=ciclo+1

    print(ejeX)
    print(ejeY)
    graficar(ejeX,ejeY)