import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    fig, ax = plt.subplots(2,1) #Se pueden agregar parámetros como sharex y sharey
    fig.set_size_inches(4,4)

    #Información para primer gráfico x^2
    x=np.arange(-10,11,1)
    y=x**2
    ax[0].plot(x,y)

    #Información para segundo gráfico x^3
    x=np.arange(-10,11,1)
    y=x**3
    ax[1].plot(x,y)

    plt.show()
