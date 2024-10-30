def propagacion_restricciones(nombres, colores):
    """Función para asignar colores a los nombres sin conflictos."""
    # Crear un diccionario para almacenar la asignación de colores
    asignacion = {nombre: None for nombre in nombres}

    # Función interna para verificar restricciones
    def es_valido(nombre, color):
        """Verifica si se puede asignar un color al nombre."""
        for n, c in asignacion.items():
            # Si el nombre ya tiene un color y es el mismo que el que se quiere asignar
            if n != nombre and c == color:
                return False  # No es válido, hay conflicto
        return True  # Es válido

    # Función para intentar asignar colores
    def asignar_colores(i):
        """Intenta asignar colores a los nombres."""
        # Si hemos asignado colores a todos los nombres
        if i == len(nombres):
            print("Asignación válida encontrada:", asignacion)
            return True
        
        nombre_actual = nombres[i]  # Obtener el nombre actual
        # Probar cada color
        for color in colores:
            # Verificar si la asignación es válida
            if es_valido(nombre_actual, color):
                asignacion[nombre_actual] = color  # Asignar el color
                print(f"Asignando {color} a {nombre_actual}")

                # Llamar recursivamente para el siguiente nombre
                if asignar_colores(i + 1):
                    return True  # Si se encontró solución, regresar True

                # Retroceder si no se encontró solución
                print(f"Retrocediendo, quitando asignación de {nombre_actual}")
                asignacion[nombre_actual] = None
        
        return False  # Si no se encontró solución

    # Iniciar la asignación de colores
    if not asignar_colores(0):
        print("No se encontró una asignación válida.")

# Nombres y colores
nombres = ["Fernanda", "Emmanuel", "Carlos"]
colores = ["Rojo", "Verde", "Azul"]

# Ejecutar la propagación de restricciones
propagacion_restricciones(nombres, colores)
