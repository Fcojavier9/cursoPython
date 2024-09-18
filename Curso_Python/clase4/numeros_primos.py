# 1- Guardando numeros primos en una lista
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

primos = []
inicio = int(input("Dame un numero de inicio: "))
final = int(input("Dame un numero final: "))

for num in range(inicio, final + 1):
    if es_primo(num):
        primos.append(num)

print(primos)