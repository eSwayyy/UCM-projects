#Programa que lee un archivo
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    archivo=open("population.csv")
    for elem in archivo:
        elem=elem.rstrip("\n")
        elemL=elem.split(",")
        print(elemL)