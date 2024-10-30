import random

def online_search(names):
    """Realiza una búsqueda online en una lista de nombres."""
    
    found = []  # Lista para almacenar los nombres encontrados
    print("Nombres disponibles:", names)

    # Simulamos la búsqueda de cada nombre
    for name in names:
        print(f"\nBuscando nombre: {name}")
        if random.random() < 0.5:  # 50% de probabilidad de encontrar el nombre
            found.append(name)  # Agregar a la lista de encontrados
            print(f"Nombre encontrado: {name}")
        else:
            print(f"Nombre no encontrado: {name}")

    # Resultado final
    print("\nNombres encontrados en la búsqueda online:", found)

# Lista de nombres a buscar
names = ["Fernanda", "Emmanuel", "Carlos"]

# Ejecutar la búsqueda online
online_search(names)
