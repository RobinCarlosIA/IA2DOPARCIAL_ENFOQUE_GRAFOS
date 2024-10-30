import numpy as np
import matplotlib.pyplot as plt

# Generamos dos conjuntos de puntos para dos clases
# Clase 1: puntos alrededor de (2, 2)
clase_1 = np.random.randn(50, 2) + np.array([2, 2])

# Clase 2: puntos alrededor de (-2, -2)
clase_2 = np.random.randn(50, 2) + np.array([-2, -2])

# Visualizamos los puntos
plt.scatter(clase_1[:, 0], clase_1[:, 1], color='blue', label='Clase 1')
plt.scatter(clase_2[:, 0], clase_2[:, 1], color='red', label='Clase 2')

# Dibujamos una línea que separa las dos clases
# y = x es la línea que se elige aquí para dividir ambas clases
x_vals = np.linspace(-5, 5, 100)  # Rango de x para la línea
y_vals = x_vals  # Esto crea la línea y = x
plt.plot(x_vals, y_vals, color='green', linestyle='--', label='Límite de Separación')

# Añadimos etiquetas y mostramos la leyenda
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Ejemplo de Separabilidad Lineal entre dos Clases")
plt.show()
