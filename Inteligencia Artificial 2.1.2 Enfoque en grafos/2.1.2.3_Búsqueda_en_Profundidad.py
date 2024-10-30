# Función DFS para realizar la búsqueda en profundidad
def dfs(graph, node, visited):
    # Marcar el nodo como visitado
    print(f"Visitando nodo {node}")
    visited.add(node)  # Agregar el nodo al conjunto de nodos visitados

    # Explorar cada nodo adyacente al nodo actual
    for neighbor in graph[node]:
        if neighbor not in visited:  # Si el vecino no ha sido visitado
            dfs(graph, neighbor, visited)  # Llamada recursiva para visitar el vecino

# Grafo representado como un diccionario (lista de adyacencia)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

# Conjunto para llevar el registro de los nodos visitados
visited = set()

# Iniciar la DFS desde el nodo 0
dfs(graph, 0, visited)
