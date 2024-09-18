# 4- Comprobar si un numero entero es palindromo y devolver la suma de sus digitos
def suma_digitos(numero):
    suma = 0
    for digito in numero:
        suma += int(digito)
    return suma

numero = input("Dime un numero: ")

print("El numero es palindromo y la suma es: ", suma_digitos(numero)) if numero == numero[::-1] else print("El numero no es palindromo")
