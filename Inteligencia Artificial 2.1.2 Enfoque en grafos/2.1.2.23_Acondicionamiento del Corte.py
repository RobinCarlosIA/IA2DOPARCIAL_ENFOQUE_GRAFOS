def acondicionamiento_corte(nombres, colores):
    """Intenta asignar colores a los nombres revisando las posibles decisiones y ajustando para obtener la mejor solución."""

    # Inicializamos un diccionario para almacenar la asignación de colores.
    asignacion = {nombre: None for nombre in nombres}
    
    # Función para verificar si una asignación es válida, es decir, no tiene conflictos.
    def es_valido(nombre, color):
        """Revisa si el color asignado a un nombre es válido sin crear conflictos."""
        for n, c in asignacion.items():
            if n != nombre and c == color:  # Si otro nombre tiene el mismo color, hay conflicto.
                return False
        return True

    # Función principal que asigna los colores a los nombres.
    def asignar(i):
        """Asigna colores de forma ajustada para minimizar conflictos."""
        if i == len(nombres):
            return True  # Si hemos asignado colores a todos los nombres, devolvemos True.

        nombre_actual = nombres[i]  # Tomamos el nombre actual.
        for color in colores:
            if es_valido(nombre_actual, color):  # Verificamos si el color es válido.
                asignacion[nombre_actual] = color  # Asignamos el color.
                print(f"Asignando {color} a {nombre_actual}")
                
                # Intentamos asignar colores a los siguientes nombres.
                if asignar(i + 1):
                    return True  # Si encontramos una solución válida, terminamos.

                # Si no es válido, "cortamos" esa decisión (quitamos la asignación).
                print(f"Cortando la decisión para {nombre_actual}, desasignando {color}")
                asignacion[nombre_actual] = None
        
        return False  # Si no encontramos solución, regresamos False.

    # Llamar a la función para comenzar el proceso
    if asignar(0):
        print("Asignación válida encontrada:", asignacion)
    else:
        print("No se encontró una asignación válida.")

# Nombres y colores
nombres = ["Fernanda", "Emmanuel", "Carlos"]
colores = ["Rojo", "Verde", "Azul"]

# Ejecutar el algoritmo de Acondicionamiento del Corte
acondicionamiento_corte(nombres, colores)
