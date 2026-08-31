# Caso 2: Gestion con Sets - verificacion de requisitos academicos para inscribirse a una materia

"""
### Justificación (Caso 2: Gestión con Sets)

* Por qué usé Sets: Elegí trabajar con conjuntos ('set') porque para los listados de materias no nos importa el orden y no tiene sentido tener duplicados. Además, son la mejor opción en Python cuando necesitas comparar grupos de datos rápidamente.

* El método que usé: En lugar de armar un bucle 'for' para revisar materia por materia, simplemente apliqué la resta de conjuntos (el operador '-'). Al hacer 'requisitos - aprobadas', Python calcula automáticamente las materias que faltan. Me ahorra líneas de código, no necesito condicionales extra y la lógica queda súper limpia y fácil de leer.
"""


materias_aprobadas = {"Programación", "Estructura de Datos", "Matemática 4"}

requisitos_poo = {"Programación", "Estructura de Datos"}
requisitos_bd = {"Programación", "Matemática 4", "Estadística"}

def puede_inscribirse(requisitos, aprobadas):
    faltantes = requisitos - aprobadas  # lo que pide la materia menos lo que ya se tiene
    return len(faltantes) == 0, faltantes

puede, faltantes = puede_inscribirse(requisitos_poo, materias_aprobadas)
print("¿Puede inscribirse a POO?:", "Sí" if puede else "No")

puede, faltantes = puede_inscribirse(requisitos_bd, materias_aprobadas)
print("¿Puede inscribirse a Base de Datos?:", "Sí" if puede else "No")
if not puede:
    print("Le faltan estas materias:", faltantes)

