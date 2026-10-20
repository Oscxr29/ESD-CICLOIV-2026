# Aquí tienes el texto extraído de la imagen:

# Caso Práctico: Reestructuración del Catálogo de E-commerce para "NovaMart"
# Contexto del Proyecto:
# La empresa de retail "NovaMart" está migrando su tienda en línea hacia una nueva arquitectura de microservicios.
#  Uno de los mayores cuellos de botella actuales es el menú de navegación: la base de datos relacional tarda demasiado
# en devolver las categorías anidadas, causando una mala experiencia de usuario.

# El equipo de Arquitectura de Software ha determinado que la jerarquía de categorías debe cargarse en la memoria caché del
# servidor web al iniciar el sistema. Para lograr búsquedas y recorridos ultrarrápidos, se requiere modelar este catálogo utilizando
# una estructura de datos jerárquica: un Árbol Binario.

# LAPTOPS y CELULARES.
# COCINA y MUEBLES.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

raiz = Nodo("Producto")

raiz.izquierda = Nodo("Tecnología")
raiz.derecha = Nodo("Hogar")

#Creamos hijos
#subcategorias de tecnologia
raiz.izquierda.izquierda = Nodo("Laptops")
raiz.izquierda.derecha = Nodo("Celulares")

#Creamos hijos
#subcategorias de hogar
raiz.izquierda.izquierda = Nodo("Cocina")
raiz.izquierda.derecha = Nodo("Muebles")

#mostrar la informacion
print("Raiz del arbol:")
print("Valor:", raiz.valor)

print("Mostrar hijos:")
print("Izquierdo:", raiz.izquierda.valor)
print("Derecho:", raiz.derecha.valor)

def es_hoja(nodo):
    return nodo.izquierda is None and nodo.derecha is None
print("Laptops es hoja:", es_hoja(raiz.izquierda.izquierda))
print("Tecnología es hoja:", es_hoja(raiz.izquierda))