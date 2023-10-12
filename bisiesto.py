"""
Diseña un programa para determinar si un año es o no bisiesto.
 750722
"""

#Entardas
anio = int(input("Ingrese el año que deseé: "))

#Procesos
if anio % 4 == 0:
    print(f"{anio} sí es un año bisiesto" )
elif anio % 100 == 0:
    print("El año es secular")
else:
    print(f"{anio} no es un año bisiesto")

