# Actividad: Listas, Tuplas y Sets
# Ejemplo elegido: Registro de cursos aprobados

# Lista: los cursos van cambiando ciclo a ciclo, se agregan conforme los voy aprobando
cursos_aprobados = ["Programación Orientada a Objetos", "Gestión de Servidores Web"]

# Tupla: el detalle de un curso ya cerrado no cambia (curso, ciclo, nota), por eso va en tupla
curso_detalle = ("Manejo y Estructura de Datos", "Ciclo IV", 9.0)

# Set: sirve para comprobar que ningún curso quede repetido en el registro
cursos_unicos = {"Programación Orientada a Objetos", "Gestión de Servidores Web", "Manejo de Estructura de Datos"}

print("Cursos aprobados:", cursos_aprobados)
print("Detalle de un curso:", curso_detalle)
print("Cursos sin duplicados:", cursos_unicos)

# se agrega un curso nuevo a la lista, porque la lista sí se puede modificar
cursos_aprobados.append("Metodología de la Investigación")
print("Lista actualizada:", cursos_aprobados)

# Uso una lista para los cursos aprobados porque esa lista va creciendo: cada ciclo meto uno nuevo con append(). Uso una tupla para el detalle de un curso ya cerrado porque esos datos (nombre, ciclo, nota) ya no cambian, y así no los toco por error. Y uso un set para que no se me repita ningún curso en el registro, porque los sets no dejan duplicados.