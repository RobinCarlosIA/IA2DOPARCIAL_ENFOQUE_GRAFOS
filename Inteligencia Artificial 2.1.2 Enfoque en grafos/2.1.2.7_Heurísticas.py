def constant_heuristic(point, goal):
    """Heurística constante que siempre devuelve el mismo valor."""
    return 1  # Siempre retorna 1, independientemente de la posición.

def heuristic_example(start, goal):
    """Ejemplo de cómo se puede usar una heurística constante para decidir el mejor camino."""
    # Usamos la heurística para evaluar el costo desde el punto de inicio al objetivo.
    heuristic_value = constant_heuristic(start, goal)
    print(f"Heurística constante desde {start} a {goal}: {heuristic_value}")
    return heuristic_value

# Definimos un punto de inicio y un objetivo.
start_point = (1, 2)  # Punto de inicio.
goal_point = (4, 6)   # Punto objetivo.

# Usamos la heurística constante para evaluar el costo desde el punto de inicio al objetivo.
heuristic_value = heuristic_example(start_point, goal_point)

# Aquí se podría añadir lógica adicional para tomar decisiones basadas en el valor heurístico.
if heuristic_value < 5:
    print("El camino es prometedor, podemos seguir explorando.")
else:
    print("El camino parece largo, consideremos otras opciones.")
