'''
Programe un algoritmo en Python, tal que sea capaz de resolver el
coeficiente binomial de n sobre k, el cual está determinado por la siguiente
ecuación:
'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

n = int(input('Ingrese su valor "n"\n'))
k = int(input('Ingrese su valor "k"\n'))

resta=n-k
i=n
while i > 1:
    n = n * (i-1)
    i=i-1

i2=k
while i2 > 1:
    k = k * (i2-1)
    i2=i2-1

i3=resta
if resta ==1:
    combinatoria = n/(k*(resta))
    print("La combinatoria es: ", combinatoria)
else:
    while i3 > 1:
        resta = resta * (i3-1)
        i3=i3-1
    print(n,k, resta)
    combinatoria = n/(k*(resta))    
    print("La combinatoria es: ", combinatoria)