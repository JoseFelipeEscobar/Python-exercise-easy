# Este es el juego de adivinar el número
#autor: Lorena Negrete 
# @version 1.0.0

#se hace la importacion de librerias requeridas 
import random
import os


#se inicializan las variables
intentosrealizados=0 #variable contadora del numero de intentos realizados de adivinar el numero
vidas=0 #variable que almcaena la candtidad de intentos permitidos
dificultad=0 #variable que almacena elnivel de dificultad
numero=0 #variable que almacena el numero a adivinar
estimacion=0 #variable que almacena el numero ingresado para comprobar si el numero que hay que adivinar
nombre="" #variable que almacena el nombre del usuario

#se muestra mensaje de saludo al usuario
print("Hola! ¿Como te llamas? ")
nombre = input()
#se muestra un mensaje de bienvenida y las opciones del nivel de dificultad del juego
print("\n====== "+nombre+""" bienvenid@ a adivina el numero ======
====== nivel de dificultad ===========
      
      1.--- facil   6 intentos
      2.--- medio   4 intentos
      3.--- dificil 3 intentos
      """)
#se procede a capturar la opcion que va escoger el usuario para el nivel de dificultad 
dificultad=int(input("ingrese el nivel de dificultad elegido: "))

#se utiliza el bucle por si el usuario no ingresa un numero valido para el nivel de dificultad
while dificultad!=1 and dificultad!=2 and dificultad!=3 : 
    print("numero invalido, las opciones son: (1 ,2 , 3)")
    dificultad=int(input("ingrese el nivel de dificultad elegido: "))

#esta linea limpia la consola de python 
os.system("cls")


if (dificultad==1):
    vidas=6
elif (dificultad==2):
    vidas=4
else:
    vidas=3
#aqui se obtiene el numero aleatorio
numero=random.randint(1,20)
#se informa al jugador los intentos que tiene para adivinar el numero 
print( "\nBueno,  " + nombre +  ", estoy pensando en un numero entre 1 y 20. ")
print("tienes "+str(vidas)+" intentos")
print(""" 
====== buena suerte ======""")

#aqui se verificca si tiene vidas para intentar adivinar el numero
while intentosrealizados < vidas:

    estimacion=int(input("\nIntenta adivinar el numero que yo pense: "))

    intentosrealizados=intentosrealizados + 1
    if estimacion < numero:
        print( "Tu estimacion es muy baja. ") 

    if estimacion > numero:
        print( "Tu estimacion es muy alta. ")

    if estimacion == numero:
         break

#si el numero que ingresamos es el numero aleatorio  se muesta un mensaje donde se diga que gano
if estimacion == numero:
    intentosrealizados = str(intentosrealizados)
    print( "\n¡Buen trabajo, ganaste " + nombre +  "! ¡Has adivinado mi numero en  " + intentosrealizados +  " intentos! ")

#si el numero que ingresamos es el numero aleatorio  se muesta un mensaje donde diga que perdio
if estimacion != numero:
    numero = str(numero)
    print( "perdiste. El numero que estaba pensando era  " + numero)
    
#esta linea hace que el sistema espera hasta que oprimas una tecla para cerrarse
os.system("pause")
