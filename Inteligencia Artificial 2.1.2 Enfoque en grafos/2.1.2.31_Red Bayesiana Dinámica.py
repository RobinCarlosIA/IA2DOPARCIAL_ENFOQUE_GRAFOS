import random

# Definimos los estados posibles para las personas
estados = ["Feliz", "Triste"]

# Probabilidades de los estados (simplificadas)
probabilidades = {
    "Fernanda": {"Feliz": 0.8, "Triste": 0.2},  # 80% de ser feliz
    "Emmanuel": {"Feliz": 0.5, "Triste": 0.5},  # 50% de ser feliz
    "Carlos": {"Feliz": 0.4, "Triste": 0.6}      # 40% de ser feliz
}

# Función que simula el estado de cada persona basado en probabilidades
def simular_estado():
    """Simula el estado actual de cada persona usando la Red Bayesiana Dinámica."""
    for nombre in probabilidades.keys():
        # Generamos un número aleatorio para determinar el estado
        num_aleatorio = random.random()
        
        # Determinamos el estado basado en las probabilidades
        if num_aleatorio < probabilidades[nombre]["Feliz"]:
            estado_actual = "Feliz"
        else:
            estado_actual = "Triste"
        
        # Mostramos el estado actual de la persona
        print(f"{nombre} está {estado_actual}.")

# Definimos cuántas simulaciones queremos realizar
simulaciones = 3  # Simulamos 3 veces

# Ejecutamos la simulación
for i in range(simulaciones):
    print(f"\nSimulación {i + 1}:")
    simular_estado()
