# 1
class Alumno:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def __str__(self):
        return f"Alumno({self.nombre}, {self.edad}, {self.notas})"

# 2
class Aula:
    def __init__(self, nombre, max_alumnos=30):
        self.nombre = nombre
        self.alumnos = []
        self.max_alumnos = max_alumnos

    # 3
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def __str__(self):
        return f"Aula({self.nombre}, {len(self.alumnos)} alumnos)"

# 4
def crear_alumno(nombre, edad, notas):
    nuevo_alumno = Alumno(nombre, edad, notas)
    return nuevo_alumno

# 5
def asignar_alumno_a_aula(alumnos, aula):
    if len(alumnos) + len(aula.alumnos) > aula.max_alumnos:
        raise Exception(f"No se pueden agregar más alumnos, el aula {aula.nombre} ya está llena (máximo {aula.max_alumnos} alumnos).")
    else:
        for alumno in alumnos:
            aula.agregar_alumno(alumno)

# 6
aula_especial = Aula("Aula para alumnos especiales", 10)
alumno1 = crear_alumno("Luis", 15, [8, 9, 7])
alumno2 = crear_alumno("Marta", 16, [7, 8, 9])

# Intentamos agregar más alumnos de los que el aula puede soportar
try:
    asignar_alumno_a_aula([ alumno1, alumno2, alumno1, alumno2, alumno1, alumno2, alumno1, alumno2], aula_especial)
except Exception as e:
    print(e)

print(aula_especial)
print(alumno1)
print(alumno2)
