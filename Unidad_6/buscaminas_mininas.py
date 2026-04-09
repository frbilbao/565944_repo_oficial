# Tamaño del tablero
filas = 5
columnas = 5
minas = 5

# Crear tablero vacío
tablero = []
visible = []

for i in range(filas):
    fila = []
    fila_visible = []
    for j in range(columnas):
        fila.append(0)
        fila_visible.append("-")
    tablero.append(fila)
    visible.append(fila_visible)

# Colocar minas manualmente (para evitar random)
tablero[0][1] = "*"
tablero[2][3] = "*"
tablero[3][0] = "*"
tablero[4][4] = "*"
tablero[1][2] = "*"

# Función para contar minas cercanas
def contar_minas(fila, col):
    contador = 0
    for i in range(fila - 1, fila + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and i < filas and j >= 0 and j < columnas:
                if tablero[i][j] == "*":
                    contador += 1
    return contador

# Mostrar tablero visible
def mostrar():
    print("\nTablero:")
    for i in range(filas):
        for j in range(columnas):
            print(visible[i][j], end=" ")
        print()

# Juego principal
jugando = True

while jugando:
    mostrar()
    
    fila = int(input("Ingrese fila (0-4): "))
    col = int(input("Ingrese columna (0-4): "))
    
    if tablero[fila][col] == "*":
        print("💥 PERDISTE! Pisaste una mina")
        jugando = False
    else:
        minas_cerca = contar_minas(fila, col)
        visible[fila][col] = minas_cerca
        
        # Verificar si ganó (descubrió todas menos minas)
        casillas_descubiertas = 0
        for i in range(filas):
            for j in range(columnas):
                if visible[i][j] != "-":
                    casillas_descubiertas += 1
        
        if casillas_descubiertas == (filas * columnas - minas):
            print("🎉 GANASTE!")
            jugando = False