materias = ["Programación Orientada a Eventos", "Estructura de Datos", "Base de Datos", "Programacion Orientada a Objetos", "Redes"]

print(materias)  # lista completa

materias.append("Matematica 4")
materias.append("Inglés 2")
print(materias)  #  después de agregar 2 con append()

materias.insert(2, "Gestion de Servidores")
print(materias)  # insertada en la posición 2

materias.remove(materias[-1])
print(materias)  #  se elimina la última con remove()

print(len(materias))  # número total de materias
#en resumen se imprimieron las materias y se agregaron 2 materias mas y se elimino la ultima materia de la lista y se imprimio el numero total de materias