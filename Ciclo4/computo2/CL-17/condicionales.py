edad = 16
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

nota = 4.9

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprobado")
elif nota >= 5 and nota < 7:
    print("insuficiencia")
else:
    print("Reprobado")

## usamos el for cuando queremmos rcorrer una secuencia de elementos, como una lista o un rango de números.

clientes = ["Juan", "María", "Pedro", "Ana"]

for cliente in clientes:
    print("Hola", cliente)


## usamos for con range para recorrer un rango de números

for i in range(5):
    print("hola")


#while se usa cuando queremos ejecutar un bloque de código mientras una condición sea verdadera.

contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador += 1

