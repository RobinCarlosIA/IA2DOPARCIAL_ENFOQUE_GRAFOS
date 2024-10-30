# Definimos el objetivo de posición
objetivo_posicion = 100  # La posición que queremos alcanzar
posicion_actual = 0       # Posición inicial del motor
ganancia_control = 0.1    # Ganancia del controlador (ajuste de respuesta)

# Bucle de control para alcanzar el objetivo
while abs(objetivo_posicion - posicion_actual) > 0.1:  # Se detiene al estar cerca del objetivo
    # Calcula el error
    error = objetivo_posicion - posicion_actual
    
    # Aplica el control proporcional
    ajuste = ganancia_control * error
    
    # Actualiza la posición
    posicion_actual += ajuste
    
    # Muestra la posición actual en cada paso
    print(f"Posición actual: {posicion_actual:.2f}")

print("¡Objetivo alcanzado!")
