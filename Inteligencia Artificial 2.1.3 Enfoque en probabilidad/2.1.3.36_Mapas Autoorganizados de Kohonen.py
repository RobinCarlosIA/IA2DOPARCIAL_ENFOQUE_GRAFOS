import numpy as np
import matplotlib.pyplot as plt

# Parámetros del SOM
num_filas, num_columnas = 10, 10  # Dimensiones del mapa SOM
num_iteraciones = 1000            # Número de iteraciones de entrenamiento
tasa_aprendizaje_inicial = 0.1     # Tasa de aprendizaje inicial

# Inicialización del SOM con pesos aleatorios
som = np.random.rand(num_filas, num_columnas, 2)

# Datos de entrada, puntos aleatorios en 2D
datos = np.random.rand(100, 2)

# Función para calcular la distancia Euclidiana
def distancia_euclidiana(punto1, punto2):
    return np.linalg.norm(punto1 - punto2)

# Entrenamiento del SOM
for t in range(num_iteraciones):
    # Seleccionar un punto aleatorio de los datos
    punto = datos[np.random.randint(0, len(datos))]

    # Encontrar la neurona ganadora (BMU) - la más cercana al punto
    distancias = np.array([[distancia_euclidiana(punto, som[x, y]) for y in range(num_columnas)] for x in range(num_filas)])
    ganadora = np.unravel_index(np.argmin(distancias), (num_filas, num_columnas))

    # Calcular la tasa de aprendizaje y el radio de vecindad
    tasa_aprendizaje = tasa_aprendizaje_inicial * (1 - t / num_iteraciones)
    radio_vecindad = max(num_filas, num_columnas) / 2 * (1 - t / num_iteraciones)

    # Actualizar los pesos de las neuronas vecinas
    for i in range(num_filas):
        for j in range(num_columnas):
            distancia_a_ganadora = distancia_euclidiana(np.array([i, j]), np.array(ganadora))
            if distancia_a_ganadora <= radio_vecindad:
                influencia = np.exp(-(distancia_a_ganadora**2) / (2 * (radio_vecindad**2)))
                som[i, j] += influencia * tasa_aprendizaje * (punto - som[i, j])

# Visualizar el SOM y los datos
plt.imshow(np.linalg.norm(som, axis=2), cmap='gray')
plt.scatter(datos[:, 0] * (num_columnas - 1), datos[:, 1] * (num_filas - 1), color='red', label='Datos')
plt.title("Mapa Autoorganizado de Kohonen")
plt.legend()
plt.show()
