lista_numeros = [5, 8, -2, 3, 1, -7, 10]

def numeros_enteros(lista_numeros):
    
    positivos = [n for n in lista_numeros if n>=0]
    numeros_repetidos = list(set(positivos))
    resultado = sorted(numeros_repetidos)

    return resultado

# print(lista_numeros)

print(numeros_enteros(lista_numeros))

# NOTAS:

# list(): crea una lista. En este ejercicio, convierte el conjunto creado por set() en una lista.
# sorted(): devuelve una nueva lista con los elementos ordenados. Por defecto, los ordena de menor a mayor.