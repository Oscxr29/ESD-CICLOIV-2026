nombre = "Oscar Aguilar" #string
edad = 19 #int
promedio = 8.7 #flotante
becado = True #booleano

print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Promedio: {promedio}")
print(f"Becado: {'Sí' if becado else 'No'}")
# en resumen se imprimieron las variables y se define que tipo de dato es cada una de ellas y la f se uso para imprimir las variables de string y definir su tipo de dato


# cálculo con las variables numéricas

colegiatura = 125 #ejemplo que vale esta cantidad la mensualidad
descuento = colegiatura * becado * 0.5  # si becado es True, aplica 50% del descuento en este caso , si no fuera becado no aplica el descuento
print(f"Descuento aplicado: ${descuento}")