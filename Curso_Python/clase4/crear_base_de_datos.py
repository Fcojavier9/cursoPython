# 5- Crear una base de datos de alumnos con nombre, edad y notas
class Alumno:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Notas: {self.notas}"

# Diccionario para almacenar a los alumnos, usando el nombre como clave
alumnos = {}

# Bucle para pedir la información
aux = 1
while True:
    nombre = input("Introduce el nombre del alumno (o 'salir' para terminar): ")
    if nombre.lower() in ('salir','exit','stop','out') :
        break
    edad = int(input(f"Introduce la edad de {nombre}: "))
    notas = input(f"Introduce las notas de {nombre} separadas por comas: ").split(',')

    # Crear un objeto Alumno y agregarlo al diccionario
    alumno = Alumno(nombre, edad, notas)
    alumnos[aux] = alumno  # El nombre es la clave en el diccionario
    aux += 1

# Mostrar los datos de los alumnos ingresados
print("\nDatos de los alumnos ingresados:")
for indice, alumno in alumnos.items():
    print(indice)
    print(alumno)