import random

# Definimos las acciones que pueden elegir las personas
acciones = ["Acción A", "Acción B"]

# Inicializamos las recompensas esperadas para cada persona
recompensas_esperadas = {
    "Fernanda": 0,
    "Emmanuel": 0,
    "Carlos": 0
}

# Número de iteraciones para simular el aprendizaje
num_iteraciones = 5

# Función que simula el aprendizaje por refuerzo activo
def aprender_por_refuerzo_activo():
    """Simula el aprendizaje por refuerzo activo para cada persona."""
    
    for i in range(num_iteraciones):
        for nombre in recompensas_esperadas.keys():
            # Elegimos una acción aleatoria para cada persona
            accion = random.choice(acciones)
            
            # Simulamos una recompensa aleatoria entre 1 y 10
            recompensa = random.randint(1, 10)
            print(f"Iteración {i + 1}: {nombre} eligió {accion} y recibió una recompensa de {recompensa}.")
            
            # Actualizamos la recompensa esperada de cada persona
            # Aumentamos el promedio de recompensas esperadas
            recompensas_esperadas[nombre] += (recompensa - recompensas_esperadas[nombre]) * 0.1  # Ajuste suave

# Ejecutamos la simulación
aprender_por_refuerzo_activo()

# Mostramos las recompensas esperadas después de la simulación
print("\nRecompensas esperadas después de la simulación:")
for nombre, recompensa in recompensas_esperadas.items():
    print(f"{nombre}: {recompensa:.2f}")
