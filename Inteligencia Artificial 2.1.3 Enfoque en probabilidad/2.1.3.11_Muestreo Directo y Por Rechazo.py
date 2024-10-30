import random

# Definimos una clase para representar el proceso de muestreo
class MuestreoProbabilistico:
    def __init__(self):
        # Guardamos las probabilidades de los eventos (en este caso, los nombres).
        self.probabilidades = {
            'Fernanda': 0.6,  # Probabilidad de Fernanda
            'Emmanuel': 0.3,  # Probabilidad de Emmanuel
            'Emiliano': 0.1   # Probabilidad de Emiliano
        }

    def muestreo_directo(self):
        """
        Realiza el muestreo directo según las probabilidades definidas.
        """
        personas = list(self.probabilidades.keys())  # Obtenemos los nombres de las personas
        probabilidades = list(self.probabilidades.values())  # Obtenemos las probabilidades

        # Seleccionamos una persona al azar basado en las probabilidades
        seleccion = random.choices(personas, probabilidades)[0]
        return seleccion  # Retornamos la persona seleccionada

    def muestreo_por_rechazo(self, condicion):
        """
        Realiza el muestreo por rechazo, donde solo aceptamos el evento si cumple con una condición.
        """
        while True:
            seleccion = self.muestreo_directo()  # Hacemos muestreo directo
            if seleccion == condicion:  # Si la persona seleccionada cumple la condición, aceptamos
                return seleccion  # Retornamos la persona aceptada

# Ejemplo de uso:
muestreo = MuestreoProbabilistico()  # Creamos una instancia del muestreo

# Muestreo directo: Seleccionamos una persona al azar
print("Muestreo Directo: ", muestreo.muestreo_directo())

# Muestreo por rechazo: Solo aceptamos si la persona seleccionada es 'Fernanda'
print("Muestreo por Rechazo (condición: Fernanda): ", muestreo.muestreo_por_rechazo('Fernanda'))
