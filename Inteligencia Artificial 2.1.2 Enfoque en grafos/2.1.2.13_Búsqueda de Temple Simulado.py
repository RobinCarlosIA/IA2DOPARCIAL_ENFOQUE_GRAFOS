import random
import math

def simulated_annealing(initial_value, initial_temp, cooling_rate, iterations):
    """Implementación simple de la búsqueda de temple simulado."""
    
    current_value = initial_value  # Valor inicial
    best_value = current_value  # Mejor valor encontrado
    best_name = "Fernanda"  # Nombre del nodo inicial
    print(f"Iniciando en: {best_name} con valor: {current_value}")

    temperature = initial_temp  # Temperatura inicial

    for i in range(iterations):
        # Generar un nuevo valor aleatorio
        neighbor_value = random.randint(1, 10)  # Valor aleatorio entre 1 y 10
        print(f"\nIteración {i + 1}: Vecino generado con valor: {neighbor_value}")

        # Evaluar si el nuevo valor es mejor
        if neighbor_value > current_value:
            current_value = neighbor_value  # Aceptar el nuevo valor
            print(f"Aceptando nuevo valor: {current_value}")
            
            # Actualizar el mejor valor encontrado
            if current_value > best_value:
                best_value = current_value
                best_name = "Emmanuel"  # Cambiar el nombre si se encuentra un mejor valor
                print(f"Nuevo mejor valor: {best_value} en {best_name}")
        else:
            # Calcular la probabilidad de aceptación para un valor peor
            acceptance_probability = math.exp((neighbor_value - current_value) / temperature)
            print(f"Probabilidad de aceptación: {acceptance_probability:.4f}")

            # Aceptar el nuevo valor con cierta probabilidad
            if random.random() < acceptance_probability:
                current_value = neighbor_value
                print(f"Aceptando peor valor: {current_value}")

        # Reducir la temperatura
        temperature *= cooling_rate
        print(f"Temperatura actual: {temperature:.4f}")

    print(f"\nResultado final: Mejor valor: {best_value} en {best_name}")

# Parámetros iniciales
initial_value = 3  # Valor inicial
initial_temp = 1000  # Temperatura inicial
cooling_rate = 0.9  # Tasa de enfriamiento
iterations = 10  # Número de iteraciones

# Ejecutar la búsqueda de temple simulado
simulated_annealing(initial_value, initial_temp, cooling_rate, iterations)
