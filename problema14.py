palabra=input("ingrese una palabra para saber el tamaño: ")
invalido=False
if invalido==False:
    if len(palabra)<4:
        print("es una palabra pequeña ")
    if len(palabra)>=4 and len(palabra)<=8:
        print("es una palabra mediana ")
    if len(palabra)>8:
        print("es una palabra grande ")