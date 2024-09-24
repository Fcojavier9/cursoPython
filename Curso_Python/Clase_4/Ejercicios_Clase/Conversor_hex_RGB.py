conversor = lambda numero_hex: int(numero_hex, 16)

def hex_string_to_RGB(hex_string : str) -> dict:
    
    # divido por trozos 
    rojo, verde, azul = [hex_string[1:3], hex_string[3:5], hex_string[5:]] # en el ultimo es 5: porque  es desde la pos 5 hasta el final
        
    return {
        "r" : conversor(rojo), # int(valor,base a convertir)
        "g" : conversor(verde), 
        "b" : conversor(azul)
    }


# Tambien se podria hacer con generadores
def hex_string_to_RGB2(hex_string : str) -> dict:
    
    # divido por trozos 
    numeros_hex = [hex_string[1:3], hex_string[3:5], hex_string[5:]] # en el ultimo es 5: porque  es desde la pos 5 hasta el final
    
    rojo, verde, azul = (conversor(numero) for numero in numeros_hex)

    return {
        "r" : rojo,
        "g" : verde, 
        "b" : azul
    }

print(hex_string_to_RGB("#FF9933")) # {'r': 255, 'g': 153, 'b': 51}
print(hex_string_to_RGB2("#FF9933") )