import random

def generar_partida(n_filas, n_columnas):
    matriz = []
    for _ in range(n_filas):
        fila = []
        for _ in range(n_columnas):
            fila.append("💣" if random.randint(0, 1) == 1 else "⬜")
        matriz.append(fila)
    return matriz


def generar_tablero_visible(n_filas, n_columnas):
    matriz = []
    for _ in range(n_filas):
        fila = []
        for _ in range(n_columnas):
            fila.append("❓")
        matriz.append(fila)
    return matriz


def mostrar_tablero(matriz):
    print("\nTABLERO:")

    print("   ", end="")
    for col in range(len(matriz[0])):
        print(col, end=" ")
    print()

    for i in range(len(matriz)):
        print(i, end="  ")
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()


def posicion_valida(fila, columna, max_filas, max_columnas):
    return 0 <= fila < max_filas and 0 <= columna < max_columnas


def quedan_casillas_seguras(tablero, visible):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == "⬜" and visible[i][j] == "❓":
                return True
    return False


def jugar():
    tablero = generar_partida(5, 5)
    visible = generar_tablero_visible(5, 5)

    filas = len(tablero)
    columnas = len(tablero[0])
    score = 0

    while True:
        mostrar_tablero(visible)

        try:
            fila = int(input("\nIngresá una fila: "))
            columna = int(input("Ingresá una columna: "))
        except ValueError:
            print("\nTenés que ingresar números.")
            continue

        if posicion_valida(fila, columna, filas, columnas):
            if visible[fila][columna] != "❓":
                print("\nYa descubriste esa celda.")
            elif tablero[fila][columna] == "💣":
                visible[fila][columna] = "💣"
                mostrar_tablero(visible)
                print("\nPerdiste. Encontraste una bomba.")
                print("Tu score fue:", score)
                break
            else:
                visible[fila][columna] = "✅"
                score += 1
                print("\nSafaste. Sumaste un punto.")
                print("Score actual:", score)

                if not quedan_casillas_seguras(tablero, visible):
                    mostrar_tablero(visible)
                    print("\n¡Ganaste! Descubriste todas las casillas seguras.")
                    print("Score final:", score)
                    break
        else:
            print("\nPosición inválida.")


jugar()