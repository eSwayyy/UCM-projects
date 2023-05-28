#Calculadora salvadora de asignaturas (con numeros enteros)
print("¿Cual fue su primera nota?")
nota1=int(input())
print("¿Cual fue su segunda nota?")
nota2=int(input())
print("¿Cual fue su tercera nota?")
nota3=int(input())
#Algebraicamente nota4 seria x=(40-(ponderacion de las notas))*4
nota4=(40-((nota1*0.25)+(nota2*0.25)+(nota3*0.25)))*4
#Si tus notas ponderan abajo de 30, entonces pierdes la asignatura xD
nota75=((nota1 + nota2 + nota3)/3)*0.75
if (nota75>=40):
    print("necesitas una nota superior a 40")
if (nota75<40):
    print("necesitas un", nota4)
if (nota4>70):
    print("parece que ya valimos compañero")
