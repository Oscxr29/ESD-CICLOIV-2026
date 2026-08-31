estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "cursos": ["Mate", "Python", "ESD"],
    }

print(estudiante)
print(estudiante["nombre"])

# Agregar y modificar elementos
estudiante["edad"] = 21
estudiante["cursos"].append("Inglés")
estudiante["Carrera"] = "Ingeniería de Sistemas"

print(estudiante)

#eliminamos la edad
del estudiante["edad"]
print(estudiante)

#eliminar con el metodo pop
estudiante.pop("Carrera")