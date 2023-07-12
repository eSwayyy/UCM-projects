'''
2) Una persona desea invertir su dinero en un banco, el cual le otorga un 2%
de interés. Cual será la cantidad de dinero que esta persona tendrá al cabo de
un año si la ganancia de cada mes es reinvertida?.
'''

dinero = int(input("Cuanto dinero desea invertir: "))
tiempo = int(input("Durante cuanto tiempo dese invertir (en meses): "))
i = 0
while i < tiempo:
    dinero = dinero * 1.02
    i = i + 1
print("al cabo de", tiempo, "meses, tendra", dinero, "$")