class Node:
    """Clase que representa un nodo en el grafo."""
    
    def __init__(self, name, heuristic, cost):
        self.name = name  # Nombre del nodo.
        self.heuristic = heuristic  # Valor heurístico del nodo.
        self.cost = cost  # Costo para llegar a este nodo.

    def f(self):
        """Función f(n) = g(n) + h(n)"""
        return self.cost + self.heuristic  # Costo total (g + h).

def a_star_search(start_node, goal_node):
    """Implementación sencilla de la búsqueda A*."""
    
    open_list = [start_node]  # Lista de nodos a explorar.
    closed_list = []  # Lista de nodos explorados.

    while open_list:
        # Ordenamos los nodos abiertos por su valor f(n).
        open_list.sort(key=lambda node: node.f())
        
        current_node = open_list.pop(0)  # Tomamos el nodo con el menor f(n).
        print(f"Explorando nodo: {current_node.name} con f(n): {current_node.f()}")

        # Si encontramos el nodo objetivo, terminamos la búsqueda.
        if current_node.name == goal_node.name:
            print(f"¡Objetivo encontrado: {current_node.name}!")
            return
        
        closed_list.append(current_node)  # Agregamos el nodo explorado a la lista cerrada.

        # Aquí podrías agregar lógica para explorar nodos hijos, omitimos por simplicidad.

    print("El objetivo no fue encontrado.")

# Definimos algunos nodos con sus nombres, valores heurísticos y costos.
node_juan = Node("Juan", 3, 0)         # Nodo Juan (heurística: 3, costo: 0).
node_armando = Node("Armando", 2, 1)    # Nodo Armando (heurística: 2, costo: 1).
node_realizado = Node("Realizado", 0, 3) # Nodo Realizado (heurística: 0, costo: 3).

goal_node = node_realizado  # El nodo objetivo es Realizado.

# Realizamos la búsqueda A* desde el nodo Juan hacia el nodo objetivo.
a_star_search(node_juan, goal_node)
