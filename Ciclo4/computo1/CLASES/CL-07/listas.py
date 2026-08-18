estudiantes = ["Ana", "Luis", "Pedro", "Carlos", "Maria"]
print(estudiantes)  # Imprime la lista completa de estudiantes
print(estudiantes[0])  # Imprime el primer estudiante
print(estudiantes[1])  # Imprime el segundo estudiante
print(estudiantes[2])  # Imprime el tercer estudiante
print(estudiantes[3])  # Imprime el cuarto estudiante
print(estudiantes[-1])  # Imprime el quinto estudiante

#si requerimos agg regar un nuevo estudiante a la lista, podemos usar el metodo append
estudiantes.append("Jorge")
print(estudiantes)  # Imprime la lista completa de estudiantes después de agregar a Jorge

#remover un estudiante de la lista, podemos usar el metodo remove
estudiantes.remove("Luis")
print(estudiantes)  # Imprime la lista completa de estudiantes después de remover a Luis

#ejercicio: una lista de compras de frutas a comprar el mercado por unidad  que incluya: 2 manazanas , banana, uva , manzana. 

Lista_De_Mercado = ["manzana", "manzana", "banana", "uva", "manzana"]
print(Lista_De_Mercado)  # Imprime la lista completa de frutas a comprar
# accedemos a la palabra banana de la lista de frutas
print(Lista_De_Mercado[2])  # Imprime la fruta en la posición 2 de la lista (banana)

# agg la fruta pera a la lista de frutas
Lista_De_Mercado.append("pera")
print(Lista_De_Mercado)  # Imprime la lista completa de frutas después de agregar la pera

#eliminamos 2 manzana y que al menos queda una manzana en la lista de frutas
Lista_De_Mercado.remove("manzana")
Lista_De_Mercado.remove("manzana")
print(Lista_De_Mercado)  # Imprime la lista completa de frutas después de remover una manzana