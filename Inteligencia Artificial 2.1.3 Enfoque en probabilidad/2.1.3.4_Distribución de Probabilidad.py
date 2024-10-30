# Definimos una clase para manejar la distribución de probabilidad.
class DistribucionProbabilidad:
    def __init__(self):
        # Inicializamos un diccionario para almacenar las probabilidades de cada persona.
        self.probabilidades = {}

    def agregar_probabilidad(self, nombre, probabilidad):
        """Método para agregar la probabilidad de un evento para una persona."""
        self.probabilidades[nombre] = probabilidad  # Almacenamos la probabilidad.

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
        print("Distribución de Probabilidades:")
        for nombre, probabilidad in self.probabilidades.items():
            print(f"{nombre}: {probabilidad:.2f}")  # Mostramos la probabilidad con dos decimales.

# Creamos una instancia de DistribucionProbabilidad.
distribucion = DistribucionProbabilidad()

# Agregamos probabilidades para cada persona.
distribucion.agregar_probabilidad('Fernanda', 0.4)  # Probabilidad de 40%.
distribucion.agregar_probabilidad('Emmanuel', 0.4)  # Probabilidad de 40%.
distribucion.agregar_probabilidad('Emiliano', 0.2)  # Probabilidad de 20%.

# Mostramos las probabilidades antes de normalizar.
print("Antes de normalizar:")
distribucion.mostrar_probabilidades()  # Mostramos las probabilidades iniciales.

# Normalizamos las probabilidades.
distribucion.normalizar_probabilidades()

# Mostramos las probabilidades después de normalizar.
print("\nDespués de normalizar:")
distribucion.mostrar_probabilidades()  # Mostramos las probabilidades normalizadas.
