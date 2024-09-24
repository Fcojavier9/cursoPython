# 6- Validar una lista de telefonos
    # parametro es por defecto un string y devuelve un booleano
def validar_telefono(telefono: str) -> bool:
    tel = telefono.replace(" ", "")
    if len(tel) != 9 and not tel.isdigit() and tel[0] not in ("6", "7"):
        return False
    return True

lista_telefonos = ["696 02 68 63", "666 66 66     66", "74782 19_32"]

for telefono in lista_telefonos:
    print(f"Telefono valido: {telefono}", ) if validar_telefono(telefono) else print(f"Telefono invalido: {telefono}")
