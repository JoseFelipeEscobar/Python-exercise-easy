sueldo=0
periodico1=int(input("cuantos periodicos de tipo I vendio el repartidor: "))
periodico2=int(input("cuantos periodicos de tipo II vendio el repartidor: "))
periodicos_vendidos=periodico1+periodico2
bono1=(periodico1//10)*15000
bono2=(periodico2//10)*10000
sueldo=periodicos_vendidos*1000 + bono1 + bono2
print("el sueldo diario del repartidor es: "+str(sueldo))
