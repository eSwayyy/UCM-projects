'''
● El reloj de los 7 segmentos: Tenemos un reloj de 7 segmentos
led, cada segundo ciertos segmentos encienden, mostrando
una cantidad determinada de tiempo.
● A las 00:00:00, se encienden 2x2 + 6x6 = 40 leds encendidos.
● Considerar que en cada segundo, para realizar el cambio de
número, el reloj se apaga por un instante infinitesimal de
tiempo (no influye en el cálculo).
● ¿Cuántos leds se encienden cuando el reloj marca la hora
ingresada por el usuario?. Por ej: 01:30:23.
'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

hora=input("Ingrese una hora con el formato (00:00:00)\n")
horalista=list(hora)
del horalista[-3]
del horalista[-5]
print(horalista)
led=0
for elemento in horalista:
    if elemento=="0" or elemento=="6" or elemento=="9":
        led= led+6
    if elemento=="1":
        led= led+2
    if elemento=="2" or elemento=="5" or elemento=="3":
        led= led +5
    if elemento=="4":
        led= led +4
    if elemento=="7":
        led= led+3
    if elemento=="8":
        led= led+7
    print(led)
led= led+4
print("Su hora tiene", led, "leds prendidos")