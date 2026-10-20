"""
Parcial 2 - Manejo y Estructura de Datos (UNIVO, Ciclo IV 2026)
Distribuidora "Las naranjas": cola FIFO + pila LIFO + arbol binario de busqueda.

Integrantes: Oscar Fabricio Guevara Aguilar, Isvi Jose Castillo Cruz

Ejecutar:  python parcial_esd.py
"""
# Nombres de los estudiantes: son los clientes de las solicitudes iniciales P001, P002 y P003.
ESTUDIANTES = ["Oscar Aguilar", "Isvi Castillo", "Gerardo Gonzalez"]

# Codigos de producto de los despachos iniciales D001, D002 y D003.
# Tienen que existir en el arbol inicial (50, 30, 70, 20, 40, 60, 80).
PRODUCTOS_DESPACHOS_INICIALES = [50, 30, 70]

#
#
# COLA FIFO: solicitudes de clientes
# La lista es la cola: append() encola al final, pop(0) atiende al frente.
#
#

def encolar(cola, codigo, cliente):
    cola.append((codigo, cliente))


def atender_solicitud(cola):
    # Condicion obligatoria antes de retirar: que la cola no este vacia.
    if not cola:
        return None
    return cola.pop(0)  # sale el que llego primero

#
#
# PILA LIFO: despachos
# La lista es la pila: append() apila, pop() sin indice desapila el ultimo.
#
#
def apilar(pila, operacion, producto):
    pila.append((operacion, producto))


def desapilar(pila):
    # Se revisa antes de hacer pop() para no intentar retirar de una pila vacia.
    if not pila:
        return None
    return pila.pop()  # sale el ultimo que entro

#
#
# ARBOL BINARIO DE BUSQUEDA: codigos de producto
# Menores a la izquierda, mayores a la derecha, sin repetidos.
#
#

class Nodo:
    def __init__(self, codigo):
        self.codigo = codigo
        self.izquierda = None
        self.derecha = None


def insertar(raiz, codigo):
    if raiz is None:
        return Nodo(codigo)
    if codigo < raiz.codigo:
        raiz.izquierda = insertar(raiz.izquierda, codigo)
    elif codigo > raiz.codigo:
        raiz.derecha = insertar(raiz.derecha, codigo)
    # si es igual no hace nada: no se permiten codigos repetidos
    return raiz


def buscar(raiz, codigo):
    if raiz is None:
        return False
    if codigo == raiz.codigo:
        return True
    if codigo < raiz.codigo:
        return buscar(raiz.izquierda, codigo)
    return buscar(raiz.derecha, codigo)


def inorden(raiz, resultado=None):
    # izquierda -> raiz -> derecha: en un BST sale de menor a mayor
    if resultado is None:
        resultado = []
    if raiz is not None:
        inorden(raiz.izquierda, resultado)
        resultado.append(raiz.codigo)
        inorden(raiz.derecha, resultado)
    return resultado


def minimo(nodo):
    # El menor valor siempre queda al extremo izquierdo de este subarbol.
    while nodo.izquierda is not None:
        nodo = nodo.izquierda
    return nodo


def eliminar(raiz, codigo):
    if raiz is None:
        return None
    if codigo < raiz.codigo:
        raiz.izquierda = eliminar(raiz.izquierda, codigo)
    elif codigo > raiz.codigo:
        raiz.derecha = eliminar(raiz.derecha, codigo)
    else:
        # Caso 1: hoja
        if raiz.izquierda is None and raiz.derecha is None:
            return None
        # Caso 2: un solo hijo, ese hijo ocupa su lugar
        if raiz.izquierda is None:
            return raiz.derecha
        if raiz.derecha is None:
            return raiz.izquierda
        # Caso 3: dos hijos, lo reemplaza su sucesor inorden
        # (el menor del subarbol derecho) y luego se borra el sucesor
        # Asi el orden del arbol se conserva despues del reemplazo.
        sucesor = minimo(raiz.derecha)
        raiz.codigo = sucesor.codigo
        raiz.derecha = eliminar(raiz.derecha, sucesor.codigo)
    return raiz


def dibujar(raiz, nivel=0):
    # Arbol de lado: la raiz a la izquierda, mayores arriba y menores abajo.
    if raiz is None:
        return
    dibujar(raiz.derecha, nivel + 1)
    print("      " * nivel + str(raiz.codigo))
    dibujar(raiz.izquierda, nivel + 1)

#
#
# DATOS INICIALES
#
#

def crear_datos_iniciales():
    datos = {"cola": [], "pila": [], "raiz": None,
             "sig_solicitud": 1, "sig_despacho": 1}

    for estudiante in ESTUDIANTES[:3]:
        encolar(datos["cola"], f"P{datos['sig_solicitud']:03d}", estudiante)
        datos["sig_solicitud"] += 1

    for producto in PRODUCTOS_DESPACHOS_INICIALES:
        apilar(datos["pila"], f"D{datos['sig_despacho']:03d}", producto)
        datos["sig_despacho"] += 1

    for codigo in (50, 30, 70, 20, 40, 60, 80):
        datos["raiz"] = insertar(datos["raiz"], codigo)

    return datos

#
#
# ENTRADA DE DATOS CON VALIDACION
#
#

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  El dato no puede estar vacio.")


def pedir_codigo(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isdecimal() and int(valor) > 0:
            return int(valor)
        print("  Escribe un codigo numerico entero y positivo.")


def generar_codigo(datos, contador, prefijo, en_uso):
    # Siguiente codigo libre: P004, P005... o D004, D005...
    while True:
        codigo = f"{prefijo}{datos[contador]:03d}"
        datos[contador] += 1
        if codigo not in en_uso:
            return codigo


def pedir_codigo_operacion(mensaje, datos, contador, prefijo, en_uso):
    # El usuario escribe el codigo, o deja vacio (Enter) para que se genere solo.
    # Se rechazan los codigos que ya estan en uso.
    while True:
        valor = input(mensaje).strip().upper()
        if not valor:
            return generar_codigo(datos, contador, prefijo, en_uso)
        if valor in en_uso:
            print(f"  El codigo {valor} ya esta en uso. Escribe otro o Enter para uno automatico.")
            continue
        return valor

#
#
# ACCIONES DEL MENU
#
#

def accion_registrar_solicitud(datos):
    en_uso = [c for c, _ in datos["cola"]]
    codigo = pedir_codigo_operacion(
        "Codigo de la solicitud (Enter = automatico): ",
        datos, "sig_solicitud", "P", en_uso)
    cliente = pedir_texto("Nombre del cliente: ")
    encolar(datos["cola"], codigo, cliente)
    print(f"Solicitud {codigo} registrada para {cliente}.")


def accion_atender_solicitud(datos):
    # Sin solicitudes no hay ningun elemento valido para retirar de la cola.
    atendida = atender_solicitud(datos["cola"])
    if atendida is None:
        print("No hay solicitudes para atender.")
        return
    print(f"Solicitud atendida: {atendida[0]} - {atendida[1]}")


def accion_mostrar_solicitudes(datos):
    if not datos["cola"]:
        print("No hay solicitudes pendientes.")
        return
    print("Solicitudes pendientes (la primera es la siguiente en atenderse):")
    for posicion, (codigo, cliente) in enumerate(datos["cola"], start=1):
        print(f"  {posicion}. {codigo} - {cliente}")


def accion_registrar_despacho(datos):
    producto = pedir_codigo("Codigo del producto: ")
    if not buscar(datos["raiz"], producto):
        print(f"El producto {producto} no existe en el arbol. Despacho no registrado.")
        return
    en_uso = [o for o, _ in datos["pila"]]
    operacion = pedir_codigo_operacion(
        "Codigo de la operacion (Enter = automatico): ",
        datos, "sig_despacho", "D", en_uso)
    apilar(datos["pila"], operacion, producto)
    print(f"Despacho {operacion} registrado (producto {producto}).")


def accion_consultar_despachos(datos):
    if not datos["pila"]:
        print("No hay despachos registrados.")
        return
    print("Despachos registrados (el de arriba es el ultimo):")
    ultimo = len(datos["pila"]) - 1
    for posicion in range(ultimo, -1, -1):
        operacion, producto = datos["pila"][posicion]
        marca = "   <-- cima" if posicion == ultimo else ""
        print(f"  {operacion} - producto {producto}{marca}")


def accion_retirar_despacho(datos):
    # Se valida antes de retirar para no hacer pop() sobre una pila vacia.
    retirado = desapilar(datos["pila"])
    if retirado is None:
        print("No hay despachos para retirar.")
        return
    print(f"Despacho retirado del registro: {retirado[0]} (producto {retirado[1]}).")


def accion_insertar_codigo(datos):
    codigo = pedir_codigo("Codigo a insertar: ")
    if buscar(datos["raiz"], codigo):
        print(f"El codigo {codigo} ya existe. No se permiten repetidos.")
        return
    datos["raiz"] = insertar(datos["raiz"], codigo)
    print(f"Codigo {codigo} insertado.")


def accion_buscar_codigo(datos):
    if datos["raiz"] is None:
        print("El arbol esta vacio.")
        return
    codigo = pedir_codigo("Codigo a buscar: ")
    if buscar(datos["raiz"], codigo):
        print(f"El codigo {codigo} existe.")
    else:
        print(f"El codigo {codigo} no existe.")


def accion_mostrar_codigos(datos):
    if datos["raiz"] is None:
        print("El arbol esta vacio.")
        return
    print("Inorden:", inorden(datos["raiz"]))
    print("Forma del arbol (de lado, raiz a la izquierda):")
    dibujar(datos["raiz"])


def accion_eliminar_codigo(datos):
    if datos["raiz"] is None:
        print("El arbol esta vacio.")
        return
    codigo = pedir_codigo("Codigo a eliminar: ")
    if not buscar(datos["raiz"], codigo):
        print(f"El codigo {codigo} no existe, no se elimino nada.")
        return
    datos["raiz"] = eliminar(datos["raiz"], codigo)
    print(f"Codigo {codigo} eliminado.")


def accion_atender_y_despachar(datos):
    # Las tres estructuras trabajando juntas:
    #   arbol -> valida el producto, cola -> da la solicitud, pila -> guarda el despacho.
    if not datos["cola"]:
        print("No hay solicitudes para atender.")
        return
    cliente = datos["cola"][0][1]
    print(f"Siguiente solicitud: {datos['cola'][0][0]} - {cliente}")
    producto = pedir_codigo("Codigo del producto a despachar: ")
    # Se valida ANTES de sacar la solicitud, para no perderla si el producto no existe.
    if not buscar(datos["raiz"], producto):
        print(f"El producto {producto} no existe en el arbol. La solicitud sigue en cola.")
        return
    en_uso = [o for o, _ in datos["pila"]]
    operacion = pedir_codigo_operacion(
        "Codigo de la operacion (Enter = automatico): ",
        datos, "sig_despacho", "D", en_uso)
    codigo_solicitud, _ = atender_solicitud(datos["cola"])
    apilar(datos["pila"], operacion, producto)
    print(f"Solicitud {codigo_solicitud} atendida y despacho {operacion} registrado "
          f"(producto {producto}, cliente {cliente}).")

#
#
# PRUEBAS AUTOMATICAS (evidencia para el entregable)
# Cada prueba compara el resultado real con el esperado y al final muestra el total de aciertos.
# Asi se revisan por separado la cola, la pila, el arbol y su coordinacion.
#
#

def ejecutar_pruebas():
    resultados = []

    def verificar(descripcion, condicion):
        resultados.append(condicion)
        print(f"  [{'OK' if condicion else 'FALLO'}] {descripcion}")

    print("\n--- Cola FIFO ---")
    d = crear_datos_iniciales()
    verificar("Cola inicial en orden P001, P002, P003",
              [c for c, _ in d["cola"]] == ["P001", "P002", "P003"])
    verificar("Primero en atenderse: P001", atender_solicitud(d["cola"])[0] == "P001")
    verificar("Segundo en atenderse: P002", atender_solicitud(d["cola"])[0] == "P002")
    encolar(d["cola"], "P004", "Cliente nuevo")
    verificar("Una solicitud nueva se agrega al final",
              [c for c, _ in d["cola"]] == ["P003", "P004"])
    atender_solicitud(d["cola"])
    atender_solicitud(d["cola"])
    verificar("Cola vacia: atender devuelve None, sin error", atender_solicitud(d["cola"]) is None)

    print("\n--- Pila LIFO ---")
    d = crear_datos_iniciales()
    verificar("Pila inicial D001, D002, D003 (base a cima)",
              [o for o, _ in d["pila"]] == ["D001", "D002", "D003"])
    verificar("Primero en retirarse: D003 (el ultimo)", desapilar(d["pila"])[0] == "D003")
    verificar("Luego: D002", desapilar(d["pila"])[0] == "D002")
    apilar(d["pila"], "D004", 20)
    verificar("Un despacho nuevo queda en la cima", d["pila"][-1][0] == "D004")
    desapilar(d["pila"])
    desapilar(d["pila"])
    verificar("Pila vacia: desapilar devuelve None, sin error", desapilar(d["pila"]) is None)

    print("\n--- Arbol binario de busqueda ---")
    d = crear_datos_iniciales()
    raiz = d["raiz"]
    verificar("Inorden ordenado: 20 30 40 50 60 70 80",
              inorden(raiz) == [20, 30, 40, 50, 60, 70, 80])
    verificar("Raiz 50, hijos 30 y 70", (raiz.codigo, raiz.izquierda.codigo, raiz.derecha.codigo) == (50, 30, 70))
    verificar("Buscar 60: existe", buscar(raiz, 60))
    verificar("Buscar 99: no existe", not buscar(raiz, 99))
    raiz = insertar(raiz, 50)
    verificar("Insertar un duplicado (50) no cambia el arbol",
              inorden(raiz) == [20, 30, 40, 50, 60, 70, 80])
    raiz = eliminar(raiz, 20)
    verificar("Eliminar hoja (20)", inorden(raiz) == [30, 40, 50, 60, 70, 80])
    raiz = eliminar(raiz, 30)
    verificar("Eliminar nodo con un hijo (30): 40 sube", raiz.izquierda.codigo == 40)
    d = crear_datos_iniciales()
    raiz = eliminar(d["raiz"], 30)
    verificar("Eliminar nodo con dos hijos (30): lo reemplaza el sucesor 40",
              raiz.izquierda.codigo == 40 and raiz.izquierda.izquierda.codigo == 20
              and raiz.izquierda.derecha is None)
    verificar("Inorden sigue ordenado tras eliminar 30", inorden(raiz) == [20, 40, 50, 60, 70, 80])
    raiz = eliminar(raiz, 50)
    verificar("Eliminar la raiz (50): la reemplaza 60", raiz.codigo == 60)
    verificar("Eliminar un codigo inexistente no rompe nada",
              inorden(eliminar(raiz, 999)) == inorden(raiz))
    vacio = None
    verificar("Arbol vacio: buscar, inorden y eliminar no fallan",
              not buscar(vacio, 1) and inorden(vacio) == [] and eliminar(vacio, 1) is None)

    print("\n--- Independencia y coordinacion ---")
    d = crear_datos_iniciales()
    atender_solicitud(d["cola"])
    verificar("Atender una solicitud no toca la pila ni el arbol",
              len(d["pila"]) == 3 and inorden(d["raiz"]) == [20, 30, 40, 50, 60, 70, 80])
    desapilar(d["pila"])
    verificar("Retirar un despacho no toca la cola ni el arbol",
              len(d["cola"]) == 2 and inorden(d["raiz"]) == [20, 30, 40, 50, 60, 70, 80])
    d["raiz"] = eliminar(d["raiz"], 80)
    verificar("Eliminar un codigo no toca la cola ni la pila", len(d["cola"]) == 2 and len(d["pila"]) == 2)
    verificar("Coordinacion: producto 40 existe en el arbol, se puede despachar", buscar(d["raiz"], 40))
    verificar("Coordinacion: producto 80 ya no existe, no se puede despachar", not buscar(d["raiz"], 80))

    total, correctas = len(resultados), sum(resultados)
    print(f"\nResultado: {correctas}/{total} pruebas superadas.")
    return correctas == total

#
#
# MENU
#
#

def mostrar_menu():
    print("\n=== Distribuidora Las naranjas ===")
    print("-- Solicitudes (cola FIFO) --")
    print(" 1. Registrar solicitud")
    print(" 2. Atender siguiente solicitud")
    print(" 3. Mostrar solicitudes pendientes")
    print("-- Despachos (pila LIFO) --")
    print(" 4. Registrar despacho")
    print(" 5. Consultar despachos")
    print(" 6. Retirar ultimo despacho")
    print("-- Productos (arbol BST) --")
    print(" 7. Insertar codigo")
    print(" 8. Buscar codigo")
    print(" 9. Mostrar codigos (inorden)")
    print("10. Eliminar codigo")
    print("-- Integracion --")
    print("11. Atender solicitud y registrar su despacho")
    print("12. Ejecutar pruebas automaticas")
    print(" 0. Salir")


def menu():
    datos = crear_datos_iniciales()
    acciones = {
        "1": accion_registrar_solicitud,
        "2": accion_atender_solicitud,
        "3": accion_mostrar_solicitudes,
        "4": accion_registrar_despacho,
        "5": accion_consultar_despachos,
        "6": accion_retirar_despacho,
        "7": accion_insertar_codigo,
        "8": accion_buscar_codigo,
        "9": accion_mostrar_codigos,
        "10": accion_eliminar_codigo,
        "11": accion_atender_y_despachar,
    }
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (0-12): ").strip()
        if opcion == "0":
            print("Programa finalizado.")
            break
        elif opcion == "12":
            ejecutar_pruebas()
        elif opcion in acciones:
            print()
            acciones[opcion](datos)
        else:
            print("Opcion no valida. Escribe un numero del 0 al 12.")


if __name__ == "__main__":
    try:
        menu()
    except (EOFError, KeyboardInterrupt):
        print("\nPrograma finalizado.")
