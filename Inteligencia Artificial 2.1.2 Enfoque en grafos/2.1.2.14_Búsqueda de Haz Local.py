import random

def local_beam_search(initial_states, beam_width, iterations):
    """Implementación simple de la búsqueda de haz local."""
    
    current_states = initial_states  # Estados actuales
    print("Estados iniciales:", current_states)

    for i in range(iterations):
        print(f"\nIteración {i + 1}:")

        next_states = []  # Lista para los próximos estados

        # Generar nuevos estados a partir de los estados actuales
        for state in current_states:
            # Generar un nuevo valor aleatorio para cada estado
            new_value = random.randint(1, 10)  # Valor aleatorio entre 1 y 10
            new_state = (state, new_value)  # Crear un nuevo estado con el nombre y el nuevo valor
            next_states.append(new_state)
            print(f"  Generando nuevo estado: {new_state}")

        # Ordenar los nuevos estados por su valor y seleccionar los mejores
        next_states.sort(key=lambda x: x[1], reverse=True)  # Ordenar por el valor
        current_states = [state for state, _ in next_states[:beam_width]]  # Seleccionar los mejores

        print("  Estados actuales después de selección:", current_states)

    # Resultado final
    best_state = current_states[0]  # Mejor estado encontrado
    print(f"\nResultado final: Mejor estado: {best_state} con valor asociado.")

# Definimos los estados iniciales con nombres y valores
initial_states = [
    ("Fernanda", 3),
    ("Emmanuel", 5),
    ("Carlos", 7)
]

# Configuraciones de búsqueda
beam_width = 2  # Número de mejores estados a mantener
iterations = 5  # Número de iteraciones

# Ejecutar la búsqueda de haz local
local_beam_search(initial_states, beam_width, iterations)
