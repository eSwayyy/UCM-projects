#Programa que tratará de realizar un análisis sobre un set de datos y graficar
import matplotlib.pyplot as plt
import numpy as np

def graficar(ejeX,ejeY):
    plt.bar(ejeX,ejeY) 
    plt.xlabel('Año')
    plt.ylabel('cantidad de juegos lanzados')
    plt.title('Juegos de Nintendo lanzados por año')
    plt.show()

if __name__ == "__main__":

    ejeX=[]
    ejeY=[]
    datos=[]
    archivo=open("df_5.csv", encoding="utf8")
    ciclo=0
    for elem in archivo:
        elem=elem.rstrip("\n")
        elemL=elem.split(",")
        i=0
        while(i<len(elemL)):
            if(i==3 and ciclo!=0 and elemL[i].startswith("Nove")==False and elemL[i].startswith("Unk")==False):
                datos.append(elemL[i][0:4])
            i=i+1
        print(datos)
        ciclo=ciclo+1
    
    ejeX=list(set(datos))
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