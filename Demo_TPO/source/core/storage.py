import json
import os

# ── storage.py ────────────────────────────────────────────────────────────────

def read_data(ruta):
    """
    Lee un archivo JSON y retorna su contenido como lista de diccionarios.
    Si el archivo no existe, lo crea vacío y retorna [].

    Parámetros:
        ruta (str): ruta relativa al archivo JSON. Ej: 'data/productos.json'

    Retorna:
        list: lista de diccionarios con los registros.
    """
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    if not os.path.exists(ruta):
        # Comportamiento "CREATE TABLE IF NOT EXISTS":
        # si no existe el archivo, lo creamos vacío y retornamos []
        with open(ruta, "w", encoding="utf-8") as file:
            json.dump([], file)
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Error al leer {ruta}: {e}")
        return []


def write_data(ruta, datos):
    """
    Escribe una lista de diccionarios en un archivo JSON.
    Sobrescribe el contenido previo (reemplaza todo el archivo).

    Parámetros:
        ruta  (str):  ruta relativa al archivo JSON. Ej: 'data/productos.json'
        datos (list): lista de diccionarios a persistir.

    Retorna:
        bool: True si se guardó correctamente, False si hubo error.
    """
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    try:
        with open(ruta, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)
        return True
    except OSError as e:
        print(f"Error al escribir {ruta}: {e}")
        return False
