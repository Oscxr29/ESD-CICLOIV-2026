cola = [] #creamos una lista vacía para simular una cola

# Agregamos elementos a la cola
cola.append("Ana")
cola.append("Juan")
cola.append("Luis")
print(cola) #imprimimos la cola después de agregar elementos

#ejemplo de los ejercicios con distintas operaciones

colaTienda = [] # creamos una lista vacía para simular una cola en una tienda Rosita

#Operacion ENQUEUE: Agregamos clientes a la cola de la tienda Rosita
colaTienda.append("Ana")
colaTienda.append("Carlos")
colaTienda.append("Luis")

print("Cola de clientes en la tienda Rosita:", colaTienda) #imprimimos la cola después de agregar clientes


#Operacion Peek: Mostramos el primer cliente en la cola sin eliminarlo
primer_cliente = colaTienda[0] # obtenemos el primer cliente de la cola
print("Primer cliente en la cola:", primer_cliente) #imprimimos el primer cliente en la cola

#Operacion SIZE: Mostramos el tamaño de la cola
tamaño_cola = len(colaTienda) # obtenemos el tamaño de la cola
print("Tamaño de la cola:", tamaño_cola) #imprimimos el tamaño de la cola

#Operacion DEQUEUE: Eliminamos el primer cliente de la cola
primer_cliente_eliminado = colaTienda.pop(0) # eliminamos el primer cliente de la cola y lo guardamos en una variable
print("Cliente eliminado de la cola:", primer_cliente_eliminado) #imprimimos el cliente eliminado de la cola

#mostramos la cola después de eliminar un cliente
print("Cola de clientes en la tienda Rosita después de eliminar un cliente:", colaTienda) #imprimimos la cola después de eliminar un cliente

#Operacion Rear Consultamos quienes estan al final de la cola
ultimo_cliente = colaTienda[-1] # obtenemos el último cliente de la cola
print("Último cliente en la cola:", ultimo_cliente) #imprimimos el último cliente en la cola


#eliminamos a otro cliente de la cola para mostrar que la cola no está vacía
colaTienda.pop(0) # eliminamos el primer cliente de la cola
print("Cola de clientes en la tienda Rosita después de eliminar otro cliente:", colaTienda) #imprimimos la cola después de eliminar otro cliente


#eliminamos a otro cliente de la cola para mostrar que la cola está vacía
colaTienda.pop(0) # eliminamos el primer cliente de la cola
print("Cola de clientes en la tienda Rosita después de eliminar otro cliente:", colaTienda) #imprimimos la cola después de eliminar otro cliente

#Operacion isEmpty: Verificamos si la cola está vacía

if not colaTienda: # verificamos si la cola está vacía
    print("La cola está vacía, no hay clientes esperando") #imprimimos que la cola está vacía
else:
    print("La cola no está vacía, hay clientes esperando") #imprimimos que la cola no está vacía

