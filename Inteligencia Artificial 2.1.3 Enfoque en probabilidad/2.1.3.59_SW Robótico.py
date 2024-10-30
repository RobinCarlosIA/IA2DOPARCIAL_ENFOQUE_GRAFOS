# Definimos las coordenadas de los puntos de interés
punto_inicial = (0, 0)           # Posición inicial del robot
punto_destino = (4, 5)           # Destino al que se quiere llegar

# Información del robot
posicion_actual = punto_inicial   # Posición actual del robot
paso = (1, 1)                     # Movimiento básico del robot en cada paso (en x y en y)

# Bucle para mover el robot hasta el destino
while posicion_actual != punto_destino:
    # Imprimimos la posición actual
    print(f"Posición actual del robot: {posicion_actual}")
    
    # Calculamos el siguiente paso
    nueva_x = min(posicion_actual[0] + paso[0], punto_destino[0])
    nueva_y = min(posicion_actual[1] + paso[1], punto_destino[1])
    
    # Actualizamos la posición
    posicion_actual = (nueva_x, nueva_y)

print("¡El robot ha llegado al destino!")
