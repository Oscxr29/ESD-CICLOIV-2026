# ESD - Manejo y Estructura de Datos

Repositorio académico de la materia **Manejo y Estructura de Datos**.
El material está organizado por cómputo, clases, prácticas y tareas dentro de
la carpeta `Ciclo4`.

## Requisitos

- Python 3.10 o posterior.
- Jupyter Notebook para abrir los archivos `.ipynb`.
- No se requieren dependencias externas para los scripts de Python; utilizan la
  biblioteca estándar.

## Uso rápido

Clona el repositorio y entra en su carpeta:

```powershell
git clone https://github.com/Oscxr29/ESD-CICLOIV-2026.git
Set-Location .\ESD-CICLOIV-2026
```

Ejecuta cualquier script desde la raíz del repositorio. Por ejemplo:

```powershell
python .\Ciclo4\computo1\CLASES\CL-01\index.py
```

En Windows también puedes usar `py`:

```powershell
py .\Ciclo4\computo2\CL-20\ArbolBST.py
```

Para abrir las prácticas de Jupyter:

```powershell
python -m pip install notebook
jupyter notebook
```

> **Nota:** varios programas solicitan datos con `input()`. Deben ejecutarse
> desde una terminal interactiva. Las rutas de este README usan `/` para que
> los enlaces funcionen en GitHub; los comandos de PowerShell usan `\`.

## Estructura real del repositorio

```text
ESD/
├── readme.md
└── Ciclo4/
    ├── computo1/
    │   └── CLASES/
    │       ├── CL-01/
    │       ├── CL-02/
    │       ├── CL-03/
    │       ├── CL-07/
    │       ├── CL-08/
    │       ├── CL-09/
    │       ├── CL-10/
    │       └── LAB-01/
    ├── computo2/
    │   ├── CL-15/
    │   ├── CL-17/
    │   ├── CL-18/
    │   ├── CL-19/
    │   └── CL-20/
    ├── Practicas/
    │   ├── computo1/
    │   └── computo2/
    └── TAREAS/
        ├── computo1/
        └── computo2/
```

## Navegación rápida

- [Cómputo 1: clases y laboratorio](./Ciclo4/computo1/CLASES/)
- [Cómputo 2: clases 15 a 20](./Ciclo4/computo2/)
- [Prácticas de cómputo 1](./Ciclo4/Practicas/computo1/)
- [Prácticas de cómputo 2](./Ciclo4/Practicas/computo2/)
- [Tareas de cómputo 1](./Ciclo4/TAREAS/computo1/)
- [Tareas de cómputo 2](./Ciclo4/TAREAS/computo2/)

## Cuadernillo 1: fundamentos

Material ubicado en [Cómputo 1](./Ciclo4/computo1/CLASES/):

- [CL-01: introducción](./Ciclo4/computo1/CLASES/CL-01/index.py)
- [CL-02: ejercicio de temperatura](./Ciclo4/computo1/CLASES/CL-02/temp.py)
- [CL-03: entrada, números y variables](./Ciclo4/computo1/CLASES/CL-03/)
  - [input.py](./Ciclo4/computo1/CLASES/CL-03/input.py)
  - [numeros.py](./Ciclo4/computo1/CLASES/CL-03/numeros.py)
  - [variabeles.py](./Ciclo4/computo1/CLASES/CL-03/variabeles.py)

## Cuadernillo 2: estructuras de datos base

- [CL-07: índices y listas](./Ciclo4/computo1/CLASES/CL-07/)
- [CL-08: diccionarios](./Ciclo4/computo1/CLASES/CL-08/)
- [CL-09: tuplas, conjuntos y ejercicios](./Ciclo4/computo1/CLASES/CL-09/)
- [CL-10: pila](./Ciclo4/computo1/CLASES/CL-10/pila.py)
- [LAB-01: laboratorio](./Ciclo4/computo1/CLASES/LAB-01/)

## Cuadernillo 3: lógica, nodos y árboles

Todo el material de este cuadernillo está en
[Ciclo4/computo2](./Ciclo4/computo2/).

### CL-15: funciones, pilas y vehículo

- [funciones.py](./Ciclo4/computo2/CL-15/funciones.py): funciones con
  parámetros, retornos y saludo interactivo.
- [pila.py](./Ciclo4/computo2/CL-15/pila.py): operaciones `push` y `pop`,
  además del ejercicio de aceleración y desaceleración de un vehículo usando
  LIFO.

La tarea del vehículo **sí existe**, pero está integrada en `pila.py`; no hay
un archivo separado con el nombre `vehiculo.py`.

### CL-17: condicionales y bucles

- [condicionales.py](./Ciclo4/computo2/CL-17/condicionales.py): `if`,
  `elif`, `else`, `for` y `while`.

### CL-18: colas FIFO y banco

- [cola.py](./Ciclo4/computo2/CL-18/cola.py): `enqueue`, `dequeue`, `peek`,
  tamaño y comprobación de cola vacía.
- [banco.py](./Ciclo4/computo2/CL-18/banco.py): sistema interactivo de turnos
  de un banco.

### CL-19: nodos y árbol binario

- [temp.py](./Ciclo4/computo2/CL-19/temp.py): clase `Nodo`, árbol binario y
  comprobación de hojas.

### CL-20: árbol binario de búsqueda

- [ArbolBST.py](./Ciclo4/computo2/CL-20/ArbolBST.py): inserción, búsqueda,
  actualización, eliminación y recorrido inorden de un inventario BST.

## Prácticas

### Cómputo 1

- [P1.py](./Ciclo4/Practicas/computo1/P1.py)
- [P2.py](./Ciclo4/Practicas/computo1/P2.py)
- [P3.py](./Ciclo4/Practicas/computo1/P3.py)
- [P4.py](./Ciclo4/Practicas/computo1/P4.py)
- [Ejemplos.ipynb](./Ciclo4/Practicas/computo1/Ejemplos.ipynb)
- [practica03.ipynb](./Ciclo4/Practicas/computo1/practica03.ipynb)

### Cómputo 2

- [P5.ipynb](./Ciclo4/Practicas/computo2/P5.ipynb)
- [P6.ipynb](./Ciclo4/Practicas/computo2/P6.ipynb)
- [P7.ipynb](./Ciclo4/Practicas/computo2/P7.ipynb)
- [P8.ipynb](./Ciclo4/Practicas/computo2/P8.ipynb): árboles binarios y
  recorridos.
- [P9.ipynb](./Ciclo4/Practicas/computo2/P9.ipynb): listas enlazadas, nodos,
  historial de navegación y métricas.
- [practica05.ipynb](./Ciclo4/Practicas/computo2/practica05.ipynb)
- [practica06.ipynb](./Ciclo4/Practicas/computo2/practica06.ipynb)

## Tareas y evaluaciones

- [Ejercicio_String.py](./Ciclo4/TAREAS/computo1/Ejercicio_String.py)
- [ejertuplas.py](./Ciclo4/TAREAS/computo1/ejertuplas.py)
- [terminal_buses.py](./Ciclo4/TAREAS/computo2/terminal_buses.py):
  integra cola de pasajeros, pila de salidas y árbol de destinos.
- [parcial_esd.py](./Ciclo4/TAREAS/computo2/parcial2/parcial_esd.py):
  integra cola FIFO, pila LIFO y árbol BST, e incluye pruebas automáticas.
