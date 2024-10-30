import random

# Definimos las acciones que pueden elegir las personas
acciones = ["Acción A", "Acción B"]

# Inicializamos la tabla de recompensas para cada persona
recompensas = {
    "Fernanda": {accion: 0 for accion in acciones},
    "Emmanuel": {accion: 0 for accion in acciones},
    "Carlos": {accion: 0 for accion in acciones}
}

# Parámetros de exploración
epsilon = 0.3  # Probabilidad de explorar
num_iteraciones = 10  # Número de iteraciones para la simulación

# Función que simula la exploración vs. explotación
def exploracion_vs_explotacion():
    """Simula el proceso de exploración y explotación para cada persona."""
    
    for i in range(num_iteraciones):
        for nombre in recompensas.keys():
            # Decidimos si exploramos o explotamos
            if random.random() < epsilon:
                # Exploración: elegimos una acción aleatoria
                accion = random.choice(acciones)
                print(f"Iteración {i + 1}: {nombre} eligió {accion} (exploración).")
            else:
                # Explotación: elegimos la mejor acción conocida
                mejor_accion = max(recompensas[nombre], key=recompensas[nombre].get)
                accion = mejor_accion
                print(f"Iteración {i + 1}: {nombre} eligió {accion} (explotación).")

            # Simulamos una recompensa aleatoria entre 1 y 10
            recompensa = random.randint(1, 10)
            print(f"{nombre} recibió una recompensa de {recompensa}.")

            # Actualizamos la recompensa promedio de la acción elegida
            recompensas[nombre][accion] += (recompensa - recompensas[nombre][accion]) * 0.1  # Ajuste suave

# Ejecutamos la simulación
exploracion_vs_explotacion()

# Mostramos las recompensas acumuladas después de la simulación
print("\nRecompensas acumuladas después de la simulación:")
for nombre, valores in recompensas.items():
    print(f"{nombre}: {valores}")
