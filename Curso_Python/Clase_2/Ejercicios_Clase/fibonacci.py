# 2- Generando numeros de Fibonacci en una lista
def fibonacci(numeros):
    fibonacci = [0, 1]
    for i in range(2, numeros):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci

numeros_fibonacci = int(input("Cuantos numeros de Fibonacci quieres: "))

print(fibonacci(numeros_fibonacci))

