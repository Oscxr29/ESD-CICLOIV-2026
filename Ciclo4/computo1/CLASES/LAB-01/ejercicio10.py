ing_software = {"Programación", "Base de Datos", "Matemática", "Análisis y Diseño de Sistemas", "Arquitectura de Software", "Metodologías Ágiles"}
ing_sistemas = {"Programación", "Base de Datos", "Matemática", "Redes de Computadoras", "Sistemas Operativos", "Arquitectura de Computadoras"}
ing_datos = {"Programación", "Base de Datos", "Matemática", "Estadística", "Machine Learning", "Inteligencia Artificial"}

# lo que se repite en las 3 carreras
comunes = ing_software & ing_sistemas & ing_datos
print("Materias comunes a las 3 carreras:", comunes)

# lo que le queda solo a cada carrera despues de quitar lo de las otras 2
exclusivas_software = ing_software - ing_sistemas - ing_datos
exclusivas_sistemas = ing_sistemas - ing_software - ing_datos
exclusivas_datos = ing_datos - ing_software - ing_sistemas
print("Solo en Ingeniería de Software:", exclusivas_software)
print("Solo en Ingeniería en Sistemas:", exclusivas_sistemas)
print("Y en Ciencia de Datos, exclusivas:", exclusivas_datos)

# todas juntas, sin duplicados
union_total = ing_software | ing_sistemas | ing_datos
print("Unión de todas las materias:", union_total)
print("Total de materias únicas:", len(union_total))