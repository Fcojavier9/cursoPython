# Función lambda para pedir un número
pedir = lambda: int(input("Introduzca un número: "))

# Pedir números hasta que se meta 0 
# y dar la suma de todos esos números
def pedir_numeros(pedir: callable) -> int: # La función pedir es un parámetro de entrada, por eso se le pone el tipo callable
    entradas = []
    numero = pedir()  # Llamada inicial a la función pedir
    while numero != 0:
        entradas.append(numero)
        numero = pedir()  # Volver a llamar a la función para la siguiente entrada
    return sum(entradas)

# Imprimir la suma de los números
print(f"La suma es: {pedir_numeros(pedir)}")