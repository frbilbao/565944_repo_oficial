import random


def pedir_entero(mensaje, minimo):
    valor = int(input(mensaje))
    while valor < minimo:
        print(f"El valor debe ser mayor o igual a {minimo}.")
        valor = int(input(mensaje))
    return valor


def generar_configuracion():
    print("=== CONFIGURACIÓN DE LA PARTIDA ===")

    config = {
        "filas": pedir_entero("Ingresá la cantidad de filas: ", 2),
        "columnas": pedir_entero("Ingresá la cantidad de columnas: ", 2)
    }

    return config


def generar_tablero(config):
    matriz = []

    for _ in range(config["filas"]):
        fila = []
        for _ in range(config["columnas"]):
            if random.randint(0, 1) == 1:
                fila.append("💣")
            else:
                fila.append("⬜")
        matriz.append(fila)

    return matriz


def generar_tablero_visible(config):
    matriz = []

    for _ in range(config["filas"]):
        fila = []
        for _ in range(config["columnas"]):
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


def mostrar_configuracion(config):
    print("\n=== CONFIGURACIÓN ===")
    print("Filas:", config["filas"])
    print("Columnas:", config["columnas"])


def jugar():
    config = generar_configuracion()
    tablero = generar_tablero(config)
    visible = generar_tablero_visible(config)
    score = 0

    mostrar_configuracion(config)

    while True:
        mostrar_tablero(visible)

        fila = pedir_entero("\nIngresá una fila: ", 0)
        columna = pedir_entero("Ingresá una columna: ", 0)

        if posicion_valida(fila, columna, config["filas"], config["columnas"]):
            if visible[fila][columna] != "❓":
                print("\nYa descubriste esa casilla.")
            elif tablero[fila][columna] == "💣":
                visible[fila][columna] = "💣"
                mostrar_tablero(visible)
                print("\nPerdiste. Encontraste una mina.")
                print("Score final:", score)

                print("\nTABLERO REAL:")
                mostrar_tablero(tablero)
                break
            else:
                visible[fila][columna] = "✅"
                score += 1
                print("\nCasilla segura.")
                print("Score actual:", score)

                if not quedan_casillas_seguras(tablero, visible):
                    mostrar_tablero(visible)
                    print("\n¡Ganaste! Descubriste todas las casillas seguras.")
                    print("Score final:", score)

                    print("\nTABLERO REAL:")
                    mostrar_tablero(tablero)
                    break
        else:
            print("\nPosición inválida.")


jugar()