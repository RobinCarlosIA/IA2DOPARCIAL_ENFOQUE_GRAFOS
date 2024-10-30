class Node:
    """Clase que representa un nodo en el grafo."""
    
    def __init__(self, name, heuristic):
        self.name = name  # Nombre del nodo.
        self.heuristic = heuristic  # Valor heurístico del nodo.

def best_first_search(start_node, goal_node):
    """Implementación de búsqueda voraz primero el mejor."""
    
    # Lista de nodos a explorar, comenzando con el nodo inicial.
    open_list = [start_node]
    
    while open_list:
        # Ordenamos la lista de nodos por su valor heurístico (menor primero).
        open_list.sort(key=lambda node: node.heuristic)
        
        # Elegimos el nodo con el menor valor heurístico.
        current_node = open_list.pop(0)
        print(f"Explorando nodo: {current_node.name} con heurística: {current_node.heuristic}")

        # Si encontramos el nodo objetivo, terminamos la búsqueda.
        if current_node.name == goal_node.name:
            print(f"¡Objetivo encontrado: {current_node.name}!")
            return
        
        # Aquí podrías agregar más nodos hijos al open_list según la estructura del grafo.
        # Por simplicidad, omitimos esa parte.

    print("El objetivo no fue encontrado.")

# Definimos algunos nodos con sus nombres y valores heurísticos.
node_juan = Node("Juan", 3)          # Nodo Juan con heurística 3.
node_armando = Node("Armando", 2)    # Nodo Armando con heurística 2.
node_realizado = Node("Realizado", 1) # Nodo Realizado con heurística 1 (más cerca del objetivo).

# Definimos el nodo objetivo.
goal_node = node_realizado             # El nodo objetivo es Realizado.

# Realizamos la búsqueda desde el nodo Juan hacia el nodo objetivo.
best_first_search(node_juan, goal_node)

