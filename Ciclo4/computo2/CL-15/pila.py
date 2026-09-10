# pila = []

# #Agreguemos 3 elementos a la pila

# pila.append("A")
# pila.append("B")
# pila.append("C")

# #Mostramos la pila
# print("Pila actual:", pila)

# #agregamos dos elementos mas a la pila

# pila.append("D")
# pila.append("E")

# print("pila Actualizada:", pila);


def push(pila, elemento): #estamos creando una funcion llamada push que recibe dos parametros pila y elemento
    pila.append(elemento) # agregamos el elemento a la pila usando el metodo append

def pop(pila): #estamos creando una funcion llamada pop que recibe un parametro pila
        return pila.pop() # si no esta vacia eliminamos el ultimo elemento de la pila y lo retornamos


#creamos una pila vacia

pilas = [] # creamos una lista vacia que representara nuestra pila
push(pilas, "A") # agregamos el elemento "A" a la pila usando la funcion push
push(pilas, "B") # agregamos el elemento "B" a la pila usando la funcion push
push(pilas, "C") # agregamos el elemento "C" a la pila usando la funcion push

print("Pila actual:", pilas) # mostramos la pila actual

# para usar el metodo pop se necesita una nueva variable que guarde el valor que se elimino de la pila, ya que si no se guarda el valor se pierde y no se puede usar despues

elemento=pop(pilas) # eliminamos el ultimo elemento de la pila usando la funcion pop y lo guardamos en la variable elemento
print("Elemento eliminado:", elemento) # mostramos el elemento eliminado

# Ejercicio: Crear una pila que simule un sistema de aceleracion de un automovil, donde se agreguen elementos que representen la velocidad del automovil

def push(Vel_inicial, Inc_veL): #estamos creando una funcion llamada push que recibe dos parametros pila y elemento
    Vel_inicial.append(Inc_veL) # agregamos el elemento a la pila usando el metodo append

automovil = [] # creamos una lista vacia que representara nuestra pila de velocidades
push(automovil, 0) # agregamos la velocidad inicial del automovil (0) a la pila usando la funcion push
push(automovil,20) # agregamos la velocidad 20 a la pila usando la funcion push
push(automovil,40) # agregamos la velocidad 40 a la pila usando la funcion push
print("Velocidades del automovil:", automovil) # mostramos las velocidades del automovil


# el ejercicio decia que lo hicieramos en 10 Km el aumento pero en este caso yo lo hice en 20 Km para que se vea mas rapido el aumento de velocidad, pero si quieren pueden cambiarlo a 10 Km y veran que funciona igual.


#ejercicio original

def acelerar(velocidad_inicial): # estamos creando una funcion llamada acelerar que recibe un parametro velocidad_inicial
    nueva_velocidad = velocidad_inicial + 10 # aumentamos la velocidad inicial en 10 y la guardamos en la variable nueva_velocidad
    return nueva_velocidad


velocidad_inicial = int(input("Ingrese la velocidad inicial del automóvil: ")) #le pedimos al usurio que ingrese la velocidad inicial del automovil y la guardamos en la variable velocidad_inicial

velocidad_final = acelerar(velocidad_inicial) # llamamos a la funcion acelerar y le pasamos como parametro la velocidad inicial, y guardamos el resultado en la variable velocidad_final

print("Velocidad inicial:", velocidad_inicial) # mostramos la velocidad inicial del automovil
print("Velocidad después de acelerar:", velocidad_final) #Mostramos la velocidad final del automovil depsues de acelerar


#la tarea es aplicar el LIFO por completo (desacelerar el vehiculo)

pila = [velocidad_inicial, velocidad_final] # creamos una pila y metemos las dos velocidades que ya teniamos (push)

pila.pop() # sacamos la ultima velocidad que entro a la pila (pop), que es la velocidad_final

velocidad_final = pila[-1] # la velocidad final ahora es la que quedo en el tope de la pila, o sea la velocidad_inicial

print("Velocidad después de desacelerar:", velocidad_final) # mostramos la velocidad despues de desacelerar



