import numpy as np
import matplotlib.pyplot as plt

# Generamos dos conjuntos de puntos para dos clases
clase_1 = np.random.randn(50, 2) + np.array([2, 2])  # Clase 1: alrededor de (2, 2)
clase_2 = np.random.randn(50, 2) + np.array([-2, -2])  # Clase 2: alrededor de (-2, -2)

# Graficamos los puntos
plt.scatter(clase_1[:, 0], clase_1[:, 1], color='blue', label='Clase 1')
plt.scatter(clase_2[:, 0], clase_2[:, 1], color='red', label='Clase 2')

# Línea de separación y = x
x_vals = np.linspace(-5, 5, 100)
y_vals = x_vals
plt.plot(x_vals, y_vals, color='green', linestyle='--', label='Límite de Separación')

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Ejemplo de Separabilidad Lineal entre dos Clases")
plt.show()
