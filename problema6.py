
comedor1=int(input("ingrese la cantidad de comedores tipo 1 solicitados : "))
comedor2=int(input("ingrese la cantidad de comedores tipo 2 solicitados: "))
costo_pintura=150000
sillas=(comedor1*4+comedor2*6)

costo_carpintero1=sillas*25000+ sillas*3000+ 150000

costo_carpintero2=40000*sillas

print("el costo de las sillas con el carpintero 1 es: $"+str(costo_carpintero1)+ " \nel costo de las sillas con el carpintero 2 es: $"+str(costo_carpintero2))
if costo_carpintero1<costo_carpintero2:
    print("se recomienda a la muebleria que escoja al carpinetero 1 ")

else:
    print("se recomienda a la muebleria que escoja al carpinetero 2 ")