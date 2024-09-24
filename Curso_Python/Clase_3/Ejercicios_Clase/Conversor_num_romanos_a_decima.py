# prueba
prueba = "XLVIII"

# Diccionario con los valores de los numeros romanos
equivalencia = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Funcion para validar si el numero romano es correcto
def es_valido(numero_romano: str) -> bool:
    contador = 1
    for i in range(1, len(numero_romano)):
        if numero_romano[i] == numero_romano[i - 1]:
            contador += 1
            if contador > 3:
                return False
        else:
            contador = 1
    return True

# Funcion que recibe un numero romano y devuelve su valor en decimal
def convertir_a_decimal(numero_romano: str) -> int:
    resultado = 0

    if not es_valido(numero_romano):
        return "Numero romano invalido"
    
    # num para llevar la posicion del numero romano y valor para el valor del numero romano
    for num, valor in enumerate(numero_romano):
        # Si el valor actual es menor que el siguiente
        if num + 1 < len(numero_romano) and equivalencia[valor] < equivalencia[numero_romano[num + 1]]:
            resultado -= equivalencia[valor]
        else:
            resultado += equivalencia[valor]
    return resultado

print(convertir_a_decimal(prueba))