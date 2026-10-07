#Sistema de un banco
#Banco los manguitos

cola = [] #creamos una lista vacía para simular una cola

numero_turno = 1 #inicializamos el número de turno en 1 para contabilizar los clientes que llegan al banco

def Registrar_Clientes(nombre): #función para registrar clientes en la cola del banco
    global numero_turno #declaramos que vamos a usar la variable global numero_turno
     #generamos el codigo del turno
     # T = Letra que significa turno, seguido del numero de turno
     #:03d minimo de digitos para rellenar son 3, si el numero de turno es menor a 3 digitos se rellenara con ceros a la izquierda
     # Ejemplo: T001, T002, T003, T004, T005, T006, T007, T008, T009, T010
    codigo_turno = f"T{numero_turno:03d}" #generamos el codigo del turno con el formato T001, T002, T003, etc.
    cola.append((codigo_turno, nombre)) #agregamos el cliente a la cola
    numero_turno += 1 #incrementamos el número de turno en 1 para el siguiente cliente

    # Mostramos los datos del cliente registrado
    print("\nCliente registrado correctamente.")
    print("Turno asignado:", codigo_turno)
    print("Nombre del cliente:", nombre)


def ver_siguiente(): #muestra el primer cliente de la cola
    if cola: #verificamos si hay clientes esperando
        siguiente_cliente = cola[0] #tomamos el primer cliente de la cola
        print("\nSiguiente cliente en espera:")
        print("Turno:", siguiente_cliente[0])
        print("Nombre:", siguiente_cliente[1])
    else:
        print("\nNo hay clientes en espera.")

def atender_cliente(): #atender al primer cliente de la cola
    if cola: #verificamos si hay clientes esperando
        cliente_atendido = cola.pop(0) #eliminamos el primer cliente de la cola y lo guardamos en una variable
        print("\nCliente atendido:")
        print("Turno:", cliente_atendido[0])
        print("Nombre:", cliente_atendido[1])
    else:
        print("\nNo hay clientes en espera.")

def mostrar_cola():
    # Verificamos si hay clientes en espera
    if not cola:
        print("\nNo hay clientes en espera.")
    else:
        # Mostramos todos los clientes de la cola
        print("\nClientes en espera:")
        for cliente in cola:
            print(cliente[0], "-", cliente[1])

        # Mostramos la cantidad de clientes
        print("\nCantidad de clientes en espera:", len(cola))


def menu():
    while True:
        print("\nBanco los totopostillos")
        print("-- Menu de Turnos --")
        print("1. Registrar cliente")
        print("2. Ver el siguiente cliente")
        print("3. Atender cliente")
        print("4. Mostrar todos los clientes")
        print("5. Salir")

        # Quitamos espacios para aceptar entradas como " 1 "
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ").strip()
            if nombre:
                Registrar_Clientes(nombre)
            else:
                print("\nEl nombre no puede estar vacío.")
        elif opcion == "2":
            ver_siguiente()
        elif opcion == "3":
            atender_cliente()
        elif opcion == "4":
            mostrar_cola()
        elif opcion == "5":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    menu()








