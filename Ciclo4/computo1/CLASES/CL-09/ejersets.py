# # Intento de eliminación sin excepción
# set4 = set([1, 2])
# set4.discard(3)
# print(set4) # Salida: {1, 2}

set4 = set([1, 2])
set4.discard(3)
print(set4) # Salida: {1, 2}

# 4. Extracción aleatoria: s.pop()
# Extracción
# El método pop() elimina y retorna un elemento aleatorio del conjunto (dado que los sets no son ordenados).

# # Extracción de elemento no determinado
# set5 = set([1, 2])
# set5.pop()
# print(set5) # Salida: {2} (o {1})

set5 = set([1, 2])
set5.pop()
print(set5) # Salida: {2} (o {1})

# 5. Vaciar el conjunto: s.clear()
# Limpieza
# El método clear() remueve la totalidad de los elementos, dejando el conjunto vacío (representado como set()).

# # Limpieza total del set
# set6 = set([1, 2])
# set6.clear()
# print(set6) # Salida: set()

set6 = set([1, 2])
set6.clear()
print(set6) # Salida: set()

#ejercicio de estudiante

# Instrucciones: Modifica el programa para administrar los empleados de dos departamentos utilizando los métodos de conjuntos (Sets).
# Sigue los pasos descritos para cada departamento.

ventas = {"Ana", "Carlos", "Maria"}
soporte = {"Jose", "Luis", "Maria"}

# Parte A — Departamento de Ventas
print("Empleados en ventas:", ventas)

ventas.add("Pedro")
ventas.add("Pedro")  # Intento de agregar nuevamente a "Pedro"
ventas.remove("Carlos")
ventas.discard("Roberto")  # Intento de eliminar a "Roberto"
empleado_retirado = ventas.pop()
print("Empleado retirado:", empleado_retirado)
ventas.clear()
print("Conjunto de ventas vacío:", ventas)


# Parte B — Departamento de Soporte
print("\nEmpleados en soporte:", soporte)

# Realiza nuevamente las operaciones anteriores, pero utilizando el conjunto soporte.
soporte.add("Pedro")
soporte.add("Pedro")  # Intento de agregar nuevamente a "Pedro"
soporte.remove("Luis")
soporte.discard("Roberto")  # Intento de eliminar a "Roberto"
empleado_retirado = soporte.pop()
print("Empleado retirado:", empleado_retirado)
soporte.clear()
print("Conjunto de soporte vacío:", soporte)
