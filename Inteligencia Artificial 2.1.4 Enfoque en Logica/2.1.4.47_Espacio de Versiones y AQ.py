# Definimos un conjunto de datos de ejemplo
# Cada ejemplo tiene características (atributos) y una clase (positivo o negativo)
data = [
    {'color': 'rojo', 'forma': 'redondo', 'clase': 'positivo'},
    {'color': 'rojo', 'forma': 'cuadrado', 'clase': 'negativo'},
    {'color': 'verde', 'forma': 'redondo', 'clase': 'positivo'},
    {'color': 'verde', 'forma': 'cuadrado', 'clase': 'positivo'},
    {'color': 'rojo', 'forma': 'redondo', 'clase': 'negativo'},
]

# Inicializamos el espacio de versiones
# En este caso, solo guardamos ejemplos positivos
version_space = []

# Llenamos el espacio de versiones con ejemplos positivos
for ejemplo in data:
    if ejemplo['clase'] == 'positivo':
        version_space.append(ejemplo)

# Mostramos el espacio de versiones
print("Espacio de Versiones:")
for v in version_space:
    print(v)

# Función AQ: encontrar ejemplos que cumplen con las características de los ejemplos positivos
def aq_algorithm(version_space):
    if not version_space:
        return None
    
    # Inicializamos la hipótesis como un diccionario vacío
    hypothesis = {}

    # Obtenemos los atributos del primer ejemplo positivo
    first_example = version_space[0]
    
    # Llenamos la hipótesis con los atributos de los ejemplos positivos
    for key in first_example:
        if key != 'clase':
            # Guardamos la primera característica
            hypothesis[key] = first_example[key]

    return hypothesis

# Ejecutamos el algoritmo AQ
hipotesis = aq_algorithm(version_space)

# Mostramos la mejor hipótesis encontrada
print("Mejor Hipótesis Encontrada:")
print(hipotesis)
