
"""
Try-except articles
https://medium.com/p/97d12aac91b6
https://medium.com/@syaokifaradisa09/python-exception-handling-making-your-code-bulletproof-a347f306b03a
https://medium.com/@vivekmcm1/python-exception-handling-explained-with-real-world-examples-15807183af6e
https://medium.com/stackademic/junior-devs-use-try-catch-everywhere-senior-devs-use-these-4-exception-handling-patterns-dcd869ed6551
https://medium.com/@chandantechie/top-10-ways-to-handle-exception-in-python-with-coding-examples-6de53cae5338
"""

# Primer caso de exceptions generales

# Declarar una exception customizada
class ValorNegativoError(Exception):
    pass

# Bucle para iterar:
while True:
    try:
        numero = float(input("Ingresa tu numero: "))
        # Evalue regla del negocio
        if numero <0:
            raise ValorNegativoError("No se puede ingresar numeros negativos")
        # Realizo la operación principal
        result = 10 / numero
    except ZeroDivisionError: # Check de Exception 1
        print("No se puede dividir por 0")
    except TypeError: # Check de Exception 2
        print("Error en el tipo de dato de numero")
    except ValueError: # Check de Exception 3
        print("ERROR: Ingrese un número válido")
    except Exception as e: # Check de Exception Genérica
        print(f"ERROR: {e}")
    else:
        print(f"El resultado de la division por {numero} es: {result}")

    # Evalúo condición de corte del While
    opcion = input("Sigue? s/n")
    if opcion.strip().lower()=="s":
        break


# Manejo de exceptions con apertura de archivos
try:
    f = open("calificaciones.csv", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
finally:
    if 'f' in locals() and not f.closed: #check if the file is opened.
      f.close()
      print("File closed.")

# Manejo de Exceptions con listas
numbers = [10, 20, 30, 40]

def printNumero(lista, indice):
    print(f"indice {indice} - valor {lista[indice]}")

try:
    printNumero(numbers, 4)
except IndexError: 
    print("Indice fuera de rango")