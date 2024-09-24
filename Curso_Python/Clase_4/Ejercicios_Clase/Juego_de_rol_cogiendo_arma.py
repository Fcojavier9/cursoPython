class Personaje:
    def __init__(self, nombre: str, rol: str):
        self.nombre = nombre
        self.rol = rol
        self.puntos_vida = 100
        self.nivel = 1
        self.inventario = []
        self.daño = 10
        print(f"Se ha creado a {self.nombre}, un {self.rol} de nivel {self.nivel}!")
 
    def ataque_basico(self, arma):
        if len(self.inventario) > 0:
            print(f"{self.nombre} ha atacado con un arma! Y su daño es {self.daño + arma.ataque}")
        else:
            print(f"{self.nombre} ha atacado! Y su daño es {self.daño}")

    def coger_arma(self, arma):
        self.inventario.append(arma)
        print(f"Has cogido un {arma.nombre}!")

class Arma:
    def __init__(self, nombre: str, ataque: int):
        self.nombre = nombre
        self.ataque = ataque


cetro = Arma("Cetro magico", 40)
gandal = Personaje("Gandalf", "mago")
gandal.coger_arma(cetro)
gandal.ataque_basico(cetro)