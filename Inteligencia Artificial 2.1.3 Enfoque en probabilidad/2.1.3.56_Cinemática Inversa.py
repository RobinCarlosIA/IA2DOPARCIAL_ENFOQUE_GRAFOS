import math

# Definimos una función para la cinemática inversa
def calcular_angulo_brazo(x, y, longitud_brazo):
    # Calculamos el ángulo necesario para alcanzar (x, y)
    if x == 0 and y == 0:
        return 0  # Si estamos en el origen, el ángulo es cero
    angulo = math.atan2(y, x)  # Calculamos el ángulo en radianes
    return math.degrees(angulo)  # Convertimos a grados

# Creamos las posiciones deseadas para Fernanda, Eliott y Emiliano
posicion_fernanda = (4, 3)
posicion_eliott = (2, 5)
posicion_emiliano = (3, -3)
longitud_brazo = 5  # Longitud del brazo robótico

# Calculamos el ángulo para cada robot
angulo_fernanda = calcular_angulo_brazo(posicion_fernanda[0], posicion_fernanda[1], longitud_brazo)
angulo_eliott = calcular_angulo_brazo(posicion_eliott[0], posicion_eliott[1], longitud_brazo)
angulo_emiliano = calcular_angulo_brazo(posicion_emiliano[0], posicion_emiliano[1], longitud_brazo)

# Imprimimos los ángulos calculados para cada robot
print(f"Ángulo de Fernanda para alcanzar la posición {posicion_fernanda}: {angulo_fernanda:.2f}°")
print(f"Ángulo de Eliott para alcanzar la posición {posicion_eliott}: {angulo_eliott:.2f}°")
print(f"Ángulo de Emiliano para alcanzar la posición {posicion_emiliano}: {angulo_emiliano:.2f}°")
