import random

# Definimos una clase para el cálculo de la ponderación de verosimilitud
class PonderacionVerosimilitud:
    def __init__(self):
        # Definimos las probabilidades iniciales de cada persona
        self.probabilidades = {
            'Fernanda': 0.5,  # Probabilidad de Fernanda
            'Emmanuel': 0.3,  # Probabilidad de Emmanuel
            'Emiliano': 0.2   # Probabilidad de Emiliano
        }

    def ponderacion(self, evidencia):
        """
        Método para calcular la ponderación de verosimilitud según una evidencia.
        """
        # Iniciamos el peso total en 1 (neutral)
        peso_total = 1.0

        # Iteramos por cada persona y su probabilidad
        for persona, probabilidad in self.probabilidades.items():
            # Si la persona está en la evidencia (ejemplo: Fernanda está presente en la evidencia)
            if persona in evidencia:
                peso_total *= probabilidad  # Multiplicamos la probabilidad de esa persona

        return peso_total  # Retornamos el peso total ponderado

# Ejemplo de uso:
ponderacion = PonderacionVerosimilitud()  # Creamos una instancia de la clase

# Definimos una evidencia, donde sabemos que 'Fernanda' y 'Emmanuel' están involucrados
evidencia = ['Fernanda', 'Emmanuel']

# Calculamos la ponderación de verosimilitud basada en la evidencia
peso = ponderacion.ponderacion(evidencia)

# Mostramos el resultado
print("Ponderación de Verosimilitud con la evidencia", evidencia, ": ", peso)
