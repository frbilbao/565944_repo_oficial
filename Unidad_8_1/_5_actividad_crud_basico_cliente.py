# ============================================================
# OPERACIONES CRUD BÁSICAS (con diccionarios)
# ============================================================

# CRUD = Create, Read, Update, Delete
# Son las 4 operaciones fundamentales sobre cualquier conjunto de datos.

# Declaramos e incializamos una lista global clientes
# Donde cadad cliente posee la siguiente estructura:
# Atributos: id_cliente | razon_social | email | cell

clientes = [
    {
        "id_cliente": 1,
        "razon_social": "YPF",
        "email": "compras@ypf.com",
        "cell": "+5491134567890",
    },
    {
        "id_cliente": 2,
        "razon_social": "Arcor",
        "email": "compras@arcor.com",
        "cell": "'+5491145671234",
    },
]

# Visualizamos la lista global clientes inicializada 
# print(clientes)


# CREATE (Alta de clientes)
"""
1. Crear un nuevo cliente (cliente_3).
2. Agregarlo a la lista clientes utilizando el método append().
3. Mostrar un mensaje confirmando la operación.
"""
cliente_3 = {
    "id_cliente": 3,
    "razon_social": "Coca-Cola",
    "email": "compras@cocacola.com",
    "cell": "+5491156789012",
}
clientes.append(cliente_3)
print("Cliente agregado correctamente.")
print(clientes)


# READ (Búsqueda de cliente por id)
"""
1. Buscar un cliente a partir de su id_cliente.
2. Utilizar un for para recorrer la lista.
3. Guardar el resultado en una variable.
4. Mostrar el cliente encontrado.
"""
id_buscar = 2
cliente_encontrado = None
for c in clientes:
    if c["id_cliente"] == id_buscar:
        cliente_encontrado = c
        break

if cliente_encontrado:
    print(f"Cliente encontrado: {cliente_encontrado}")
else:
    print("No se encontró el cliente.")


# READ (Búsqueda de cliente por campo indicado clave:valor)
"""
1. Buscar un cliente a partir de su id_cliente.
2. Utilizar un for para recorrer la lista.
3. Guardar el resultado en una variable.
4. Mostrar el cliente encontrado.
"""
clave_buscar = "razon_social"
valor_buscar = "Arcor"
clientes_encontrados = []

for c in clientes:
    if c[clave_buscar] == valor_buscar:
        clientes_encontrados.append(c)

if clientes_encontrados:
    print(f"Clientes encontrados: {clientes_encontrados}")
else:
    print("No se encontraron clientes.")


# UPDATE (Modificación de un cliente según su id)
"""
1. Recorrer la lista de clientes.
2. Identificar un cliente por su id.
3. Modificar su email.
4. Mostrar el cliente actualizado.
"""
id_actualizar = 1
nuevo_email = "nuevoemail@ypf.com"
cliente_actualizado = None

for c in clientes:
    if c["id_cliente"] == id_actualizar:
        c["email"] = nuevo_email
        cliente_actualizado = c

if cliente_actualizado:
    print(f"Cliente actualizado: {cliente_actualizado}")
else:
    print("No se encontró el cliente a actualizar.")


# DELETE (Eliminación de un cliente según su id)
"""
1. Buscar un cliente por su id_cliente.
2. Eliminarlo de la lista utilizando remove().
3. Mostrar la lista final de productos.
"""
id_eliminar = 3
cliente_a_eliminar = None

for c in clientes:
    if c["id_cliente"] == id_eliminar:
        cliente_a_eliminar = c

if cliente_a_eliminar:
    clientes.remove(cliente_a_eliminar)
    print(f"Cliente eliminado: {cliente_a_eliminar}")
    print("Lista final de clientes:")
    print(clientes)
else:
    print("No se encontró el cliente a eliminar.")

