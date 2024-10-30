class Node:
    """Clase que representa un nodo en el grafo."""
    
    def __init__(self, name, heuristic):
        self.name = name  # Nombre del nodo.
        self.heuristic = heuristic  # Valor heurístico del nodo.
        self.children = []  # Lista de nodos hijos.

def hill_climbing_search(start_node):
    """Implementación sencilla de la búsqueda de ascensión de colinas."""
    
    current_node = start_node  # Iniciamos desde el nodo inicial.
    print(f"Iniciando en el nodo: {current_node.name} con heurística: {current_node.heuristic}")

    while True:
        # Asumimos que no hay vecinos mejores al inicio.
        best_neighbor = None
        best_heuristic = current_node.heuristic  # El mejor valor heurístico comienza como el del nodo actual.

        # Evaluamos cada vecino para encontrar el mejor.
        for child in current_node.children:
            print(f"Evaluando vecino: {child.name} con heurística: {child.heuristic}")
            if child.heuristic > best_heuristic:  # Si encontramos un vecino con mejor heurística.
                best_heuristic = child.heuristic
                best_neighbor = child

        # Si no hay mejor vecino, hemos llegado a un pico (o objetivo).
        if best_neighbor is None:
            print(f"¡Objetivo encontrado: {current_node.name} con heurística: {current_node.heuristic}!")
            break
        else:
            current_node = best_neighbor  # Avanzamos al mejor vecino.
            print(f"Ascendiendo al nodo: {current_node.name} con heurística: {current_node.heuristic}")

# Definimos algunos nodos.
node_juan = Node("Juan", 3)         # Nodo Juan con heurística 3.
node_armando = Node("Armando", 5)    # Nodo Armando con heurística 5.
node_realizado = Node("Realizado", 7) # Nodo Realizado con heurística 7 (más alto).

# Establecemos la relación de padres e hijos.
node_juan.children.append(node_armando)  # Juan tiene a Armando como hijo.
node_armando.children.append(node_realizado)  # Armando tiene a Realizado como hijo.

# Realizamos la búsqueda de ascensión de colinas desde el nodo Juan.
hill_climbing_search(node_juan)
