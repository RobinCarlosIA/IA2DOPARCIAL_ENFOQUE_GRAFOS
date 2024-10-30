def salto_atras_conflictos(nombres, colores):
    """Intenta asignar colores a los nombres y retrocede si hay un conflicto."""
    
    # Creamos un diccionario para guardar los colores asignados a cada nombre.
    asignacion = {nombre: None for nombre in nombres}

    def es_valido(nombre, color):
        """Verifica si se puede asignar un color sin conflictos."""
        for n, c in asignacion.items():
            if n != nombre and c == color:  # Si otro nombre ya tiene el color, hay conflicto.
                return False
        return True  # Si no hay conflictos, es válido.

    def asignar_colores(i):
        """Asigna colores y retrocede si hay un conflicto."""
        
        # Si ya hemos asignado colores a todos los nombres.
        if i == len(nombres):
            print("Asignación completa y válida:", asignacion)
            return True
        
        nombre_actual = nombres[i]  # Nombre actual al que le vamos a asignar color.
        for color in colores:
            # Verificamos si es válido asignar este color al nombre actual.
            if es_valido(nombre_actual, color):
                asignacion[nombre_actual] = color  # Asignamos el color.
                print(f"Asignando {color} a {nombre_actual}")

                # Intentamos asignar colores al siguiente nombre.
                if asignar_colores(i + 1):
                    return True  # Si se encuentra solución, regresamos True.

                # Si no hay solución, retrocedemos (quitamos el color asignado).
                print(f"Retrocediendo, quitando asignación de {nombre_actual}")
                asignacion[nombre_actual] = None
        
        return False  # Si no se encuentra solución, regresamos False.

# Nombres y colores
nombres = ["Fernanda", "Emmanuel", "Carlos"]
colores = ["Rojo", "Verde", "Azul"]

# Ejecutar el algoritmo de salto atrás dirigido por conflictos
if not salto_atras_conflictos(nombres, colores):
    print("No se encontró una asignación válida.")
