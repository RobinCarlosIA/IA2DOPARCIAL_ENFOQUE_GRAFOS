# Definimos las probabilidades de transición entre estados ocultos (Fernanda, Emmanuel, Emiliano)
transiciones = {
    'Fernanda': {'Fernanda': 0.6, 'Emmanuel': 0.3, 'Emiliano': 0.1},
    'Emmanuel': {'Fernanda': 0.2, 'Emmanuel': 0.5, 'Emiliano': 0.3},
    'Emiliano': {'Fernanda': 0.1, 'Emmanuel': 0.4, 'Emiliano': 0.5}
}

# Definimos las probabilidades de emisión (observaciones: 'si', 'no') para cada estado oculto
emisiones = {
    'Fernanda': {'si': 0.7, 'no': 0.3},
    'Emmanuel': {'si': 0.4, 'no': 0.6},
    'Emiliano': {'si': 0.8, 'no': 0.2}
}

# Probabilidades iniciales para cada estado oculto
iniciales = {'Fernanda': 0.5, 'Emmanuel': 0.3, 'Emiliano': 0.2}

# Secuencia de observaciones (por ejemplo: 'si', 'no', 'si')
observaciones = ['si', 'no', 'si']

# Función para calcular la probabilidad de una secuencia de observaciones usando el algoritmo hacia adelante
def algoritmo_hacia_adelante(transiciones, emisiones, iniciales, observaciones):
    # Paso inicial (t = 0), calculamos las probabilidades iniciales basadas en la primera observación
    probabilidades = {estado: iniciales[estado] * emisiones[estado][observaciones[0]] for estado in iniciales}

    # Para cada observación en la secuencia (t = 1, 2, ...)
    for observacion in observaciones[1:]:
        nuevas_probabilidades = {}
        for estado_actual in transiciones:
            # Calculamos la nueva probabilidad para cada estado
            nuevas_probabilidades[estado_actual] = sum(
                probabilidades[estado_anterior] * transiciones[estado_anterior][estado_actual]
                for estado_anterior in transiciones
            ) * emisiones[estado_actual][observacion]
        
        # Actualizamos las probabilidades para la siguiente iteración
        probabilidades = nuevas_probabilidades

    # Al final, sumamos todas las probabilidades de los estados ocultos
    return sum(probabilidades.values())

# Ejecutamos el algoritmo hacia adelante con los datos definidos
resultado = algoritmo_hacia_adelante(transiciones, emisiones, iniciales, observaciones)

# Mostramos el resultado de la probabilidad de la secuencia de observaciones
print("Probabilidad de la secuencia de observaciones:", resultado)
