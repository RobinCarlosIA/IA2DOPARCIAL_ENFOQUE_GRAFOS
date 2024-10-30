# Importamos la librería math para calcular logaritmos
import math

# Definimos una clase para el aprendizaje bayesiano
class AprendizajeBayesiano:
    
    def __init__(self):
        # Priori inicial: probabilidad de que algo sea verdadero (antes de ver los datos)
        self.priori = 0.5

    # Función para calcular la probabilidad posterior usando la regla de Bayes
    def actualizar_probabilidad(self, evidencia, verosimilitud):
        # Evidencia: probabilidad de observar el dato
        # Verosimilitud: probabilidad de observar el dato dado que la hipótesis es verdadera
        
        # Aplicamos la regla de Bayes para calcular la probabilidad posterior
        posterior = (verosimilitud * self.priori) / evidencia
        return posterior

# Simulamos el proceso de aprendizaje
aprendiz = AprendizajeBayesiano()

# Valores de ejemplo:
# - Probabilidad de la evidencia (e.g., probabilidad de ver un resultado positivo en un test)
evidencia = 0.6

# - Verosimilitud: probabilidad de ver ese resultado dado que la hipótesis es verdadera
verosimilitud = 0.9

# Actualizamos la probabilidad posterior basada en la evidencia y la verosimilitud
probabilidad_posterior = aprendiz.actualizar_probabilidad(evidencia, verosimilitud)

# Mostramos el resultado
print("La probabilidad posterior es:", probabilidad_posterior)
