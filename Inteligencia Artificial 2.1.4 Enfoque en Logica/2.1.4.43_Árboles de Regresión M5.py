import numpy as np

# Datos de ejemplo (simulados para un árbol de regresión)
data = [
    {'x': 1, 'y': 2},
    {'x': 2, 'y': 4},
    {'x': 3, 'y': 6},
    {'x': 4, 'y': 8},
    {'x': 5, 'y': 10},
    {'x': 6, 'y': 8},
    {'x': 7, 'y': 6}
]

# Función para calcular el error cuadrado medio (para ayudar a decidir divisiones)
def calcular_error(data, target):
    valores = [punto[target] for punto in data]
    media = np.mean(valores)
    error = sum((y - media) ** 2 for y in valores) / len(valores)
    return error

# Función para dividir los datos basados en un valor de umbral
def dividir_datos(data, atributo, valor):
    menor = [punto for punto in data if punto[atributo] <= valor]
    mayor = [punto for punto in data if punto[atributo] > valor]
    return menor, mayor

# Construcción del árbol de regresión
def construir_arbol(data, min_tamaño=2, error_minimo=1.0):
    if len(data) <= min_tamaño:
        return np.mean([punto['y'] for punto in data])  # devolver la media si el grupo es pequeño
    
    mejor_atributo, mejor_valor, mejor_error, mejor_division = None, None, float('inf'), None
    for atributo in ['x']:
        valores = set(punto[atributo] for punto in data)
        for valor in valores:
            menor, mayor = dividir_datos(data, atributo, valor)
            if len(menor) < min_tamaño or len(mayor) < min_tamaño:
                continue
            error_total = calcular_error(menor, 'y') + calcular_error(mayor, 'y')
            if error_total < mejor_error:
                mejor_atributo, mejor_valor, mejor_error, mejor_division = atributo, valor, error_total, (menor, mayor)
    
    if mejor_error > error_minimo:
        return np.mean([punto['y'] for punto in data])
    
    # Recursión para construir ramas del árbol
    menor_arbol = construir_arbol(mejor_division[0], min_tamaño, error_minimo)
    mayor_arbol = construir_arbol(mejor_division[1], min_tamaño, error_minimo)
    
    return {mejor_atributo: {'<= ' + str(mejor_valor): menor_arbol, '> ' + str(mejor_valor): mayor_arbol}}

# Construcción del árbol
arbol = construir_arbol(data)
print("Árbol de regresión:", arbol)

# Predicción utilizando el árbol de regresión
def predecir(arbol, ejemplo):
    if not isinstance(arbol, dict):
        return arbol
    atributo = next(iter(arbol))
    valor, ramas = list(arbol[atributo].items())[0], list(arbol[atributo].values())[0]
    
    if ejemplo[atributo] <= float(valor.split(' ')[1]):
        return predecir(ramas, ejemplo)
    else:
        return predecir(arbol[atributo][list(arbol[atributo].keys())[1]], ejemplo)

# Predicción con un nuevo valor
ejemplo = {'x': 6}
print("Predicción para el ejemplo:", predecir(arbol, ejemplo))
