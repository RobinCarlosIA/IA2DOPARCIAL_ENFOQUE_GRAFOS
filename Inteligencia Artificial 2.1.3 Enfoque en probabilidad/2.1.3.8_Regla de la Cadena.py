# Definimos una clase para manejar probabilidades
class ReglaDeLaCadena:
    def __init__(self):
        # Usamos un diccionario para almacenar las probabilidades
        self.probabilidades = {}

    # Método para agregar probabilidades condicionales
    def agregar_probabilidad(self, evento, probabilidad):
        """
        Agrega una probabilidad para un evento.
        """
        self.probabilidades[evento] = probabilidad

    # Método para calcular la probabilidad conjunta usando la regla de la cadena
    def calcular_probabilidad_conjunta(self, eventos):
        """
        Calcula la probabilidad conjunta de una lista de eventos usando la regla de la cadena.
        """
        prob_conjunta = 1.0  # Empezamos con la probabilidad conjunta inicial en 1
        for evento in eventos:
            if evento in self.probabilidades:
                prob_conjunta *= self.probabilidades[evento]  # Multiplicamos por la probabilidad de cada evento
            else:
                print(f"No se encontró la probabilidad de {evento}")
                return 0
        return prob_conjunta

# Creamos una instancia de la regla de la cadena
regla = ReglaDeLaCadena()

# Agregamos las probabilidades de los eventos
# Probabilidades individuales (pueden ser marginales o condicionales, según el caso)
regla.agregar_probabilidad('Fernanda', 0.5)  # Probabilidad de que ocurra Fernanda
regla.agregar_probabilidad('Emmanuel', 0.6)  # Probabilidad de que ocurra Emmanuel dado algo
regla.agregar_probabilidad('Emiliano', 0.7)  # Probabilidad de que ocurra Emiliano dado algo

# Calculamos la probabilidad conjunta de que ocurran Fernanda, Emmanuel y Emiliano
prob_conjunta = regla.calcular_probabilidad_conjunta(['Fernanda', 'Emmanuel', 'Emiliano'])

# Mostramos el resultado
print(f"La probabilidad conjunta de que ocurra 'Fernanda', 'Emmanuel' y 'Emiliano' es: {prob_conjunta}")
