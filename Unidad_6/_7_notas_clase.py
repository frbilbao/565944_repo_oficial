
# Declaro
matriz = [[1, 3, 2], [3, 5, 1]]

# Mostar la matriz en la consola mediante un bucle
print(f"La matriz es mediante un bucle:")
for fila in matriz:
    print(fila)



import random
def matriz_random(n_filas, n_columnas):
    matriz = []
    for _ in range(n_filas):
        fila = []
        for _ in range(n_columnas):
            fila.append(random.randint(0, 9))  # Agrega un número aleatorio entre 0 y 9
        matriz.append(fila)
    return matriz

m_random = matriz_random(3,2)
print(m_random)