# NO hay informacion del precio unitario de libros 
#establezco el precio en $20000
libros=int(input("ingrese la cantidad de libros a comprar: "))
precio_libro=20000
compra=0

if libros>12:
    compra=libros*precio_libro
    descuento=compra*0.1
    total=compra-descuento
else:
    compra= libros*precio_libro
    descuento= compra*0.1
    total= compra-descuento
print(" el valor de la compra es: $"+str(compra))
print(" el descuento  es de: $"+str(descuento))
print(" el valor a pagar es: $"+str(total))