def comprobar_hacia_delante(asignacion, nombres, colores):
    """Verifica si se puede asignar colores a los nombres sin conflictos."""
    
    # Comprobar si todos los nombres tienen un color asignado
    if len(asignacion) == len(nombres):
        print("Asignación completa y válida encontrada:", asignacion)
        return True
    
    # Seleccionar el siguiente nombre que necesita un color
    for nombre in nombres:
        if nombre not in asignacion:
            # Probar cada color para este nombre
            for color in colores:
                # Asignar el color al nombre
                asignacion[nombre] = color
                print(f"Probando asignar {color} a {nombre}")

                # Verificar si la asignación es válida
                if len(set(asignacion.values())) == len(asignacion.values()):
                    # Llamar recursivamente para verificar el siguiente nombre
                    if comprobar_hacia_delante(asignacion, nombres, colores):
                        return True  # Si se encontró solución, regresar True

                # Retroceder si no se encontró solución
                print(f"Retrocediendo, quitando asignación de {nombre}")
                del asignacion[nombre]
            break  # Romper el bucle después de probar un nombre

    return False  # Si no se encontró solución

# Nombres y colores
nombres = ["Fernanda", "Emmanuel", "Carlos"]
colores = ["Rojo", "Verde", "Azul"]

# Diccionario para almacenar las asignaciones
asignacion = {}

# Ejecutar la comprobación hacia adelante
if not comprobar_hacia_delante(asignacion, nombres, colores):
    print("No se encontró una asignación válida.")
