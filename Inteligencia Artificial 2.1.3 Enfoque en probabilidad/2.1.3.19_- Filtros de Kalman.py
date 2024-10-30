import numpy as np

# Definimos una clase simple para representar el Filtro de Kalman.
class FiltroDeKalman:
    def __init__(self, estimacion_inicial, incertidumbre_inicial):
        # Inicializamos el estado estimado y la incertidumbre inicial
        self.estimacion = estimacion_inicial
        self.incertidumbre = incertidumbre_inicial

    def predecir(self, movimiento, incertidumbre_movimiento):
        # Actualizamos la estimación y la incertidumbre basado en el movimiento
        self.estimacion += movimiento  # Actualizamos la estimación con el movimiento
        self.incertidumbre += incertidumbre_movimiento  # Incrementamos la incertidumbre

    def actualizar(self, medicion, incertidumbre_medicion):
        # Calculamos la ganancia de Kalman para ajustar la estimación
        kalman_gain = self.incertidumbre / (self.incertidumbre + incertidumbre_medicion)
        # Ajustamos la estimación usando la medición y la ganancia de Kalman
        self.estimacion = self.estimacion + kalman_gain * (medicion - self.estimacion)
        # Reducimos la incertidumbre
        self.incertidumbre = (1 - kalman_gain) * self.incertidumbre

# Valores iniciales para Fernanda, Emmanuel y Emiliano
estimacion_inicial = 10  # Supongamos que Fernanda empieza en 10
incertidumbre_inicial = 4  # La incertidumbre inicial es 4

# Creamos un objeto del filtro de Kalman
kalman = FiltroDeKalman(estimacion_inicial, incertidumbre_inicial)

# Simulamos un movimiento de Fernanda y actualizamos el filtro
movimiento = 2  # Fernanda se mueve 2 unidades
incertidumbre_movimiento = 2  # La incertidumbre del movimiento es 2
kalman.predecir(movimiento, incertidumbre_movimiento)

# Simulamos una medición y actualizamos el filtro
medicion = 15  # Medición actual de la posición de Fernanda es 15
incertidumbre_medicion = 3  # Incertidumbre de la medición es 3
kalman.actualizar(medicion, incertidumbre_medicion)

# Mostramos la estimación final de la posición de Fernanda y su incertidumbre
print("Estimación final de la posición de Fernanda:", kalman.estimacion)
print("Incertidumbre final de la estimación:", kalman.incertidumbre)
