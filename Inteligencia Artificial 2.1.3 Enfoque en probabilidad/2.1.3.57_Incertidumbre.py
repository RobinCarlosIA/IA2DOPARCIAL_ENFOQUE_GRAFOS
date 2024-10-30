import random

# Definimos la función que simula la medición con incertidumbre
def medicion_con_incertidumbre(valor_real, incertidumbre, iteraciones):
    resultados = []  # Lista para almacenar las mediciones simuladas

    for _ in range(iteraciones):
        # Generamos una medición con incertidumbre aleatoria
        medicion = valor_real + random.uniform(-incertidumbre, incertidumbre)
        resultados.append(medicion)  # Guardamos la medición en la lista

    promedio = sum(resultados) / len(resultados)  # Calculamos el promedio
    return promedio

# Valores iniciales
valor_real = 10.0         # Valor real de la medición
incertidumbre = 0.5       # Incertidumbre (±0.5)
iteraciones = 1000        # Número de simulaciones

# Calculamos el valor promedio con incertidumbre
promedio = medicion_con_incertidumbre(valor_real, incertidumbre, iteraciones)

# Mostramos el resultado
print(f"El valor promedio de la medición considerando la incertidumbre es: {promedio:.2f}")
