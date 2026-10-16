# Laboratorio práctico 2: Terminal de buses
# Aquí juntamos las tres estructuras del curso en un solo programa:
#   - Cola (FIFO): los pasajeros que esperan, el primero que llega es el primero que se atiende
#   - Pila (LIFO): las salidas de buses, lo último que se registró es lo primero que se puede deshacer
#   - Árbol: los destinos ordenados como Terminal Central > Región > Destino

import unicodedata  # para comparar textos sin importar tildes (ver la función normalizar)


# FUNCIÓN DE APOYO


def normalizar(texto):
    # Le quita las tildes y lo pasa a minúsculas.
    # Así "la union", "La Unión" y "LA UNIÓN" cuentan como lo mismo
    # y el usuario no se pelea con el teclado.
    sin_tildes = unicodedata.normalize("NFD", texto)
    return "".join(c for c in sin_tildes if unicodedata.category(c) != "Mn").lower()
# NFD descompone los caracteres acentuados en dos partes: la letra base y el acento. Luego, la comprensión de lista filtra los caracteres
#  cuya categoría Unicode es "Mn" (Mark, Nonspacing), que son los acentos. Finalmente, se unen los caracteres restantes y se convierten a minúsculas.

# ÁRBOL DE DESTINOS

class NodoDestino:
    def __init__(self, nombre):
        self.nombre = nombre  # el nombre del destino, región o terminal
        self.hijos = []       # lista con los nodos que cuelgan de este (vacía si es un destino final)

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def construir_arbol():
    # La raíz es la Terminal Central y de ahí salen las tres zonas.
    raiz = NodoDestino("Terminal Central")

    # Se uso un diccionario para no repetir tres veces el mismo código:
    # cada región con la lista de sus destinos.
    regiones = {
        "Zona Oriental": ["San Miguel", "La Unión", "Usulután"],
        "Zona Central": ["San Salvador", "La Libertad", "Cuscatlán"],
        "Zona Occidental": ["Santa Ana", "Ahuachapán", "Sonsonate"],
    }

    for nombre_region, destinos in regiones.items():
        nodo_region = NodoDestino(nombre_region)
        for destino in destinos:
            nodo_region.agregar_hijo(NodoDestino(destino))
        raiz.agregar_hijo(nodo_region)

    return raiz

def mostrar_jerarquia(nodo, nivel=0):
    # Función recursiva: imprime el nodo y luego se llama a sí misma por cada hijo.
    # "nivel" sube de 1 en 1 y sirve para dar la sangría (2 espacios por nivel).
    print("  " * nivel + "- " + nodo.nombre)
    for hijo in nodo.hijos:
        mostrar_jerarquia(hijo, nivel + 1)

def buscar_destino(nodo, nombre):
    # Búsqueda recursiva. Caso base 1: este nodo es el que buscamos, lo devolvemos.
    if normalizar(nodo.nombre) == normalizar(nombre):
        return nodo

    # Si no es este, preguntamos en cada rama hacia abajo.
    for hijo in nodo.hijos:
        encontrado = buscar_destino(hijo, nombre)
        if encontrado is not None:  # alguna rama lo encontró, lo subimos
            return encontrado

    # Caso base 2: ya recorrimos todo y no apareció, devolvemos None.
    return None

# DATOS DEL PROGRAMA (globales, porque se van a modificar desde varias funciones)

arbol_destinos = construir_arbol()

cola_pasajeros = []   # COLA: se agrega al final con append() y se atiende por el frente con pop(0)
pila_salidas = []     # PILA: se agrega al final con append() y se deshace por el final con pop()

numero_turno = 1      # contador para los turnos P001, P002, ...
numero_salida = 1     # contador para las salidas S001, S002, ...

# COLA (FIFO): PASAJEROS EN ESPERA

def registrar_pasajero():
    global numero_turno  # lo vamos a modificar, por eso va como global

    nombre = input("Nombre del pasajero: ").strip()
    if not nombre:  # validación: no aceptamos nombres vacíos
        print("\nEl nombre no puede estar vacío.")
        return

    destino_escrito = input("Destino: ").strip()
    if not destino_escrito:
        print("\nEl destino no puede estar vacío.")
        return

    # Buscamos el destino en el árbol. Si devuelve None, no existe y no registramos nada.
    nodo = buscar_destino(arbol_destinos, destino_escrito)
    if nodo is None:
        print(f"\nEl destino '{destino_escrito}' no existe en el árbol de destinos.")
        return

    # P + número con 3 dígitos: P001, P002, P003...
    turno = f"P{numero_turno:03d}"

    # Se guarda el nombre oficial del destino (nodo.nombre) y no lo que escribió el usuario,
    # así queda siempre con la misma ortografía.
    cola_pasajeros.append((turno, nombre, nodo.nombre))
    numero_turno += 1

    print("\nPasajero registrado correctamente.")
    print("Turno asignado:", turno)

def atender_pasajero():
    # Validamos que la cola no esté vacía antes de sacar a alguien
    if not cola_pasajeros:
        print("\nNo hay pasajeros en espera.")
        return

    # pop(0) saca el elemento de la posición 0, o sea el que llegó primero (FIFO)
    turno, nombre, destino = cola_pasajeros.pop(0)

    print("\nPASAJERO ATENDIDO")
    print("Turno:", turno)
    print("Nombre:", nombre)
    print("Destino:", destino)

def mostrar_cola():
    if not cola_pasajeros:
        print("\nNo hay pasajeros en espera.")
        return

    # Se muestran en orden de llegada, tal cual están guardados en la lista
    print("\nPASAJEROS EN ESPERA")
    for turno, nombre, destino in cola_pasajeros:
        print(f"{turno} - {nombre} - {destino}")
    print("Total en espera:", len(cola_pasajeros))

# PILA (LIFO): SALIDAS DE BUSES

def bus_ya_registrado(codigo_bus):
    # MEJORA 2: revisa si ese código de bus ya está en la pila.
    # Si alguien deshace la salida, el bus sale de la pila y el código queda libre otra vez.
    for _, codigo, _ in pila_salidas:
        if normalizar(codigo) == normalizar(codigo_bus):
            return True
    return False

def registrar_salida():
    global numero_salida

    codigo_bus = input("Código del bus (ej. Bus-31): ").strip()
    if not codigo_bus:
        print("\nEl código del bus no puede estar vacío.")
        return

    # MEJORA 2: evitar códigos de bus duplicados
    if bus_ya_registrado(codigo_bus):
        print(f"\nEl bus '{codigo_bus}' ya tiene una salida registrada. No se permiten códigos repetidos.")
        return

    destino_escrito = input("Destino del bus: ").strip()
    if not destino_escrito:
        print("\nEl destino no puede estar vacío.")
        return

    nodo = buscar_destino(arbol_destinos, destino_escrito)
    if nodo is None:
        print(f"\nEl destino '{destino_escrito}' no existe en el árbol de destinos.")
        return

    codigo_salida = f"S{numero_salida:03d}"

    # append() mete la salida al final de la lista, que es el tope de la pila
    pila_salidas.append((codigo_salida, codigo_bus, nodo.nombre))
    numero_salida += 1

    print("\nCódigo del bus:", codigo_bus)
    print("Destino del bus:", nodo.nombre)
    print("Salida registrada:", codigo_salida)

def deshacer_salida():
    # Primero comprobamos que la pila tenga algo, si no pop() truena con un error
    if not pila_salidas:
        print("\nNo hay salidas registradas para deshacer.")
        return

    # pop() sin número saca el último elemento, o sea la salida más reciente (LIFO)
    codigo_salida, codigo_bus, destino = pila_salidas.pop()

    print("\nSALIDA DESHECHA")
    print("Salida:", codigo_salida)
    print("Código del bus:", codigo_bus)
    print("Destino del bus:", destino)

def mostrar_salidas():
    if not pila_salidas:
        print("\nNo hay salidas registradas.")
        return

    print("\nSALIDAS REGISTRADAS")
    ultima = len(pila_salidas) - 1  # posición del tope de la pila
    for posicion, (codigo_salida, codigo_bus, destino) in enumerate(pila_salidas):
        marca = "  <-- ÚLTIMA" if posicion == ultima else ""
        print(f"{codigo_salida} - {codigo_bus} - {destino}{marca}")
    print("Total de salidas:", len(pila_salidas))

# ÁRBOL: CONSULTAS Y MEJORA 1 que consiste en agregar destinos desde el menú

def ver_arbol():
    print("\nÁRBOL DE DESTINOS")
    mostrar_jerarquia(arbol_destinos)

def buscar_destino_menu():
    nombre = input("Destino a buscar: ").strip()
    if not nombre:
        print("\nEl nombre del destino no puede estar vacío.")
        return

    nodo = buscar_destino(arbol_destinos, nombre)
    if nodo is None:
        print(f"\nEl destino '{nombre}' no existe.")
    else:
        print("\nDestino encontrado:", nodo.nombre)

def agregar_destino():
    # MEJORA 1: agregar destinos desde el menú indicando la región padre

    nuevo = input("Nombre del nuevo destino: ").strip().title()  # title() para que quede con mayúsculas como los demás
    if not nuevo:
        print("\nEl nombre del destino no puede estar vacío.")
        return

    # No dejamos duplicados, así la búsqueda siempre devuelve un solo nodo
    if buscar_destino(arbol_destinos, nuevo) is not None:
        print(f"\nEl destino '{nuevo}' ya existe.")
        return

    padre_escrito = input("Región padre (ej. Zona Oriental): ").strip()
    if not padre_escrito:
        print("\nLa región padre no puede estar vacía.")
        return

    # Reutilizamos la misma búsqueda recursiva para encontrar al padre
    padre = buscar_destino(arbol_destinos, padre_escrito)
    if padre is None:
        print(f"\nLa región '{padre_escrito}' no existe. El destino no se agregó.")
        return

    padre.agregar_hijo(NodoDestino(nuevo))
    print(f"\nDestino '{nuevo}' agregado dentro de '{padre.nombre}'.")

# MENÚ PRINCIPAL

def menu():
    while True:
        print("\n=== Terminal de Buses ===")
        print("-- Pasajeros (cola) --")
        print("1. Registrar pasajero")
        print("2. Atender pasajero")
        print("3. Ver pasajeros en espera")
        print("-- Salidas (pila) --")
        print("4. Registrar salida de bus")
        print("5. Deshacer última salida")
        print("6. Ver salidas registradas")
        print("-- Destinos (árbol) --")
        print("7. Ver árbol de destinos")
        print("8. Buscar destino")
        print("9. Agregar destino nuevo")
        print("0. Salir")

        # strip() quita espacios, así " 1 " también funciona
        opcion = input("Seleccione una opción (0-9): ").strip() #strip funciona para quitar espacios en blanco al inicio y al final de la cadena de texto

        if opcion == "1":
            registrar_pasajero()
        elif opcion == "2":
            atender_pasajero()
        elif opcion == "3":
            mostrar_cola()
        elif opcion == "4":
            registrar_salida()
        elif opcion == "5":
            deshacer_salida()
        elif opcion == "6":
            mostrar_salidas()
        elif opcion == "7":
            ver_arbol()
        elif opcion == "8":
            buscar_destino_menu()
        elif opcion == "9":
            agregar_destino()
        elif opcion == "0":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción no válida.")

if __name__ == "__main__":  # así el menú solo arranca si se ejecuta este archivo directamente
    menu()
