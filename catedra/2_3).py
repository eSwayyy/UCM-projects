'''
1) En un supermercado se hace una promoción, mediante la cual el cliente
obtiene un descuento dependiendo de un numero que se escoge al azar. Si
el numero escogido es menor que 74 el descuento es del 15% sobre el total
de la compra, si es mayor o igual a 74 el descuento es del 20%. Obtener
cuanto dinero se le descuenta.
'''

boleta = int(input("¿Cual es el total de su boleta?: "))
numero = int(input("Digite un numero al azar: "))
if numero < 74:
    boleta = boleta * 0.85
    print("Su precio final es: ", boleta)
else:
    boleta = boleta * 0.8
    print("Su precio final es: ", boleta)
