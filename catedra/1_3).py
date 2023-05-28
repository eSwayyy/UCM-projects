'''
3) Calcular el numero de pulsaciones que una persona debe tener por
cada 10 segundos de ejercicio, si la formula es:
num. pulsaciones = (220 - edad)/10
'''

edad = int(input("¿Cual es su edad?: "))
num_puls = (220 - edad)/10

print("Su numero de pulsaciones cada 10 segundos de ejercicio deberia ser", num_puls)