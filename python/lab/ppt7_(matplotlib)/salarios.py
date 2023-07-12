import matplotlib.pyplot as plt
import numpy as np

archivo = open("ds_salaries.csv")
#######################################
ejeX=["2023","2022","2021","2020"]
ejeY=[]
promedio2023=[]
promedio2022=[]
promedio2021=[]
promedio2020=[]
for elem in archivo:
    elem=elem.rstrip("\n")
    elemL=elem.split(",")
    pos=0
    for datos in elemL:
        if pos==4 and elemL[0]=="2023":
            promedio2023.append(datos)
        if pos==4 and elemL[0]=="2022":
            promedio2022.append(datos)
        if pos==4 and elemL[0]=="2021":
            promedio2021.append(datos)
        if pos==4 and elemL[0]=="2020":
            promedio2020.append(datos)
        pos+=1
#######################################
suma2023=0
for elemento in promedio2023:
    elemento=int(elemento)
    suma2023+=elemento
suma2022=0
for elemento in promedio2022:
    elemento=int(elemento)
    suma2022+=elemento
suma2021=0
for elemento in promedio2021:
    elemento=int(elemento)
    suma2021+=elemento
suma2020=0
for elemento in promedio2020:
    elemento=int(elemento)
    suma2020+=elemento
#######################################
promedio2023=suma2023//len(promedio2023)
promedio2022=suma2022//len(promedio2022)
promedio2021=suma2021//len(promedio2021)
promedio2020=suma2020//len(promedio2020)
#######################################
ejeY.append(promedio2023)
ejeY.append(promedio2022)
ejeY.append(promedio2021)
ejeY.append(promedio2020)
#######################################
del ejeY[0]
del ejeX[0]
#######################################
plt.plot(ejeX, ejeY)
plt.xlabel('Años')
plt.ylabel('Salario')
plt.show()