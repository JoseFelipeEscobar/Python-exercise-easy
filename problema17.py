# NO hay informacion del precio unitario de las camisas 
#establezco el precio en $30000
n=int(input("ingrese el nuemro de camisas a comprar: "))
precio=30000
compra=n*30000
if n>=3:
    descuento=compra*0.2
    total=compra-descuento
else:
    descuento=compra*0.1
    total=compra-descuento
    

print(" el valor de la compra es: $"+str(compra))
print(" el descuento  es de: $"+str(descuento))
print(" el valor a pagar es: $"+str(total))