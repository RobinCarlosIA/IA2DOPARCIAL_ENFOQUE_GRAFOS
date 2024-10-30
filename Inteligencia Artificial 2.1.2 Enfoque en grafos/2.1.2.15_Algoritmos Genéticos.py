import random

def create_population():
    """Crea una población inicial con nombres y valores aleatorios."""
    return [
        ("Fernanda", random.randint(1, 10)), 
        ("Emmanuel", random.randint(1, 10)), 
        ("Carlos", random.randint(1, 10))
    ]

def fitness(individual):
    """Devuelve la aptitud del individuo (su valor)."""
    return individual[1]

def selection(population):
    """Selecciona los dos mejores individuos de la población."""
    population.sort(key=fitness, reverse=True)  # Ordenar por valor
    return population[:2]  # Retornar los dos mejores

def crossover(parent1, parent2):
    """Combina dos padres para crear un nuevo individuo."""
    child_name = f"{parent1[0]}-{parent2[0]}"  # Combina los nombres
    child_value = (parent1[1] + parent2[1]) // 2  # Promedio de los valores
    return (child_name, child_value)

def genetic_algorithm(generations):
    """Función principal del algoritmo genético."""
    population = create_population()  # Crear población inicial
    print("Población inicial:", population)

    for generation in range(generations):
        print(f"\nGeneración {generation + 1}:")
        
        selected = selection(population)  # Seleccionar los mejores
        print("Seleccionados:", selected)

        # Crear un nuevo hijo a partir de los seleccionados
        child = crossover(selected[0], selected[1])
        population = selected + [child]  # Nueva población

        print("Nueva población:", population)

    # Resultado final
    best_individual = selection(population)[0]
    print(f"\nResultado final: Mejor individuo: {best_individual}")

# Número de generaciones
generations = 5

# Ejecutar el algoritmo genético
genetic_algorithm(generations)
