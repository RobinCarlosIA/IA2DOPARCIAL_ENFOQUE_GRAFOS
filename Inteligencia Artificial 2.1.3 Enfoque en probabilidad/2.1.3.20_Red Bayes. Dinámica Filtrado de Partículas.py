import random

# Clase que representa un Filtro de Partículas.
class FiltroDeParticulas:
    def __init__(self, num_particulas):
        # Inicializamos un número dado de partículas en posiciones aleatorias.
        self.particulas = [random.uniform(0, 20) for _ in range(num_particulas)]
        # Lista para almacenar los pesos de las partículas.
        self.pesos = [1.0 / num_particulas] * num_particulas

    def predecir(self, movimiento):
        # Actualizamos la posición de cada partícula con el movimiento dado.
        self.particulas = [p + movimiento + random.gauss(0, 1) for p in self.particulas]

    def actualizar(self, medicion):
        # Actualizamos los pesos de las partículas basados en la medición.
        self.pesos = [self._calcular_peso(p, medicion) for p in self.particulas]

    def _calcular_peso(self, particula, medicion):
        # Calculamos un peso basado en la diferencia entre la partícula y la medición.
        return 1.0 / abs(particula - medicion + 0.01)  # Añadimos 0.01 para evitar división por cero.

    def reamostrar(self):
        # Reamostramos las partículas según los pesos, dándole más importancia a las mejores.
        nueva_lista = random.choices(self.particulas, weights=self.pesos, k=len(self.particulas))
        self.particulas = nueva_lista

    def estimar(self):
        # Estimamos la posición promedio de las partículas como el resultado final.
        return sum(self.particulas) / len(self.particulas)

# Usamos valores iniciales con nombres conocidos.
num_particulas = 100  # Vamos a usar 100 partículas.

# Inicializamos el filtro de partículas.
filtro = FiltroDeParticulas(num_particulas)

# Simulamos un movimiento de Fernanda y actualizamos las partículas.
filtro.predecir(2)  # Fernanda se mueve 2 unidades.

# Supongamos que medimos la posición de Fernanda y obtenemos 15.
filtro.actualizar(15)

# Reamostramos las partículas según la medición.
filtro.reamostrar()

# Estimamos la posición de Fernanda con las partículas.
estimacion = filtro.estimar()
print("Estimación de la posición de Fernanda:", estimacion)
