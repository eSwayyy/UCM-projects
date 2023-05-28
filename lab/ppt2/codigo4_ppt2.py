#Programa para resolver ecuaciones cuadraticas

from math import sqrt
print("¿Cual es su coeficiente a?")
a=float(input())
print("¿Cual es su coeficiente b?")
b=float(input())
print("¿Cual es su coeficiente c?")
c=float(input())

disc=(b**2) - (4*a*c)
disc2=disc
disc= sqrt(disc)
x1=(-b+disc)/2*a
x2=(-b-disc)/2*a

if (disc2>0):
 print("Las soluciones de tu ecuacion son", x1, "y", x2)
if (disc2==0):
  print("Las soluciones de tu ecuacion son", x1, "y", x2) 