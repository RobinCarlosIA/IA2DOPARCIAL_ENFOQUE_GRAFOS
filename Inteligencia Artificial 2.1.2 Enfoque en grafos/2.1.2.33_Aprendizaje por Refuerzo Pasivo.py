import random

# Definimos las acciones posibles
acciones = ["Acción 1", "Acción 2"]

# Inicializamos las recompensas esperadas para cada persona
recompensas_esperadas = {
    "Fernanda": 0,
    "Emmanuel": 0,
    "Carlos": 0
}

# Función que simula el aprendizaje por refuerzo pasivo
def aprender_por_refuerzo():
    """Simula el aprendizaje por refuerzo pasivo de cada persona."""
    for nombre in recompensas_esperadas.keys():
        # Elegimos una acción aleatoria
        accion = random.choice(acciones)
        
        # Simulamos una recompensa aleatoria para la acción
        recompensa = random.randint(1, 10)  # Recompensas entre 1 y 10
        print(f"{nombre} eligió {accion} y recibió una recompensa de {recompensa}.")
        
        # Actualizamos la recompensa esperada
        recompensas_esperadas[nombre] = (recompensas_esperadas[nombre] + recompensa) / 2  # Promedio

# Ejecutamos la simulación
aprender_por_refuerzo()

# Mostramos las recompensas esperadas después de la simulación
print("\nRecompensas esperadas después de la simulación:")
for nombre, recompensa in recompensas_esperadas.items():
    print(f"{nombre}: {recompensa:.2f}")
