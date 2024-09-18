# 3- Alumnos: Comprobar si primera y ultima letras de un string son la misma (sin discriminar mayus/minus)

string = input("Dame un string: ")

print("Las letras son iguales") if string[0].lower() == string[-1].lower() else print("Las letras no son iguales")
