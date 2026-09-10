def saludar():
    print("¡Hola! Bienvenido a la función de saludo.")

saludar()


def suma (a, b):
    return a + b

sum =  suma(3, 5)
print("La suma es:", sum)


#parametros

def saludar(nombre):
    print("hola", nombre)
nombre= input("Ingrese su nombre: ")
nombre2 = input("Ingrese su segundo nombre: ")
saludar(nombre + " " + nombre2);
# saludar(nombre); como opciones individuales si son dos nombres distintos
# saludar(nombre2);
