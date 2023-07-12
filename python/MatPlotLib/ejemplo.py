#Programa que lee un archivo csv

if __name__ == "__main__":
    archivo=open("population.csv")
    for elem in archivo:
        print(elem)
