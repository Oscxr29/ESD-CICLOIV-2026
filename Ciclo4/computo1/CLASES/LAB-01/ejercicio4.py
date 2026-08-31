edad = 20            # Entero
promedio = 8.5       # flotante
nombre = "Oscar"      # string
activo = True        # booleano

print(f"Variable: edad = {edad}, Tipo: {type(edad)}") 
print(f"Variable: promedio = {promedio}, Tipo: {type(promedio)}") 
print(f"Variable: nombre = \"{nombre}\", Tipo: {type(nombre)}") 
print(f"Variable: activo = {activo}, Tipo: {type(activo)}")
# en resumen se imprimieron las variables y se define que tipo de dato es cada una de ellas y la f se uso para imprimir las variables de string y definir su tipo de dato

# anexamos todas las variables para imprimir un solo mensaje 
mensaje = "Hola " + nombre + ", tu promedio mas 1 punto es " + str(promedio + 1)
print(mensaje)