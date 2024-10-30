# Definimos una función de orden superior que aplica una función a cada elemento de una lista
def aplicar_funcion(lista, funcion):
    resultado = []  # Lista para almacenar los resultados
    for elemento in lista:
        resultado.append(funcion(elemento))  # Aplicamos la función a cada elemento
    return resultado

# Definimos algunas funciones simples
def cuadrado(x):
    return x ** 2  # Devuelve el cuadrado del número

def cubo(x):
    return x ** 3  # Devuelve el cubo del número

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]  # Lista de números

# Aplicamos la función cuadrado a la lista de números
resultado_cuadrado = aplicar_funcion(numeros, cuadrado)
print("Resultados del cuadrado:", resultado_cuadrado)

# Aplicamos la función cubo a la lista de números
resultado_cubo = aplicar_funcion(numeros, cubo)
print("Resultados del cubo:", resultado_cubo)
