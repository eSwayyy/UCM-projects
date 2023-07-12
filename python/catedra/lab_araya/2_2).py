'''
4) Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si
se compran tres camisas o más se aplica un descuento del 20% sobre el
total de la compra y si son menos de tres camisas un descuento del 10%
'''

print("Las camisas cuestan 1000$")
camisas = int(input("Cuantas camisas va a comprar?: "))

if camisas >= 3:
    camisas = (camisas * 1000) * 0.8
else: 
    camisas = (camisas * 1000) * 0.9

print("El precio por el total de camisas es: ", camisas)