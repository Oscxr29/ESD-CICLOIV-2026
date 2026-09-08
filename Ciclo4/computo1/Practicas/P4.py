import collections

# fila real de un super: el que llega primero, paga primero.
# por eso deque en vez de una lista normal, popleft() en una lista
# normal es O(n) porque tiene que recorrer todo, en deque es O(1).


def cobrar_siguiente(fila):
    """Saca al primer cliente de la fila. Si no hay nadie, regresa None en vez de tronar."""
    try:
        return fila.popleft()
    except IndexError:
        return None


def atender_supermercado():
    fila_caja = collections.deque()
    membresias_vigentes = {"MEMB-001", "MEMB-002", "MEMB-003"}
    cupones_usados = set()  # sets porque solo me importa si ya existe o no, no el orden

    cliente_1 = {"nombre": "Gabo", "membresia": "MEMB-001", "cupon": "DESC-50",
                 "bolsa": ["Leche", "Huevos", "Pan de caja"]}
    cliente_2 = {"nombre": "Isvi", "membresia": "MEMB-999", "cupon": "DESC-50",
                 "bolsa": ["Manzanas", "Cereal"]}
    cliente_3 = {"nombre": "Henry", "membresia": "MEMB-002", "cupon": "DESC-20",
                 "bolsa": ["Jugo de naranja"]}

    for c in (cliente_1, cliente_2, cliente_3):
        fila_caja.append(c)

    print(f"Clientes en fila: {len(fila_caja)}\n")

    while True:
        cliente = cobrar_siguiente(fila_caja)
        if cliente is None:
            print("No hay nadie en la fila para cobrar.")
            break

        print(f"Atendiendo a {cliente['nombre']}")

        if cliente["membresia"] in membresias_vigentes:
            print(f"  Membresia {cliente['membresia']} valida")
        else:
            print(f"  Membresia {cliente['membresia']} no esta registrada")

        cupon = cliente["cupon"]
        if cupon in cupones_usados:
            # Kenneth cae aca, quiso usar el mismo cupon que ya uso Alex
            print(f"  El cupon {cupon} ya se uso antes en esta sesion, no se vuelve a aplicar")
        else:
            cupones_usados.add(cupon)
            print(f"  Cupon {cupon} aplicado")

        # la bolsa se comporta como pila: lo ultimo que el cliente metio
        # es lo primero que el cajero saca a escanear
        bolsa = cliente["bolsa"]
        if not bolsa:
            print("  Bolsa vacia")
        while bolsa:
            print(f"  Registrando: {bolsa.pop()}")

        print()


if __name__ == "__main__": # esto es para que si alguien importa este modulo, no se ejecute la funcion main
    atender_supermercado() # la funcion main de este modulo es atender_supermercado