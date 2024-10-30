# Definimos una clase simple para representar el grafo.
class Graph:

    def __init__(self):
        # El grafo será un diccionario donde cada clave es un vértice
        # y cada valor es una lista de vecinos (conexiones).
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        # Agregamos una arista entre dos vértices (bidireccional).
        if vertex not in self.graph:
            self.graph[vertex] = []  # Si el vértice no existe, lo inicializamos.
        if neighbor not in self.graph:
            self.graph[neighbor] = []  # Inicializamos el vecino si no existe.
        self.graph[vertex].append(neighbor)  # Conectamos el vértice al vecino.
        self.graph[neighbor].append(vertex)  # Conectamos el vecino al vértice (grafo no dirigido).

    def dfs_iterative(self, start_vertex):
        # Método para realizar DFS de manera iterativa usando una pila.
        
        visited = set()  # Conjunto para almacenar los vértices visitados.
        stack = [start_vertex]  # Usamos una pila y agregamos el vértice inicial.

        while stack:  # Mientras haya vértices en la pila:
            vertex = stack.pop()  # Sacamos el último vértice agregado (LIFO).

            if vertex not in visited:  # Si el vértice no ha sido visitado:
                print(vertex, end=" ")  # Lo imprimimos.
                visited.add(vertex)  # Lo marcamos como visitado.

                # Agregamos los vecinos del vértice a la pila.
                # No usamos `reversed()` en esta versión simplificada.
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)

# Ejemplo de uso:
g = Graph()  # Creamos una instancia del grafo.

# Agregamos algunas aristas al grafo.
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')

# Iniciamos la búsqueda en profundidad iterativa (DFS) desde el vértice 'A'.
print("Recorrido DFS Iterativo:")
g.dfs_iterative('A')
