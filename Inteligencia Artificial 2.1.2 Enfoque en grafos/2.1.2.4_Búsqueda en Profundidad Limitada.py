# Definimos una clase simple para representar el grafo.
class Graph:

    def __init__(self):
        # El grafo se representará como un diccionario donde las claves son los vértices
        # y los valores son listas de vecinos conectados.
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        # Método para agregar una arista bidireccional entre dos vértices.
        if vertex not in self.graph:
            self.graph[vertex] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        # Añadimos la arista en ambas direcciones (grafo no dirigido).
        self.graph[vertex].append(neighbor)
        self.graph[neighbor].append(vertex)

    def dfs_limited(self, start_vertex, max_depth, visited=None, depth=0):
        # Método para realizar una búsqueda en profundidad limitada (DFS).
        # Se detendrá si se alcanza la profundidad máxima `max_depth`.
        
        if visited is None:
            visited = set()  # Inicializamos el conjunto de vértices visitados.
        
        # Marcamos el vértice actual como visitado.
        visited.add(start_vertex)
        print(start_vertex, end=" ")  # Imprimimos el vértice actual.

        # Si hemos alcanzado la profundidad máxima, nos detenemos.
        if depth >= max_depth:
            return

        # Recorremos los vecinos del vértice actual.
        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                # Si el vecino no ha sido visitado y no hemos alcanzado la profundidad máxima,
                # hacemos una llamada recursiva para visitarlo, aumentando la profundidad.
                self.dfs_limited(neighbor, max_depth, visited, depth + 1)

# Ejemplo de uso:
g = Graph()  # Creamos una instancia del grafo.

# Agregamos algunas aristas al grafo.
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')

# Establecemos la profundidad máxima para la búsqueda.
max_depth = 2

# Iniciamos la búsqueda en profundidad limitada (DFS) desde el vértice 'A' con una profundidad máxima.
print(f"Recorrido DFS limitado con profundidad máxima de {max_depth}:")
g.dfs_limited('A', max_depth)
