# Elevar al cuadrado todos los digitos de un string
entrada = input("Ingrese un numero: ")

def elevar_cuadrado(digitos: str) -> list[int]: # devuelve una lista de enteros
    digitos_elevados = []
    for digito in digitos:
        # Verifico si el digito es un numero
        if digito.isdigit():
            # Agrego el digito elevado al cuadrado a la lista
            digitos_elevados.append(int(digito)**2)
    return digitos_elevados

print(elevar_cuadrado(entrada))

