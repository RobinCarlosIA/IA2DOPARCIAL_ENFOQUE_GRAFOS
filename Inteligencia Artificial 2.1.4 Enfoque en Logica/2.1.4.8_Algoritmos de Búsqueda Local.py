import random

# Definimos una función simple que queremos maximizar
def funcion_objetivo(x):
    return -(x**2) + 4*x  # Esta función tiene un máximo

# Algoritmo de búsqueda local (Hill Climbing)
def subida_de_colina(inicio, pasos=10, tamaño_paso=0.1):
    mejor_x = inicio
    mejor_valor = funcion_objetivo(mejor_x)

    for _ in range(pasos):
        # Generamos un nuevo punto cercano
        vecino = mejor_x + random.uniform(-tamaño_paso, tamaño_paso)
        valor_vecino = funcion_objetivo(vecino)

        # Si el nuevo punto es mejor, lo actualizamos
        if valor_vecino > mejor_valor:
            mejor_x = vecino
            mejor_valor = valor_vecino
            print(f"Nuevo mejor valor: x = {mejor_x}, valor = {mejor_valor}")

    return mejor_x, mejor_valor

# Ejecutamos el algoritmo
inicio = 0  # Punto de inicio
mejor_x, mejor_valor = subida_de_colina(inicio)
print("Resultado final: x =", mejor_x, "valor máximo =", mejor_valor)

