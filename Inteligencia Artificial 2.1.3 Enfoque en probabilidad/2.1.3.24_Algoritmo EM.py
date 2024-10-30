import numpy as np

# Definimos la clase para el Algoritmo EM
class AlgoritmoEM:
    def __init__(self, datos, num_clusters):
        self.datos = datos  # Conjunto de datos
        self.num_clusters = num_clusters  # Número de clusters que queremos encontrar
        self.probabilidades = np.zeros((len(datos), num_clusters))  # Inicializamos las probabilidades para cada cluster
        self.medias = np.random.choice(datos, num_clusters)  # Inicializamos las medias aleatoriamente
        self.varianzas = np.ones(num_clusters)  # Inicializamos las varianzas
        self.pesos = np.ones(num_clusters) / num_clusters  # Inicializamos los pesos de cada cluster
    
    # Paso de Expectación: calculamos las probabilidades de que los puntos pertenezcan a cada cluster
    def expectacion(self):
        for i, x in enumerate(self.datos):
            for k in range(self.num_clusters):
                prob = self.pesos[k] * self._gaussiana(x, self.medias[k], self.varianzas[k])
                self.probabilidades[i, k] = prob
            self.probabilidades[i, :] /= np.sum(self.probabilidades[i, :])  # Normalizamos
    
    # Paso de Maximización: actualizamos las medias, varianzas y pesos
    def maximizacion(self):
        for k in range(self.num_clusters):
            # Calculamos la suma de las probabilidades para cada cluster
            suma_prob = np.sum(self.probabilidades[:, k])
            # Actualizamos la media del cluster
            self.medias[k] = np.sum(self.probabilidades[:, k] * self.datos) / suma_prob
            # Actualizamos la varianza del cluster
            self.varianzas[k] = np.sum(self.probabilidades[:, k] * (self.datos - self.medias[k])**2) / suma_prob
            # Actualizamos el peso del cluster
            self.pesos[k] = suma_prob / len(self.datos)
    
    # Método para ejecutar el algoritmo EM
    def entrenar(self, iteraciones):
        for i in range(iteraciones):
            self.expectacion()  # Paso E
            self.maximizacion()  # Paso M
            print(f"Iteración {i+1}: medias={self.medias}, varianzas={self.varianzas}, pesos={self.pesos}")

    # Función para calcular la distribución gaussiana
    def _gaussiana(self, x, media, varianza):
        return (1 / np.sqrt(2 * np.pi * varianza)) * np.exp(-(x - media)**2 / (2 * varianza))

# Ejemplo de uso
# Creamos un conjunto de datos sencillo
datos = np.array([1.0, 2.0, 2.5, 3.0, 4.5, 5.0, 6.0, 7.0, 8.0])

# Creamos una instancia del Algoritmo EM con 2 clusters
em = AlgoritmoEM(datos, 2)

# Entrenamos el modelo con 10 iteraciones
em.entrenar(10)
