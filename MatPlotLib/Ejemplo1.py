
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    x=np.arange(1,100,1)
    y=(x)**(1/2)

    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.title('Función raíz de x')
    plt.show()

