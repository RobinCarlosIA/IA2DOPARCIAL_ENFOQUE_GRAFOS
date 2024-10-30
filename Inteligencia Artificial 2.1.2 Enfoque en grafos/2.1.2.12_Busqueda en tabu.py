class Node:
    """Clase que representa un nodo en la búsqueda tabú."""
    
    def __init__(self, name, heuristic):
        self.name = name  # Nombre del nodo.
        self.heuristic = heuristic  # Valor heurístico del nodo.
        self.children = []  # Lista de nodos hijos.

def tabu_search(start_node, iterations, tabu_size):
    """Implementación sencilla de la búsqueda tabú."""
    
    current_node = start_node  # Comenzamos en el nodo inicial.
    print(f"Iniciando en el nodo: {current_node.name} con heurística: {current_node.heuristic}")
    
    tabu_list = []  # Lista de nodos que no se pueden visitar (tabú).

    for i in range(iterations):
        print(f"\nIteración {i + 1}:")
        best_neighbor = None
        best_heuristic = float('-inf')  # Comenzamos con el peor valor posible.

        # Evaluamos cada vecino.
        for child in current_node.children:
            if child not in tabu_list:  # Solo consideramos nodos que no están en la lista tabú.
                print(f"  Evaluando vecino: {child.name} con heurística: {child.heuristic}")
                if child.heuristic > best_heuristic:  # Buscamos el vecino con la mejor heurística.
                    best_heuristic = child.heuristic
                    best_neighbor = child

        # Si no hay vecino mejor, terminamos la búsqueda.
        if best_neighbor is None:
            print(f"  No se encontraron vecinos mejores. Terminando búsqueda.")
            break
        
        # Avanzamos al mejor vecino encontrado.
        current_node = best_neighbor
        print(f"  Ascendiendo al nodo: {current_node.name} con heurística: {current_node.heuristic}")

        # Agregamos el nodo actual a la lista tabú.
        tabu_list.append(current_node)
        if len(tabu_list) > tabu_size:  # Si excede el tamaño tabú, eliminamos el nodo más antiguo.
            removed_node = tabu_list.pop(0)
            print(f"  Nodo tabú removido: {removed_node.name}")

    print(f"\nResultado final: Nodo {current_node.name} con heurística: {current_node.heuristic}")

# Definimos algunos nodos.
node_juan = Node("Juan", 3)         # Nodo Juan con heurística 3.
node_armando = Node("Armando", 5)    # Nodo Armando con heurística 5.
node_realizado = Node("Realizado", 7) # Nodo Realizado con heurística 7 (más alto).

# Establecemos la relación de padres e hijos.
node_juan.children.append(node_armando)  # Juan tiene a Armando como hijo.
node_armando.children.append(node_realizado)  # Armando tiene a Realizado como hijo.

# Parámetros para la búsqueda tabú.
iterations = 5  # Número de iteraciones para la búsqueda.
tabu_size = 2   # Tamaño de la lista tabú.

# Realizamos la búsqueda tabú desde el nodo Juan.
tabu_search(node_juan, iterations, tabu_size)
