# Definimos ejemplos positivos y negativos
# Cada ejemplo es un diccionario que contiene características y su clase (positivo o negativo)
ejemplos_positivos = [
    {'color': 'rojo', 'forma': 'redondo', 'clase': 'positivo'},
    {'color': 'verde', 'forma': 'redondo', 'clase': 'positivo'},
]

ejemplos_negativos = [
    {'color': 'rojo', 'forma': 'cuadrado', 'clase': 'negativo'},
    {'color': 'verde', 'forma': 'cuadrado', 'clase': 'negativo'},
]

# Función para generar una regla basada en los ejemplos positivos
def generar_regla(positivos):
    if not positivos:
        return None
    
    # Inicializamos la regla como un diccionario vacío
    regla = {}

    # Recorremos el primer ejemplo positivo
    ejemplo = positivos[0]
    
    # Agregamos características del primer ejemplo a la regla
    for atributo, valor in ejemplo.items():
        if atributo != 'clase':
            regla[atributo] = valor

    return regla

# Ejecutamos la generación de reglas
regla_encontrada = generar_regla(ejemplos_positivos)

# Mostramos la regla encontrada
print("Regla Encontrada:")
print(regla_encontrada)

# Función para verificar si la regla se cumple
def verificar_regla(regla, ejemplo):
    for atributo, valor in regla.items():
        if ejemplo.get(atributo) != valor:
            return False
    return True

# Verificamos ejemplos positivos y negativos
print("\nVerificación de Ejemplos:")
for ejemplo in ejemplos_positivos:
    print(f"Ejemplo Positivo {ejemplo}: {'Cumple' if verificar_regla(regla_encontrada, ejemplo) else 'No Cumple'}")

for ejemplo in ejemplos_negativos:
    print(f"Ejemplo Negativo {ejemplo}: {'Cumple' if verificar_regla(regla_encontrada, ejemplo) else 'No Cumple'}")
