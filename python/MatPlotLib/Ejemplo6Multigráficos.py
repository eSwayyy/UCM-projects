
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    x = np.arange(0,10,0.2)
    y1 = np.cos(x)
    y2 = np.sin(x)
    y3 = np.tan(x)

    plt.plot(x,y1,'o',linewidth=5,color="y")
    plt.plot(x,y2, "*",linewidth=6,color='b')
    plt.plot(x,y3, "-",linewidth=3,color='r')
    plt.grid()
    #plt.axis("equal")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráfico de funciones seno y coseno")
    plt.show()

