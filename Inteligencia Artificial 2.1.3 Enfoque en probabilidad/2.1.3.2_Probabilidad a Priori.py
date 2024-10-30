# Definimos una clase para manejar las probabilidades a priori.
class ProbabilidadAPriori:
    def __init__(self):
        # Inicializamos un diccionario para almacenar las probabilidades a priori de cada persona.
        self.probabilidades = {}

    def agregar_probabilidad(self, nombre, probabilidad):
        """Método para agregar la probabilidad a priori de una persona."""
        self.probabilidades[nombre] = probabilidad  # Almacenamos la probabilidad de la persona.

    def mostrar_probabilidades(self):
        """Método para mostrar las probabilidades a priori de cada persona."""
        print("Probabilidades a Priori:")
        for nombre, probabilidad in self.probabilidades.items():
            print(f"{nombre}: {probabilidad:.2f}")  # Mostramos la probabilidad con dos decimales.

# Creamos una instancia de ProbabilidadAPriori.
probabilidades_a_priori = ProbabilidadAPriori()

# Agregamos probabilidades a priori para cada persona.
probabilidades_a_priori.agregar_probabilidad('Fernanda', 0.3)  # 30% de probabilidad.
probabilidades_a_priori.agregar_probabilidad('Emmanuel', 0.5)  # 50% de probabilidad.
probabilidades_a_priori.agregar_probabilidad('Emiliano', 0.2)  # 20% de probabilidad.

# Mostramos las probabilidades a priori de cada persona.
probabilidades_a_priori.mostrar_probabilidades()  # Llamamos al método para mostrar las probabilidades.
