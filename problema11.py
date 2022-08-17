n1= int(input("ingrese un numero : "))
n2= int(input("ingrese un numero: "))
n3= int(input("ingrese un numero: "))

if n1==n2 or n1==n3 or n2==n3:
    print("error hay dos numeros iguales")
else:
    if n1<n2 and n1<n3:
        if n2<n3:
            print(n1 , n2, n3)
        else:
            print(n1 , n3, n2)
    
    if n2<n1 and n2<n3:
        if n1<n3:
            print(n2,n1,n3 )
        else:
            print(n2,n3,n1)
    if n3<n1 and n3<n2:
        if n1<n2:
            print(n3,n1,n2)
        else:
            print(n3,n2,n1)
