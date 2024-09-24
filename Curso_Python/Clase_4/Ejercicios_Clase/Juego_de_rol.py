class Personaje:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol
        self.puntos_vida = 100
        self.nivel = 1
        self.status = True
        self.inventario = []
        print(f"Se ha creado a {self.nombre}, un {self.rol} de nivel {self.nivel}!")

    # self hace referencia al objeto que se está creando
    # no se puede tipar el retorno porque imprime por pantalla
    def atacar(self, objetivo):
        print(f"{self.nombre} ha atacado a {objetivo.nombre}!")
        objetivo.puntos_vida -= 50
        if(objetivo.puntos_vida <= 0):
            self.subir_nivel()
            print(f"{objetivo.nombre} ha muerto!")
        else:
            print(f"{objetivo.nombre} ahora tiene {objetivo.puntos_vida} puntos de vida.")

    # función para subir de nivel
    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nombre} ha subido a nivel {self.nivel}!")

personaje1 = Personaje("Gandalf", "mago")
personaje2 = Personaje("Aragorn", "guerrero")

personaje1.atacar(personaje2)
personaje1.atacar(personaje2)