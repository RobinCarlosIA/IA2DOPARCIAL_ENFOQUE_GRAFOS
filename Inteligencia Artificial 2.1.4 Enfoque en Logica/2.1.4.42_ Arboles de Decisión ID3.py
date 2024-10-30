# Datos de ejemplo
data = [
    {'Temperatura': 'Frío', 'Humedad': 'Alta', 'Clase': 'No'},
    {'Temperatura': 'Frío', 'Humedad': 'Normal', 'Clase': 'No'},
    {'Temperatura': 'Cálido', 'Humedad': 'Alta', 'Clase': 'Sí'},
    {'Temperatura': 'Cálido', 'Humedad': 'Normal', 'Clase': 'Sí'}
]

# Función para contar valores de un atributo
def contar_valores(data, atributo):
    valores = {}
    for ejemplo in data:
        valor = ejemplo[atributo]
        if valor not in valores:
            valores[valor] = 0
        valores[valor] += 1
    return valores

# Función para calcular entropía
import math
def calcular_entropia(data, atributo):
    valores = contar_valores(data, atributo)
    total = sum(valores.values())
    entropia = 0
    for valor in valores.values():
        probabilidad = valor / total
        entropia -= probabilidad * math.log2(probabilidad) if probabilidad > 0 else 0
    return entropia

# Construir una estructura simple de árbol
def construir_arbol(data, atributos, target):
    clases = [ejemplo[target] for ejemplo in data]
    if clases.count(clases[0]) == len(clases):
        return clases[0]
    
    if not atributos:
        return max(clases, key=clases.count)
    
    mejor_atributo = min(atributos, key=lambda atr: calcular_entropia(data, atr))
    arbol = {mejor_atributo: {}}
    for valor in set(ej[mejor_atributo] for ej in data):
        sub_data = [ej for ej in data if ej[mejor_atributo] == valor]
        arbol[mejor_atributo][valor] = construir_arbol(sub_data, [atr for atr in atributos if atr != mejor_atributo], target)
    
    return arbol

# Construir el árbol usando los datos
atributos = ['Temperatura', 'Humedad']
arbol = construir_arbol(data, atributos, 'Clase')
print("Árbol de decisión:", arbol)

# Ejemplo de predicción usando el árbol generado
def predecir(arbol, ejemplo):
    if not isinstance(arbol, dict):
        return arbol
    atributo = next(iter(arbol))
    valor = ejemplo.get(atributo)
    return predecir(arbol[atributo][valor], ejemplo) if valor in arbol[atributo] else "Desconocido"

# Predicción con un nuevo ejemplo
ejemplo = {'Temperatura': 'Cálido', 'Humedad': 'Alta'}
print("Predicción para el ejemplo:", predecir(arbol, ejemplo))
