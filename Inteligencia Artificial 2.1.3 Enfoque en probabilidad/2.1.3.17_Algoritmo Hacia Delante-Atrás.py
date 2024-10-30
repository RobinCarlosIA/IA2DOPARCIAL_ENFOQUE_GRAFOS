# Definimos las probabilidades de transición entre personas
transiciones = {
    'Fernanda': {'Fernanda': 0.7, 'Emmanuel': 0.2, 'Emiliano': 0.1},
    'Emmanuel': {'Fernanda': 0.3, 'Emmanuel': 0.4, 'Emiliano': 0.3},
    'Emiliano': {'Fernanda': 0.1, 'Emmanuel': 0.3, 'Emiliano': 0.6}
}

# Definimos las probabilidades de observación para cada persona
observaciones = {
    'Fernanda': {'si': 0.6, 'no': 0.4},
    'Emmanuel': {'si': 0.5, 'no': 0.5},
    'Emiliano': {'si': 0.8, 'no': 0.2}
}

# Probabilidades iniciales para cada persona
probabilidades = {'Fernanda': 0.3, 'Emmanuel': 0.4, 'Emiliano': 0.3}

# Observaciones de ejemplo ('si' o 'no')
observaciones_secuencia = ['si', 'no']

# Algoritmo hacia adelante simple
for obs in observaciones_secuencia:
    nuevas_probabilidades = {}
    for persona in probabilidades:
        nuevas_probabilidades[persona] = sum(probabilidades[otra] * transiciones[otra][persona] for otra in probabilidades)
        nuevas_probabilidades[persona] *= observaciones[persona][obs]

    # Normalizamos las probabilidades
    total = sum(nuevas_probabilidades.values())
    probabilidades = {persona: prob / total for persona, prob in nuevas_probabilidades.items()}

# Mostramos el resultado final
print("Probabilidades finales:", probabilidades)
