"""
CONSIGNA:
Generar una función principal y luego subfunciones que sean invocadas desde la función principal,
de manera de mantener el mismo workflow de la actividad_1, pero aprovechando las ventajas
de trabajar módulos reutilixables.

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

def principal():
    saludar()
    while True:
        nombre = leer_nombre()
        if nombre.lower() == "salir":
            print("Saliendo del programa...")
            break
        if validar_nombre(nombre):
            agregar_estudiante(nombre)
        else:
            print("El nombre ingresado no es válido.")
    print("Lista final de estudiantes:", estudiantes)

principal()