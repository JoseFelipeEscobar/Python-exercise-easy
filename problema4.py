num_hijos=int(input("cuantos hijos tienes: "))
estrato=int(input("ingrese su estrato (1 2 3 4 5 6): "))


if estrato <=2 : 
    viuda=input("es viuda SI o NO (S o N)")   
    if num_hijos<=3:
        subsidio=120000
    elif num_hijos>3:
        subsidio=180000
        
    if viuda=="s" or viuda=="S":
        subsidio=subsidio+50000
        
    print("el dinero que recibira por el subsidio es: $" + str(subsidio))

else:
    print("usted no hace parte de del programa")