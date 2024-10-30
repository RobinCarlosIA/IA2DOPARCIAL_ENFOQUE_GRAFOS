# Importamos la librería necesaria para manejar probabilidades
from collections import defaultdict

# Definimos la clase para la Red Bayesiana
class RedBayesiana:
    def __init__(self):
        # Usamos un diccionario para almacenar las probabilidades condicionales
        self.probabilidades = defaultdict(dict)
    
    # Método para agregar las probabilidades condicionales a la red
    def agregar_probabilidad(self, evento, dado_evento, probabilidad):
        """
        Agrega P(evento | dado_evento) a la red bayesiana.
        """
        self.probabilidades[evento][dado_evento] = probabilidad

    # Método para calcular la probabilidad total usando la probabilidad condicional
    def calcular_probabilidad(self, evento, dado_evento):
        """
        Calcula P(evento | dado_evento) si la tenemos en la red.
        """
        if dado_evento in self.probabilidades[evento]:
            return self.probabilidades[evento][dado_evento]
        else:
            return "Probabilidad no definida en la red."

# Creamos una instancia de la Red Bayesiana
red = RedBayesiana()

# Agregamos probabilidades a la red. 
# P(Emmanuel | Fernanda): La probabilidad de que ocurra Emmanuel dado que ocurre Fernanda.
red.agregar_probabilidad('Emmanuel', 'Fernanda', 0.7)

# P(Emiliano | Fernanda): La probabilidad de que ocurra Emiliano dado que ocurre Fernanda.
red.agregar_probabilidad('Emiliano', 'Fernanda', 0.6)

# P(Fernanda | Emiliano): La probabilidad de que ocurra Fernanda dado que ocurre Emiliano.
red.agregar_probabilidad('Fernanda', 'Emiliano', 0.8)

# Calculamos las probabilidades usando la red
# Queremos calcular la probabilidad de 'Emmanuel' dado que ocurrió 'Fernanda'
prob_emmanuel_dado_fernanda = red.calcular_probabilidad('Emmanuel', 'Fernanda')

# Queremos calcular la probabilidad de 'Emiliano' dado que ocurrió 'Fernanda'
prob_emiliano_dado_fernanda = red.calcular_probabilidad('Emiliano', 'Fernanda')

# Mostramos los resultados
print(f"La probabilidad de que ocurra 'Emmanuel' dado que ocurrió 'Fernanda' es: {prob_emmanuel_dado_fernanda}")
print(f"La probabilidad de que ocurra 'Emiliano' dado que ocurrió 'Fernanda' es: {prob_emiliano_dado_fernanda}")
