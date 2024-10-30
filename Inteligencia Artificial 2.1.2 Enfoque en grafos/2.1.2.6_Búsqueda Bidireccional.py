from collections import deque

# Clase para representar un grafo simple.
class Graph:
    
    def __init__(self):
        self.graph = {}  # Diccionario para almacenar el grafo.

    def add_edge(self, person1, person2):
        # Agrega una conexión entre dos personas.
        if person1 not in self.graph:
            self.graph[person1] = []  # Si no existe, inicializamos su lista.
        if person2 not in self.graph:
            self.graph[person2] = []  # Hacemos lo mismo para la otra persona.
        self.graph[person1].append(person2)  # Conectamos person1 a person2.
        self.graph[person2].append(person1)  # Conectamos person2 a person1.

    def bidirectional_search(self, start, goal):
        # Busca un camino desde start hasta goal.
        if start == goal:
            return [start]  # Retorna el camino inmediato si son iguales.

        # Inicializamos colas para búsqueda.
        start_queue = deque([start])
        goal_queue = deque([goal])

        visited_from_start = {start}  # Personas visitadas desde el inicio.
        visited_from_goal = {goal}  # Personas visitadas desde el objetivo.

        # Mientras tengamos personas en ambas colas:
        while start_queue and goal_queue:
            # Expandimos desde el inicio.
            if self._expand_node(start_queue, visited_from_start, visited_from_goal):
                return list(visited_from_start)  # Retorna el camino si se encuentra.

            # Expandimos desde el objetivo.
            if self._expand_node(goal_queue, visited_from_goal, visited_from_start):
                return list(visited_from_goal)  # Retorna el camino si se encuentra.

        return []  # Retorna vacío si no hay camino.

    def _expand_node(self, queue, visited_from_this_side, visited_from_other_side):
        # Expande una persona en la búsqueda.
        current = queue.popleft()  # Sacamos la persona de la cola.

        # Revisamos las conexiones de la persona.
        for neighbor in self.graph.get(current, []):
            if neighbor not in visited_from_this_side:
                visited_from_this_side.add(neighbor)  # Marcamos como visitado.
                queue.append(neighbor)  # Agregamos a la cola.

                # Comprobamos si esta persona fue visitada desde el otro lado.
                if neighbor in visited_from_other_side:
                    return True  # Se encontró un camino.

        return False  # No se encontró un camino.

# Ejemplo de uso:
g = Graph()  # Creamos un grafo.

# Agregamos conexiones entre las personas.
g.add_edge('Fernanda', 'Emmanuel')
g.add_edge('Fernanda', 'Emiliano')
g.add_edge('Emmanuel', 'Eliott')
g.add_edge('Emiliano', 'Eliott')

# Buscamos un camino entre 'Fernanda' y 'Eliott'.
path = g.bidirectional_search('Fernanda', 'Eliott')
print("Camino encontrado:", path)
