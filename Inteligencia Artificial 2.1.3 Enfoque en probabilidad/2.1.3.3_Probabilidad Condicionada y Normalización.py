# Definimos una clase para manejar la probabilidad condicionada y normalización.
class ProbabilidadCondicionada:
    def __init__(self):
        # Inicializamos un diccionario para almacenar las probabilidades de eventos.
        self.probabilidades = {}

    def agregar_probabilidad(self, nombre, probabilidad):
        """Método para agregar la probabilidad de un evento para una persona."""
        self.probabilidades[nombre] = probabilidad  # Almacenamos la probabilidad.

    def probabilidad_condicionada(self, nombre, condicion):
        """Método para calcular la probabilidad condicionada de un evento."""
        # Supongamos que la probabilidad condicionada es la probabilidad dada una condición.
        # Aquí la condición es simplemente un número que afecta la probabilidad.
        probabilidad = self.probabilidades.get(nombre, 0)
        return probabilidad * condicion  # Retornamos la probabilidad condicionada.

    def normalizar_probabilidades(self):
        """Método para normalizar las probabilidades de todos los eventos."""
        total = sum(self.probabilidades.values())  # Sumamos todas las probabilidades.
        if total == 0:  # Si la suma es cero, no podemos normalizar.
            return

        # Normalizamos cada probabilidad.
        for nombre in self.probabilidades:
            self.probabilidades[nombre] /= total  # Dividimos cada probabilidad por el total.

    def mostrar_probabilidades(self):
        """Método para mostrar las probabilidades de cada persona."""
        print("Probabilidades:")
        for nombre, probabilidad in self.probabilidades.items():
            print(f"{nombre}: {probabilidad:.2f}")  # Mostramos la probabilidad con dos decimales.

# Creamos una instancia de ProbabilidadCondicionada.
probabilidades = ProbabilidadCondicionada()

# Agregamos probabilidades para cada persona.
probabilidades.agregar_probabilidad('Fernanda', 0.3)  # Probabilidad de 30%.
probabilidades.agregar_probabilidad('Emmanuel', 0.5)  # Probabilidad de 50%.
probabilidades.agregar_probabilidad('Emiliano', 0.2)  # Probabilidad de 20%.

# Mostramos las probabilidades antes de normalizar.
print("Antes de normalizar:")
probabilidades.mostrar_probabilidades()  # Mostramos las probabilidades iniciales.

# Normalizamos las probabilidades.
probabilidades.normalizar_probabilidades()

# Mostramos las probabilidades después de normalizar.
print("\nDespués de normalizar:")
probabilidades.mostrar_probabilidades()  # Mostramos las probabilidades normalizadas.

# Calculamos la probabilidad condicionada de Emmanuel dado que la condición es 0.8.
condicion = 0.8  # Por ejemplo, una condición que afecta la probabilidad.
probabilidad_emmanuel_condicionada = probabilidades.probabilidad_condicionada('Emmanuel', condicion)
print(f"\nProbabilidad condicionada de Emmanuel: {probabilidad_emmanuel_condicionada:.2f}")
