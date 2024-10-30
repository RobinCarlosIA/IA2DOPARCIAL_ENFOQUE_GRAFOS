import random

# Definimos las acciones que pueden elegir las personas
acciones = ["Acción A", "Acción B"]

# Inicializamos la tabla de recompensas para cada persona
recompensas = {
    "Fernanda": {accion: 0 for accion in acciones},
    "Emmanuel": {accion: 0 for accion in acciones},
    "Carlos": {accion: 0 for accion in acciones}
}

# Definimos una política simple: elegir la acción con la mayor recompensa
def politica_simple(nombre):
    """Devuelve la acción recomendada según la política."""
    return max(recompensas[nombre], key=recompensas[nombre].get)

# Parámetros de la simulación
num_iteraciones = 10  # Número de iteraciones para la simulación

# Función que simula la búsqueda de la política
def busqueda_de_la_politica():
    """Simula el proceso de búsqueda de la política para cada persona."""
    
    for i in range(num_iteraciones):
        for nombre in recompensas.keys():
            # Obtenemos la acción recomendada según la política
            accion_recomendada = politica_simple(nombre)
            print(f"Iteración {i + 1}: {nombre} elige {accion_recomendada} según la política.")

            # Simulamos una recompensa aleatoria entre 1 y 10
            recompensa = random.randint(1, 10)
            print(f"{nombre} recibe una recompensa de {recompensa}.")

            # Actualizamos la recompensa promedio de la acción elegida
            recompensas[nombre][accion_recomendada] += (recompensa - recompensas[nombre][accion_recomendada]) * 0.1  # Ajuste suave

# Ejecutamos la simulación
busqueda_de_la_politica()

# Mostramos las recompensas acumuladas después de la simulación
print("\nRecompensas acumuladas después de la simulación:")
for nombre, valores in recompensas.items():
    print(f"{nombre}: {valores}")
