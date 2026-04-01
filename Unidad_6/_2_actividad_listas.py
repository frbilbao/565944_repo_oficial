
"""
CONSIGNA
Dada una lista de temperaturas registradas durante una semana:
temperaturas = [22, 24, 19, 23, 25, 21, 20]

Desarrollar un programa que:

Muestre todas las temperaturas
Calcule y muestre:
Temperatura promedio
Temperatura máxima
Temperatura mínima
Indique cuántos días la temperatura fue mayor a 22 grados

💡 Pistas
Usar for para recorrer la lista
Usar acumuladores (suma, contador)
Opcional: usar funciones como max() y min()
"""

temperaturas = [22, 24, 19, 23, 25, 21, 20]

# Mostrar todas las temperaturas
print("Temperaturas de la semana:")
for temperatura in temperaturas:
    print(temperatura)

# Calcular promedio
suma = 0
for temperatura in temperaturas:
    suma = suma + temperatura
promedio = suma / len(temperaturas)
print("Temperatura promedio:", promedio)

# Temperatura máxima y mínima
print("Temperatura máxima:", max(temperaturas))
print("Temperatura mínima:", min(temperaturas))

# Contar días con temperatura mayor a 22
contador = 0
for temperatura in temperaturas:
    if temperatura > 22:
        contador = contador + 1
print("Días con temperatura mayor a 22:", contador)