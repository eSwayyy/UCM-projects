#Programa que convierte una cantidad de segundos a horas, minutos y segundos | Ejercicio 6 ppt1

print("Ingrese la cantidad de segundos")
segundos=int(input())
horas= segundos//3600

minutos= segundos%3600
minutos= minutos//60

segundos2= minutos%60

print("Tienes", horas, "horas con", minutos, "minutos con", segundos2, "segundos")