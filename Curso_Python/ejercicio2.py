class Alumno:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    def __str__(self):
        return f'Alumno: {self._nombre}, Edad: {self._edad}'


class Aula:
    def __init__(self, numero_aula: int):
        self._numero_aula = numero_aula
        self._alumnos = []

    @property
    def numero_aula(self):
        return self._numero_aula

    def agregar_alumno(self, alumno: Alumno):
        self._alumnos.append(alumno)

    def mostrar_alumnos(self):
        for alumno in self._alumnos:
            print(alumno)

    def __str__(self):
        return f'Aula {self._numero_aula} con {len(self._alumnos)} alumnos'


def crear_y_asignar_alumnos_a_aula(aula: Aula, lista_alumnos: list):
    for nombre, edad in lista_alumnos:
        alumno = Alumno(nombre, edad)
        aula.agregar_alumno(alumno)


if __name__ == "__main__":

    aula1 = Aula(1)

    lista_de_alumnos = [
        ("Bonifacio", 16),
        ("Camarón", 17),
        ("Benito", 15)
    ]

    crear_y_asignar_alumnos_a_aula(aula1, lista_de_alumnos)

    print(aula1)
    aula1.mostrar_alumnos()

    venancio = Alumno("Venancio", 18)
    aula1.agregar_alumno(venancio)
    print(aula1)
    aula1.mostrar_alumnos()