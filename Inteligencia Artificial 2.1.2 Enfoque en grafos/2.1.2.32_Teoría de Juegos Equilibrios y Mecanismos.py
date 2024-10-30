import random

# Definimos las estrategias disponibles
estrategias = ["Cooperar", "No Cooperar"]

# Función que simula la elección de estrategias para cada persona
def simular_juego():
    """Simula el juego y muestra las elecciones de cada persona."""
    elecciones = {}
    
    # Cada persona elige una estrategia aleatoria
    elecciones["Fernanda"] = random.choice(estrategias)
    elecciones["Emmanuel"] = random.choice(estrategias)
    elecciones["Carlos"] = random.choice(estrategias)

    # Mostramos las elecciones
    for nombre, estrategia in elecciones.items():
        print(f"{nombre} eligió: {estrategia}")

    # Evaluamos el equilibrio de Nash
    if all(estrategia == "Cooperar" for estrategia in elecciones.values()):
        print("Equilibrio de Nash: Todos cooperan.")
    elif all(estrategia == "No Cooperar" for estrategia in elecciones.values()):
        print("Equilibrio de Nash: Todos no cooperan.")
    else:
        print("No hay equilibrio de Nash.")

# Ejecutamos la simulación una vez
simular_juego()
