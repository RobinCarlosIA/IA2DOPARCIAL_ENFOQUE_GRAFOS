import random

# Definimos las acciones que pueden elegir las personas
acciones = ["Acción A", "Acción B"]

# Inicializamos la tabla Q para cada persona y cada acción
Q = {
    "Fernanda": {accion: 0 for accion in acciones},
    "Emmanuel": {accion: 0 for accion in acciones},
    "Carlos": {accion: 0 for accion in acciones}
}

# Parámetros de Q-Learning
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
num_iteraciones = 10  # Número de iteraciones para la simulación

# Función que simula el Q-Learning
def q_learning():
    """Simula el aprendizaje por Q-Learning para cada persona."""
    
    for i in range(num_iteraciones):
        for nombre in Q.keys():
            # Elegimos una acción aleatoria de las posibles
            accion = random.choice(acciones)
            
            # Simulamos una recompensa aleatoria entre 1 y 10
            recompensa = random.randint(1, 10)
            print(f"Iteración {i + 1}: {nombre} eligió {accion} y recibió una recompensa de {recompensa}.")
            
            # Actualizamos el valor Q usando la fórmula de Q-Learning
            # Q(s, a) = Q(s, a) + α * (r + γ * max_a Q(s', a) - Q(s, a))
            max_q_next = max(Q[nombre].values())  # Máximo Q para la siguiente acción
            Q[nombre][accion] += alpha * (recompensa + gamma * max_q_next - Q[nombre][accion])

# Ejecutamos la simulación
q_learning()

# Mostramos los valores Q después de la simulación
print("\nValores Q después de la simulación:")
for nombre, valores in Q.items():
    print(f"{nombre}: {valores}")
