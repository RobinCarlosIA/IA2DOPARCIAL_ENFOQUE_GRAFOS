import random

# Definimos los posibles estados y observaciones
estados = ['Soleado', 'Lluvioso']
observaciones = ['Paraguas', 'No Paraguas']

# Probabilidad de transición entre estados
# P(clima_actual | clima_anterior)
transiciones = {
    'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# Probabilidad de observación según el estado oculto
# P(observacion | clima)
emisiones = {
    'Soleado': {'Paraguas': 0.1, 'No Paraguas': 0.9},
    'Lluvioso': {'Paraguas': 0.9, 'No Paraguas': 0.1}
}

# Función para obtener el siguiente estado basado en probabilidades de transición
def siguiente_estado(estado_actual):
    probabilidades = transiciones[estado_actual]
    return random.choices(estados, weights=[probabilidades['Soleado'], probabilidades['Lluvioso']])[0]

# Función para generar la observación basada en el estado actual
def observar_estado(estado_actual):
    probabilidades = emisiones[estado_actual]
    return random.choices(observaciones, weights=[probabilidades['Paraguas'], probabilidades['No Paraguas']])[0]

# Simulación del HMM
def simular_hmm(estado_inicial, pasos):
    estado_actual = estado_inicial
    historial = []

    # Simular varios pasos
    for _ in range(pasos):
        observacion = observar_estado(estado_actual)  # Obtenemos la observación
        historial.append((estado_actual, observacion))  # Guardamos el estado y observación
        estado_actual = siguiente_estado(estado_actual)  # Actualizamos el estado para el siguiente paso
    
    return historial

# Ejecutamos la simulación
historial = simular_hmm('Soleado', 5)  # Empezamos con "Soleado" y simulamos 5 días

# Mostramos el historial de estados y observaciones
for dia, (estado, observacion) in enumerate(historial, 1):
    print(f"Día {dia}: Estado = {estado}, Observación = {observacion}")
