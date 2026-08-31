modulos = ["Autenticación", "Usuarios", "Productos", "Reportes", "Notificaciones"]

print(modulos)  #  lista completa de modulos 

modulos.append("Pagos")
print(modulos)  #  agregado con append()

modulos.insert(2, "Dashboard")
print(modulos)  #  insertado en la posición 2

indice_productos = modulos.index("Productos") # obtenemos el índice de "Productos"
modulos[indice_productos] = "Inventario"
print(modulos)  # "Productos" modificado por índice

modulos.remove("Notificaciones")
print(modulos)  # eliminado con remove()

print(len(modulos))  # la cantidad actual de módulos

print(modulos)  #  lista final