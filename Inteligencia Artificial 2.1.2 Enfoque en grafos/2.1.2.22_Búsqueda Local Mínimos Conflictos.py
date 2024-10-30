import random

def minimos_conflictos(nombres, colores, max_intentos=1000):
    """Asignar colores a los nombres tratando de minimizar los conflictos."""
    
    # Se empieza asignando un color aleatorio a cada nombre.
    asignacion = {nombre: random.choice(colores) for nombre in nombres}
    
    # Esta función cuenta los conflictos de un nombre comparado con los demás.
    def contar_conflictos(nombre):
        """Cuenta cuántos nombres tienen el mismo color (conflictos)."""
        conflictos = 0
        for n in nombres:
            if n != nombre and asignacion[n] == asignacion[nombre]:
                conflictos += 1  # Si otro nombre tiene el mismo color, es un conflicto.
        return conflictos

    # Intentar solucionar el problema en un número limitado de intentos.
    for intento in range(max_intentos):
        # Verificar si ya no hay conflictos.
        conflictos_totales = sum(contar_conflictos(nombre) for nombre in nombres)
        if conflictos_totales == 0:
            print("Solución sin conflictos encontrada:", asignacion)
            return asignacion

        # Elegir un nombre al azar que tenga conflictos.
        nombre_con_conflicto = random.choice([nombre for nombre in nombres if contar_conflictos(nombre) > 0])

        # Elegir el color que genera menos conflictos para ese nombre.
        mejor_color = asignacion[nombre_con_conflicto]
        min_conflictos = contar_conflictos(nombre_con_conflicto)
        for color in colores:
            asignacion[nombre_con_conflicto] = color
            nuevos_conflictos = contar_conflictos(nombre_con_conflicto)
            if nuevos_conflictos < min_conflictos:
                mejor_color = color
                min_conflictos = nuevos_conflictos

        # Asignar el mejor color encontrado.
        asignacion[nombre_con_conflicto] = mejor_color
        print(f"En el intento {intento}, {nombre_con_conflicto} cambia a {mejor_color} para reducir conflictos.")

    print("No se encontró una solución sin conflictos.")
    return None

# Nombres y colores
nombres = ["Fernanda", "Emmanuel", "Carlos"]
colores = ["Rojo", "Verde", "Azul"]

# Ejecutar el algoritmo de mínimos conflictos
minimos_conflictos(nombres, colores)

