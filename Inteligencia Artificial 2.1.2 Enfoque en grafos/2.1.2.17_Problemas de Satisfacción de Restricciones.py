def assign_colors(names, colors):
    """Asigna colores a los nombres y verifica restricciones."""
    assignments = {}  # Diccionario para almacenar asignaciones de colores
    
    for i, name in enumerate(names):
        # Asignar un color a cada nombre
        color = colors[i % len(colors)]  # Usar módulo para reciclar colores si hay más nombres que colores
        assignments[name] = color
        print(f"Asignando {color} a {name}")
    
    # Verificar restricciones: cada nombre tiene un color
    print("\nAsignaciones finales:", assignments)

# Nombres y colores disponibles
names = ["Fernanda", "Emmanuel", "Carlos"]
colors = ["Rojo", "Verde", "Azul"]

# Ejecutar la asignación de colores
assign_colors(names, colors)
