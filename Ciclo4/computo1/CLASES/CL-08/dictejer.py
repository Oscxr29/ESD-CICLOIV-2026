#ejemplo practico 

producto = {
    "codigo": "P001",
    "nombre": "teclado mecanico",
    "precio": 45.95,
    "stock": 100,
    "disponible": True,
}

print(producto)
print(producto["nombre"]) #imprimimos el nombre del producto

#cambiar la disponibilidad del proudcto y el stock a 0 
print("Disponibilidad antes de la venta:", producto["disponible"])
producto["disponible"] = False
print("Disponibilidad después de la venta:", producto["disponible"])