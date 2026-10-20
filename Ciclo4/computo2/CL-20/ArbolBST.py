"""SISTEMA DE INVENTARIO CON ÁRBOL BINARIO DE BÚSQUEDA (BST)
Caso empresarial: administrar productos de una empresa.

Cada producto tiene:
- Código: identifica al producto y determina su posición.
- Nombre: describe el producto.
- Cantidad: unidades disponibles en inventario.

Regla del BST:
- Códigos menores: subárbol izquierdo.
- Códigos mayores: subárbol derecho.
- No se permiten códigos duplicados.
"""
class Nodo:
    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.izquierda = None
        self.derecha = None

def agregar(raiz, codigo, nombre, cantidad):
    if raiz is None:
        return Nodo(codigo, nombre, cantidad)
    if codigo < raiz.codigo:
        raiz.izquierda = agregar(
            raiz.izquierda, codigo, nombre, cantidad
        )
    elif codigo > raiz.codigo:
        raiz.derecha = agregar(
            raiz.derecha, codigo, nombre, cantidad
        )
    else:
        print("El codigo ya existe:", codigo)
    return raiz

def buscar(raiz, codigo):
    if raiz is None:
        return None
    if codigo == raiz.codigo:
        return raiz
    if codigo < raiz.codigo:
        return buscar(raiz.izquierda, codigo)
    return buscar(raiz.derecha, codigo)

def actualizar(raiz, codigo, nuevo_nombre, nueva_cantidad):
    producto = buscar(raiz, codigo)
    if producto is None:
          print("Producto no encontrado")
          return
    producto.nombre = nuevo_nombre
    producto.cantidad = nueva_cantidad
    print("Producto actualizado correctamente.")

def  minimo (nodo):
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
        # Caso 1: Nodo sin hijos
        if raiz.izquierda is None and raiz.derecha is None:
            return None
        # Caso 2: Nodo con un hijo
        if raiz.izquierda is None:
            return raiz.derecha
        if raiz.derecha is None:
            return raiz.izquierda
        # Caso 3: Nodo con dos hijos
        sucesor = minimo(raiz.derecha)
        raiz.codigo = sucesor.codigo
        raiz.nombre = sucesor.nombre
        raiz.cantidad = sucesor.cantidad
        raiz.derecha = eliminar(raiz.derecha, sucesor.codigo)
     return raiz

def inorder(raiz):
     if raiz is None:
          return
     inorder(raiz.izquierda)
     print(
          raiz.codigo, " - ", raiz.nombre, " - Stock: ", raiz.cantidad
     )
     inorder(raiz.derecha)

"""
Codigo    Nombre          Cantidad
50,       "Laptop",         12
30,       "Teclado",        25
70,       "Monitor",         8
20,       "Mouse",          40
40,       "Audífonos",      18
60,       "Impresora",       5
80,       "Webcam",         10
"""
raiz = None
raiz = agregar(raiz, 50, "Laptop", 12)
raiz = agregar(raiz, 30, "Teclado", 25)
raiz = agregar(raiz, 70, "Monitor", 8)
raiz = agregar(raiz, 20, "Mouse", 40)
raiz = agregar(raiz, 40, "Audífonos", 18)
raiz = agregar(raiz, 60, "Impresora", 5)
raiz = agregar(raiz, 80, "Webcam", 10)

print("\n Inventario Inicial:")
inorder(raiz)

print("\n Busqueda:")
producto = buscar(raiz, 40)
if producto is not None:
     print("Encontrado:",producto.nombre)
else:
     print("Producto no encontrado.")

print("\n Actualizar producto:")
actualizar(raiz, 40, "Audífonos inalámbricos", 22)


print("\n Eliminar producto:")
raiz = eliminar(raiz, 30)
print("Se realizo la eliminacion del producto con codigo 30.")

print("\n Inventario Final:")
inorder(raiz)