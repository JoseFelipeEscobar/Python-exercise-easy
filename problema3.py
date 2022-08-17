# agrego un comentario para definir datos
print("escriba el sexo del pasajero, m si es masculino y f si es femenino")

sexo=input(" escriba (m o f): ")
equipaje=int(input("lleva equipaje (SI: 1  NO: 0): "))

peso=0
if (equipaje==1):
    peso = int(input("ingrese el peso del equipaje"))
    
total=pasaje_basico=425000

if (sexo=="m" or sexo=="M"):
    if peso>0 and peso<=50:
        total=pasaje_basico*(1.25)
    if peso>50:
        total=pasaje_basico*(1.35)
   
    
    
if (sexo=="f" or sexo=="F"):
    if peso>0 and peso<=50:
        total=pasaje_basico*(1.2)
    if peso>50:
        total=pasaje_basico*(1.3)
    
        
print(f"el costo del pasaje es: {total}")
