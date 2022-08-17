horas=int(input("ingrese el nuemro de horas trabajadas: "))
    
if horas>40:
    horas_extra=horas-40
    salario=horas_extra*20000+(40*16000)
else:
    salario=horas*16000
    
print(" el salario del empleado es: "+str(salario))