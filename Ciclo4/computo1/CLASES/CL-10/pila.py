pila = []
pila.append("Iniciar Sesion") # append() para agregar elementos a la pila
pila.append("Consultar el perfil")
pila.append("Ver amigos en comun")
pila.append("Hola bebe que usted hace?")
print(pila)

#desapilar un elemento de la pila
accion = pila.pop() # pop() para eliminar el último elemento agregado a la pila
print("\n Accion a retirar:", accion)

accion = pila.pop() # pop() para eliminar el último elemento agregado a la pila
print("\n  Penultima Accion a retirar:", accion)
print(pila)

