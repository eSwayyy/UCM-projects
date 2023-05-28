#Programa que lee un archivo
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    
    archivo=open("population.csv")
    ciclo=0

    ejeY=[]
    ejeX=[]

    for elem in archivo:
        elem=elem.rstrip("\n")
        elemL=elem.split(",")
        if(ciclo==0):
            posicion=0
            listaCategorias=[]
            for categorias in elemL:
                if(categorias.endswith("Population")==1):
                    categorias=categorias.rstrip(" Population")
                    dato=[posicion,int(categorias)]
                    listaCategorias.append(dato)
                    ejeY.append(0)
                    ejeX.append(int(categorias))
                posicion=posicion+1
            #print(listaCategorias)
            
        else:
            i=0
            while(i<len(listaCategorias)):
                #print(listaCategorias[i][0])
                #print(elemL)
                ejeY[i]=ejeY[i]+int(elemL[listaCategorias[i][0]])
                i=i+1
        ciclo=ciclo+1
        #print(elem)
        
    j=0
    while(j<len(ejeY)):
        ejeY[j]=round(ejeY[j]/ciclo,1)
        j=j+1
    print(ejeX)
    print(ejeY)

    plt.plot(ejeX,ejeY)
    plt.xlabel('Año')
    plt.ylabel('Población')
    plt.title('Tendencia de la población mundial')
    plt.show()