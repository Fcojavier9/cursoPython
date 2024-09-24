traduccion = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C"
}

# FUNCION
def conversion(secuencia : str) -> str:
    resultado = ""
    for base_nitrogenada in secuencia:
        resultado += traduccion[base_nitrogenada.upper()]
    return resultado

hebra = "AtaGATCAtAggCATAACCA"
arn = conversion(hebra)

# HECHO CON FUNCION LAMBDA
                    # Parámetro de entrada : valor de retorno
conversionLambda = lambda base_nitrogenada : traduccion[base_nitrogenada]
arnLambda = ""
for base_nitrogenada in hebra:
    arnLambda += conversionLambda(base_nitrogenada.upper())

# IMPRIMIR RESULTADOS
print(f"Hebra Bases Nitrogenadas {hebra}")
print(f"Con funcion {arn}")
print(f"Con lambda {arnLambda}")