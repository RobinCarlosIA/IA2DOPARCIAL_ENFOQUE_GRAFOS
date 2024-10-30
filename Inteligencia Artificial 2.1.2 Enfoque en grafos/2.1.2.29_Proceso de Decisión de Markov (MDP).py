import random

# Definimos los estados posibles
estados = ["Invertir", "Ahorrar", "Gastar"]

# Recompensas por cada estado
recompensas = {
    "Invertir": 10,  # Ganar 10 puntos al invertir
    "Ahorrar": 5,    # Ganar 5 puntos al ahorrar
    "Gastar": -1     # Perder 1 punto al gastar
}

# Estado inicial de cada persona
personas = {
    "Fernanda": "Ahorrar",
    "Emmanuel": "Invertir",
    "Carlos": "Gastar"
}

# Función que simula una ronda del MDP
def simular_ronda(personas):
    """Simula una ronda del proceso de decisión de Markov."""
    for nombre, estado_actual in personas.items():
        # Elegimos un nuevo estado aleatorio
        nuevo_estado = random.choice(estados)
        recompensa = recompensas[nuevo_estado]  # Obtenemos la recompensa del nuevo estado
        
        # Mostramos el cambio de estado y la recompensa
        print(f"{nombre} pasó de '{estado_actual}' a '{nuevo_estado}' y ganó {recompensa} puntos.")
        
        # Actualizamos el estado de la persona
        personas[nombre] = nuevo_estado

# Definimos cuántas rondas queremos simular
rondas = 3  # Simulamos 3 rondas

# Ejecutamos la simulación
for i in range(rondas):
    print(f"\nRonda {i + 1}:")
    simular_ronda(personas)
