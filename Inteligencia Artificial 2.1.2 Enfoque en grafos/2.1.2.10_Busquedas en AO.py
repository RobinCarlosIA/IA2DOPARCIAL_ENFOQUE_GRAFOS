class AONode:
    """Clase que representa un nodo en un grafo AO*."""
    
    def __init__(self, name, heuristic):
        self.name = name  # Nombre del nodo.
        self.heuristic = heuristic  # Valor heurístico del nodo.
        self.children = []  # Lista de nodos hijos.

def ao_star_search(start_node, goal_node):
    """Implementación sencilla de la búsqueda AO*."""
    
    # Inicializamos la lista de nodos a explorar.
    open_list = [start_node]
    
    while open_list:
        current_node = open_list.pop(0)  # Tomamos el primer nodo de la lista.
        print(f"Explorando nodo: {current_node.name} con heurística: {current_node.heuristic}")

        # Si encontramos el nodo objetivo, terminamos la búsqueda.
        if current_node.name == goal_node.name:
            print(f"¡Objetivo encontrado: {current_node.name}!")
            return
        
        # Agregamos los nodos hijos a la lista de nodos a explorar.
        open_list.extend(current_node.children)

    print("El objetivo no fue encontrado.")

# Definimos algunos nodos.
node_juan = AONode("Juan", 3)  # Nodo Juan con heurística 3.
node_armando = AONode("Armando", 2)  # Nodo Armando con heurística 2.
node_realizado = AONode("Realizado", 0)  # Nodo Realizado con heurística 0 (objetivo).

# Establecemos la relación de padres e hijos.
node_juan.children.append(node_armando)  # Juan tiene a Armando como hijo.
node_armando.children.append(node_realizado)  # Armando tiene a Realizado como hijo.

goal_node = node_realizado  # El nodo objetivo es Realizado.

# Realizamos la búsqueda AO* desde el nodo Juan hacia el nodo objetivo.
ao_star_search(node_juan, goal_node)
