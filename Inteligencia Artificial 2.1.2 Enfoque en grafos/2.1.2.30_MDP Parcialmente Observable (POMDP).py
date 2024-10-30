import random

# Definimos los estados y las recompensas
estados = ["Invertir", "Ahorrar", "Gastar"]
recompensas = [10, 5, -1]  # Recompensas para cada estado

# Inicializamos el estado de cada persona
personas = {
    "Fernanda": "Ahorrar",
    "Emmanuel": "Invertir",
    "Carlos": "Gastar"
}

# Función que simula una ronda del POMDP
def simular_ronda():
    """Simula una ronda del proceso de decisión de Markov parcialmente observable."""
    for nombre in personas.keys():
        # Elegimos un nuevo estado aleatorio
        nuevo_estado = random.choice(estados)
        
        # Asignamos la recompensa según el nuevo estado
        recompensa = recompensas[estados.index(nuevo_estado)]
        
        # Mostramos la decisión y la recompensa
        print(f"{nombre} decidió '{nuevo_estado}' y ganó {recompensa} puntos.")

        # Actualizamos el estado de la persona
        personas[nombre] = nuevo_estado

# Definimos cuántas rondas queremos simular
rondas = 3  # Simulamos 3 rondas

# Ejecutamos la simulación
for i in range(rondas):
    print(f"\nRonda {i + 1}:")
    simular_ronda()
