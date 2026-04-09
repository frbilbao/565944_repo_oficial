# Mini Buscaminas - código base
import random


def generar_partida(n_filas, n_columnas):
    matriz = []
    for _ in range(n_filas):
        fila = []
        for _ in range(n_columnas):
            fila.append("💣" if random.randint(0, 1) == 1 else "⬜")  
        matriz.append(fila)
    return matriz


# Función para mostrar el tablero completo
def mostrar_tablero(matriz):
    print("\nTABLERO:")
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()


# Función para verificar si una posición es válida
def posicion_valida(fila, columna, max_filas, max_columnas):
    return 0 <= fila < max_filas and 0 <= columna < max_columnas


# Función principal del juego
def jugar():
    # generar partida 
    tablero = generar_partida(5,5)
    filas = len(tablero)
    columnas = len(tablero[0])
    score = 0
    mostrar_tablero(tablero)

    while True:
        fila = int(input("\nIngresá una fila: "))
        columna = int(input("Ingresá una columna: "))

        if posicion_valida(fila, columna, filas, columnas):
            if tablero[fila][columna] == "":
                print("Ya has descubierto esta celda")
            elif tablero[fila][columna] == "💣":
                print("\nPerdiste. Encontraste una bomba.")
                mostrar_tablero(tablero)
                print(f"Tu Score fue: {score}")
                break
            else:
                print("\nSafate! sumaste un punto.")
                tablero[fila][columna] = "✅"
                score+=1
        else:
            print("\nPosición inválida.")


# Programa principal
jugar()