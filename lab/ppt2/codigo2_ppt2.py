#Calculadora de areas, perimetros y diagonal

import math

print("Digite la base del rectangulo:")
base=float(input())

print("Digite la altura del rectangulo:")
altura=float(input())

area=base * altura
perimetro= 2 * (base + altura)
diagonal=(base * base) + (altura * altura)
diagonal= math.sqrt(diagonal)

print("El area del rectangulo es\n", area)
print("El perimetro del rectangulo es\n", perimetro)
print("La diagonal del rectangulo es\n", diagonal)