
cafe=0
libros_comprados=int(input("ingrese # de libros comprados: "))

if libros_comprados<=5:
    print("lo sentios no plica la oferta para su compra")
elif (libros_comprados>=5 and libros_comprados<12):
    cafe=1
    print("por su compra usted recibe  1 bolsa de cafe ")
elif libros_comprados>=12:
    cafe=libros_comprados//4
    print("por su compra usted recibe 1 botella de vino y "+str(cafe)+" bolsas de cafe ")
