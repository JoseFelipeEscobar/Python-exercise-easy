a=float(input("ingrese la longitud del lado a: "))
b=float(input("ingrese la longitud del lado b: "))
c=float(input("ingrese la longitud del lado c: "))

if (a**2+b**2==c**2) or (a**2==b**2+c**2) or (a**2+c**2==b**2):
    print("el triangulo es rectangulo")
else:
    print("el triangulo no esrectangulo")