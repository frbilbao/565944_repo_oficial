
"""
CONSIGNA:
Una tienda registra las ventas de 3 productos durante 4 días. La información se guarda en una matriz:

ventas = [
    [10, 12, 8, 9],   # Producto 1
    [5, 7, 6, 8],     # Producto 2
    [15, 14, 13, 16]  # Producto 3
]

Desarrollar un programa que:

Muestre la matriz de ventas
Calcule:
1. Total vendido por cada producto
2. Total vendido por cada día
3. Indique:
Qué producto fue el más vendido (en total)

💡 Pistas
Usar dos for (uno para filas, otro para columnas)
Pensar:
Filas → productos
Columnas → días
"""

ventas = [
    [10, 12, 8, 9],   # Producto 1
    [5, 7, 6, 8],     # Producto 2
    [15, 14, 13, 16]  # Producto 3
]

# Mostrar la matriz de ventas
print("Matriz de ventas:")
for fila in ventas:
    print(fila)

# Total vendido por cada producto
print("\nTotal por producto:")
for i in range(len(ventas)):
    total = 0
    for j in range(len(ventas[i])):
        total = total + ventas[i][j]
    print(f"Producto {i + 1}: {total}")

# Total vendido por cada día
print("\nTotal por día:")
for j in range(len(ventas[0])):
    total = 0
    for i in range(len(ventas)):
        total = total + ventas[i][j]
    print(f"Día {j + 1}: {total}")

# Producto más vendido
mayor_total = 0
producto_mas_vendido = 0
for i in range(len(ventas)):
    total = 0
    for j in range(len(ventas[i])):
        total = total + ventas[i][j]
    if total > mayor_total:
        mayor_total = total
        producto_mas_vendido = i + 1
print(f"\nProducto más vendido: Producto {producto_mas_vendido} con {mayor_total} unidades")

