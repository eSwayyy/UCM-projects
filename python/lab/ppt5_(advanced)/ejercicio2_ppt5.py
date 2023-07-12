'''
Realice un programa en Python, tal que, solicite al usuario un número natural y a
continuación devuelva su equivalente en base binaria.
'''
import os
if os.name == "posix":
    os.system('clear')
else:
    os.system('cls')

num=int(input("Digite un numero natural:\n"))
numlist=[]
while num>0:
    resto= num%2
    num= num//2
    numlist.append(resto)
    print(".")
numlist.reverse()
print(numlist)