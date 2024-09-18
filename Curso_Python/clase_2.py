# 1 - modificar un array de strings
var = ["john palmer", "DOe Toe", "sTaRlEtTe TOTETE", "TesT 2"]

for nombre in var:
    print(nombre.capitalize())
    print(nombre.lower())
    print(nombre.upper())
    print(nombre.title())
    print(nombre.swapcase())
    print(nombre.replace("e", "i"))
    print(nombre.replace("T", "X"))
    print(nombre.replace("T", "X", 1))
    print(nombre.count("T"))
    print(nombre.find("T"))
    print(nombre.rfind("T"))
    print(nombre.startswith("j"))
    print(nombre.endswith("T"))
    print("-------------")

# otra manera de hacerlo y lo devuelve en array, parecido a map
var_minusculas = [elemento.lower() for elemento in var]
print(var_minusculas) 
print("-------------")

# otra manera mas seria con append igual que la de arriba ↑
lista_vacia = []
for nombre in var:
        lista_vacia.append(nombre.lower())
print(lista_vacia)
print("-------------")

# ---------------------------------------------------------------------- #

# LISTAS

# 2 - Encontrar el máximo de una lista de números
lista = [1, 4, 7, 2, 3, 9, 4, 1]
maximo = max(lista)
print("El máximo de la lista es: ", maximo)


# 3 - Calcular la media de una lista de números
media = sum(lista) / len(lista)
print("La media de la lista es: ", media)


# 4 - Crear un filtro de obscenidad
texto = "El equipo rojo es una mierda, no valen para nada, saco de mierda"
obscenidad = ["mierda", "caca", "culo"]
for i in obscenidad:
    if i in texto:
        texto = texto.replace(i, "****")
print(texto)
print("-------------")

# ---------------------------------------------------------------------- #

# DICCIONARIOS
edades = {
     "nombre" : "Juan", 
     "edad" : 25,
}

nombre = edades["nombre"]
edad = edades["edad"]

print(f"{nombre} tiene {edad} años")
respuesta = "Es mayor de edad" if edad >= 18 else "Es un niño"
print(respuesta)
print("-------------")

# ---------------------------------------------------------------------- #

# 5 - Diccionario de personas
personas = {
    "persona_1": {
        "nombre": "Joaquin",
        "apellido": "Hernandez",
        "edad": 30,
        "trabajo": "ingeniero",
        "hobbies": {"astronomia": 40,
                          "fotografia":25,
                          "cocina": 66}
    },
    "persona_2": {
        "nombre": "Joaquin",
        "apellido": "Hernandez",
        "edad": 12,
        "trabajo": "ingeniero",
        "hobbies": ["astronomia", "fotografia", "cocina"]
    },
    "persona_3": {
        "nombre": "Joaquin",
        "apellido": "Hernandez",
        "edad": 8,
        "trabajo": "ingeniero",
        "hobbies": ["astronomia", "fotografia", "cocina"]
    },
}

for persona in personas.values():
        # ternario en python
        print("Es mayor de edad" if persona["edad"] >= 18 else "Es un niño")
        print("Su hobbie es: ", persona["hobbies"])
print("-------------")

# ---------------------------------------------------------------------- #

# 6 - crear tablas de multiplicar
numero_tabla = int(input("De que número quieres la tabla de multiplicar: "))
for numero in range(1, 11):
    print(f"{numero_tabla} x {numero} = {numero_tabla * numero}")

# ---------------------------------------------------------------------- #

# 7 - Ejercicio crear un diccionario con dos listas

claves = [1, 2, 3, 4, 5]
valores = ["Juan", "Ana", "Raquel", "Antonio", "Belen"]

# dict() crea un diccionario a partir de dos listas
# zip() combina dos listas en una lista de tuplas
diccionario = dict(zip(claves, valores))
print(diccionario)

# con comprension de diccionarios
diccionario3 = {clave: valor for clave, valor in zip(claves, valores)}
print(diccionario3)

# con bucle for seria
diccionario2 = {}
for indice, clave in enumerate(claves):
    diccionario2[clave] = valores[indice]
print(diccionario2)

# tener un diccionario y crear dos listas
claves = list(diccionario.keys()) # list() convierte las claves en una lista
valores = list(diccionario.values()) # list() convierte los valores en una lista
print(claves)
print(valores)
