compra=int(input("ingrese el valor de la compra: "))
estrato=int(input("cuanl es su estrato (1 2 3 4 5 6): "))
edad=int(input("ingrese su edad: "))
precio_final=compra
if estrato==1:
    if edad<60:
        precio_final=compra*0.85
    else:
        precio_final=compra*0.75
    print("el precio de la compra es "+str(precio_final))
elif estrato==2:
    if edad<60:
        precio_final=compra*0.9
    else:
        precio_final=compra*0.8
    print("el precio de la compra es "+str(precio_final))
else:
    print("no pertenece a una comunidad vulnerable el valor total es "+str(precio_final))