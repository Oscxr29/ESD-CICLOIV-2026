# x = 10
# print(x, id(x))      
# x = x + 1
# print(x, id(x))     #

# texto = "hola"
# print(texto, id(texto))          
# texto = texto + " mundo"
# print(texto, id(texto))         

#listas 

# lista = [1, 2, 3]
# print(lista, id(lista))   
# lista.append(4)
# print(lista, id(lista))   


# def modificar_numero(num):
#     num += 10
#     print("Dentro de función:", num)   # 15

# val = 5
# modificar_numero(val)
# print("Fuera de función:", val)   # sigue siendo 5


# Actividad: Tipos de datos con reglas propias
# Idea central: estos "tipos" no dejan que un valor exista si no cumple
# su regla. No es solo guardar un dato, es cuidar que tenga sentido.


class Email:
    def __init__(self, direccion):
        # Un correo real siempre tiene un "@" y un "." (dominio).
        # Si falta alguno, ni se molesta en guardarlo.
        if "@" not in direccion or "." not in direccion:
            raise ValueError("Esa dirección no parece un correo válido")
        self.direccion = direccion

class Edad:
    def __init__(self, valor):
        # Nadie tiene edad negativa ni 300 años, así que se pone límites
        # razonables (0 a 100) y exigimos que sea un número entero.
        if not isinstance(valor, int) or valor < 0 or valor > 100:
            raise ValueError("Esa edad no es realista (debe ser 0-120)")
        self.valor = valor


class Nota:
    def __init__(self, calificacion):
        # En la escala de 0.0 a 10.0, no existen notas de 15 o -3.
        if not (0.0 <= calificacion <= 10.0):
            raise ValueError("La nota debe estar entre 0.0 y 10.0")
        self.calificacion = calificacion


class Contrasena:
    def __init__(self, valor):
        # Una contraseña segura necesita largo, una mayúscula y un número.
        # Si le falta algo, se rechaza antes de que cause problemas.
        if len(valor) < 8:
            raise ValueError("La contraseña necesita al menos 8 caracteres")
        if not any(c.isupper() for c in valor):
            raise ValueError("Falta al menos una letra mayúscula")
        if not any(c.isdigit() for c in valor):
            raise ValueError("Falta al menos un número")
        self.valor = valor


class Telefono:
    def __init__(self, numero):
        # Formato de El Salvador: 8 dígitos, nada de letras ni guiones.
        if not numero.isdigit() or len(numero) != 8:
            raise ValueError("El teléfono debe tener 8 dígitos numéricos")
        self.numero = numero


# Casos de uso: un ejemplo válido y uno inválido por cada clase


print("--- Email ---")
try:
    e = Email("usuario@dominio.com")
    print("Válido:", e.direccion)
except ValueError as err:
    print("Error:", err)

try:
    Email("correo_sin_arroba.com")
except ValueError as err:
    print("Rechazado:", err)

print("\n--- Edad ---")
try:
    ed = Edad(20)
    print("Válido:", ed.valor)
except ValueError as err:
    print("Error:", err)

try:
    Edad(-5)
except ValueError as err:
    print("Rechazado:", err)

print("\n--- Nota ---")
try:
    n = Nota(8.5)
    print("Válido:", n.calificacion)
except ValueError as err:
    print("Error:", err)

try:
    Nota(12.0)
except ValueError as err:
    print("Rechazado:", err)

print("\n--- Contraseña ---")
try:
    c = Contrasena("Clave2026")
    print("Válido:", c.valor)
except ValueError as err:
    print("Error:", err)

try:
    Contrasena("abc123")
except ValueError as err:
    print("Rechazado:", err)

print("\n--- Teléfono ---")
try:
    t = Telefono("71234567")
    print("Válido:", t.numero)
except ValueError as err:
    print("Error:", err)

try:
    Telefono("712345")
except ValueError as err:
    print("Rechazado:", err)



# Un poco de contexto: qué hace cada clase y qué revisa antes de validar

#
# Email:
#   Esta clase representa un correo electrónico, pero no deja que
#   cualquier texto se convierta en uno. Apenas se crea el objeto,
#   revisa que el texto tenga un arroba y un punto, que son las dos
#   señas mínimas de que algo realmente es un correo. Si falta una
#   de las dos, el objeto ni siquiera llega a formarse.
#
# Edad:
#   Esta clase guarda la edad de una persona, pero antes de aceptar
#   el número se asegura de que sea un entero y de que caiga dentro
#   de un rango de vida posible, entre 0 y 120. De esa forma no se
#   cuelan edades negativas ni cifras que no tienen sentido humano.
#
# Nota:
#   Esta clase representa una calificación dentro de la escala de
#   0 a 10. Al crear el objeto, comprueba que el número entregado
#   esté dentro de ese rango; si alguien intenta poner un 15 o una
#   nota negativa, la clase simplemente no lo deja pasar.
#
# Contraseña:
#   Esta clase guarda una contraseña, pero antes de aceptarla revisa
#   tres cosas al mismo tiempo: que tenga al menos 8 caracteres, que
#   incluya una mayúscula y que tenga al menos un número. Son las
#   condiciones mínimas para que no sea una contraseña demasiado
#   fácil de adivinar.
#
# Teléfono:
#   Esta clase representa un número de teléfono en formato de
#   El Salvador. Antes de guardarlo, verifica que esté compuesto
#   solo por dígitos y que tenga exactamente 8, que es el largo que
#   usan los números en el país. Si trae letras o le faltan dígitos,
#   el objeto no se crea.