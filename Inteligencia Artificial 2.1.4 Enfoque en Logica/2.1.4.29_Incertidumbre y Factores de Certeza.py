import random

# Definimos una función para simular un evento con una certeza dada
def simular_evento(nombre_evento, certeza):
    # Generamos un número aleatorio entre 0 y 1
    resultado = random.random()
    
    # Verificamos si el resultado está dentro de la certeza
    if resultado < certeza:
        print(f"El evento '{nombre_evento}' ocurre con certeza de {certeza * 100}%.")
    else:
        print(f"El evento '{nombre_evento}' NO ocurre. (Incertidumbre)")

# Definimos algunos eventos y sus niveles de certeza
eventos = {
    "Lluvia": 0.7,  # 70% de certeza de que llueva
    "Sol": 0.5,     # 50% de certeza de que salga el sol
    "Nieve": 0.1    # 10% de certeza de que nieve
}

# Simulamos los eventos
for evento, certeza in eventos.items():
    simular_evento(evento, certeza)
