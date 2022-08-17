xnota1=float(input("ingrese la nota 1: "))
nota2=float(input("ingrese la nota 2: "))
nota3=float(input("ingrese la nota 3: "))
promedio=0

if nota1>nota2 and nota2>nota3:
    if nota2>=nota3:
        promedio =(nota1+nota2)/2
    else:
        promedio=(nota1+nota3)/2
        
if nota3>=nota2 and nota3>=nota1:
    if nota1>=nota2:
        promedio =nota3+nota1/2
    else:
        promedio=(nota3+nota2)/2
if nota1==nota2 or nota2=nota3:

        
print("el promedio es: "+str(promedio))

