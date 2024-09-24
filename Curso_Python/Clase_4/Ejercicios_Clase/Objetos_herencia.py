class Rueda:
    def __init__(self, marca: str = "Michelin"):
        self.marca = marca
        self.pinchada = False

    def pincharse(self):
        self.pinchada = True

class Motor:
    def __init__(self, cilindrada: int):
        self.cilindrada = cilindrada if cilindrada else 1400

class Asiento:
    def __init__(self, material: str):
        self.material = material

class BolaRemolque:
    def __init__(self, carga: float):
        self.carga = carga

class Vehiculo:
    def __init__(self, matricula: str, marca: str, color: str, *, n_ruedas: int,
                                                                cilindrada_motor: int = None,
                                                                n_asientos: int = 1):
        self.matricula = matricula
        self.marca = marca
        self.color = color
        self.ruedas = [Rueda() for rueda in range(n_ruedas)]
        self.motor = Motor(cilindrada_motor)
        self.asientos = [Asiento() for asientos in range(n_asientos)]
 
    def __str__(self):
        return f"{self.marca} {self.color} con matrícula {self.matricula}, {self.ruedas} ruedas y motor {self.motor}"
 
class Coche(Vehiculo):
    def __init__(self, matricula: str, marca: str, color: str, *, n_ruedas: int,
                                                                cilindrada_motor: int = None,
                                                                n_asientos: int,
                                                                peso_carga: float):
        super().__init__(matricula, marca, color, n_ruedas=4, n_asientos=5)  # Inicializamos los campos del padre
        self.carroceria = ": Deportivo"
        self.bola_de_carga = BolaRemolque(peso_carga)
 
    def __str__(self):
        return f"{super().__name__}, carrocería {self.carroceria} y {self.asientos} asientos"
 
class Moto(Vehiculo):
    def __init__(self, matricula: str, marca: str, color: str, *, n_ruedas: int,
                                                                cilindrada_motor: int = None,
                                                                n_asientos: int):
        super().__init__(self, matricula, marca, color) # Inicializamos los campos del padre

    def __str__(self):
        return f"{super().__name__} y {self.asiento} asiento"
 
# Crear instancias de Coche y Moto con matrículas diferentes
coche = Coche("1234-ABC", "BMW", "Rojo", "V12")
moto = Moto("5678-DEF", "Yamaha", "Azul", "500cc")
 
# Imprimir detalles de los vehículos
print(coche)
print(moto)