prueba = "127.0.0.1"

# Funcion que recibe una ip y devuelve si es valida o no
def validar_ip(ip: str) -> str:
    bloques_ip = ip.split(".") # separo la ip por puntos

    if len(bloques_ip) != 4:
        return "Invalida"
    
    for bloque in bloques_ip:
        # si el bloque no es un numero o no esta en el rango 0-255
        if not bloque.isdigit() or not 0 <= int(bloque) < 255:
            return "Invalida"
    return "Valida"

print(validar_ip(prueba))