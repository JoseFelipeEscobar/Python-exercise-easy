edad=int(input("ingrese su edad: "))
sexo=input(" escriba su sexo (m o f): ")

if (sexo=="m" or sexo=="M"):
    pulsaciones=(210-edad)/10
    print(" sus pulsaciones deberian ser:"+str(pulsaciones))
    
if (sexo=="f" or sexo=="F"):
    pulsaciones=(220-edad)/10
    print(" sus pulsaciones deberian ser:"+str(pulsaciones))