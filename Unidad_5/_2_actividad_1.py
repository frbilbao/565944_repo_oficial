"""
CONSIGNA:
Se nos solicita crear un bloque de código que realice lo siguiente:

1. Imprimir un mensaje de bienvenida
2. Leer el nombre de un estudiante por consola
3. Verificar que sea un nombre válido
4. Si es válido guardarlo en la lista global
5. Si es inválido, mostrar un mensaje en la consola
6. A fin de poder repetir el flujo, incluir el código dentro de un bucle while
"""

estudiantes = []

def saludar():
    print("Bienvenido al sistema")

def leer_nombre():
    nombre = input("Ingrese un nombre (o 'salir' para terminar): ")
    return nombre

def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True

def agregar_estudiante(nombre):
    estudiantes.append(nombre)
    print(f"Estudiante '{nombre}' agregado a la lista.")

saludar()

while True:
    nuevo_nombre = leer_nombre()

    if nuevo_nombre.lower() == "salir":
        print("Saliendo del programa...")
        break

    if validar_nombre(nuevo_nombre):
        agregar_estudiante(nuevo_nombre)
    else:
        print("El nombre ingresado no es válido.")

print("Lista final de estudiantes:", estudiantes)
