def buscar_asignacion(assignment, nombres, colores):
    """Función para buscar una asignación de colores usando vuelta atrás."""
    
    # Si ya se asignaron colores a todos los nombres
    if len(assignment) == len(nombres):
        print("Asignación válida encontrada:", assignment)
        return True
    
    # Seleccionar el siguiente nombre para asignar
    nombre_actual = nombres[len(assignment)]
    
    # Probar cada color disponible
    for color in colores:
        # Asignar color al nombre actual
        assignment[nombre_actual] = color
        print(f"Probando asignar {color} a {nombre_actual}")

        # Verificar si la asignación es válida (sin duplicados)
        if len(set(assignment.values())) == len(assignment.values()):
            # Llamar recursivamente para el siguiente nombre
            if buscar_asignacion(assignment, nombres, colores):
                return True  # Si se encontró una solución, regresar True
        
        # Si no se encontró solución, retroceder
        print(f"Retrocediendo, quitando asignación de {nombre_actual}")
        del assignment[nombre_actual]
    
    return False  # Si no se encontró solución

# Nombres y colores
nombres = ["Fernanda", "Emmanuel", "Carlos"]
colores = ["Rojo", "Verde", "Azul"]

# Diccionario para almacenar las asignaciones
asignacion = {}

# Ejecutar la búsqueda de vuelta atrás
if not buscar_asignacion(asignacion, nombres, colores):
    print("No se encontró una asignación válida.")

