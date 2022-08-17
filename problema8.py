nombre=input("ingrese su nombre: ")
estatura=float(input("ingrese su estatura: "))
peso=float(input("ingrese su peso: "))
imc=peso/(estatura**2)

if imc<18.5:
    print(nombre+" su idice de masa corporal es "+str(round(imc,2))+" peso por debajo de lo normal")
    
if imc>=18.5 and imc<25:
    print(nombre+" su idice de masa corporal es "+str(round(imc,2))+" peso  normal")
if imc>=25 and imc<30:
    print(nombre+" su idice de masa corporal es "+str(round(imc,2))+" sobrepeso ")
if  imc>=30:
    print(nombre+" su idice de masa corporal es "+str(round(imc,2))+" obesidad")