"""
Julieta Núñez Pacheco
19 de septiembre de 2025
Este ejercicio calcula el sueldo semanal según las horas y
tarifa proporcionada
"""

# Entradas

horas = int(input("Horas trabajadas: "))
tarifa = int(input("Tarifa por hora: "))

# Proceso

if horas > 48:
    h_extra = horas - 48
    sh_extra = h_extra * tarifa * 2
    sueldo = (tarifa * 48) + sh_extra
else: 
    h_extra = 0 
    sh_extra = 0 
    sueldo = tarifa * horas

# Salidas

print("Horas extras: " + str(h_extra))
print("Sueldo por hora extras: " + str(sh_extra))
print("Sueldo semanal: " + str(sueldo))
