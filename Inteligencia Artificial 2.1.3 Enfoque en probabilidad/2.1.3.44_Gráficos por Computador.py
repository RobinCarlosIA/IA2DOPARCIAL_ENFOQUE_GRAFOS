import matplotlib.pyplot as plt

# Nombres de las personas
nombres = ['Fernanda', 'Emmanuel', 'Emiliano', 'Eliott']

# Valores ficticios para cada nombre (pueden ser calificaciones, edades, etc.)
valores = [85, 90, 78, 88]

# Creamos un gráfico de barras
plt.bar(nombres, valores, color='skyblue')

# Añadimos un título al gráfico
plt.title('Gráfico de Barras de Nombres y Valores')

# Añadimos etiquetas a los ejes
plt.xlabel('Nombres')
plt.ylabel('Valores')

# Mostramos el gráfico
plt.show()
