from collections import deque  # Importamos deque, una estructura de cola eficiente

# Función de búsqueda en anchura
def bfs(grafo, nodo_inicio, objetivo):
    # Inicializamos la cola con el nodo de inicio
    cola = deque([nodo_inicio])
    
    # Inicializamos un conjunto de nodos visitados para evitar visitar nodos más de una vez
    visitados = set([nodo_inicio])
    
    # Mientras haya nodos en la cola, seguimos explorando
    while cola:
        # Sacamos el nodo que está en el frente de la cola para explorarlo
        nodo_actual = cola.popleft()
        
        # Imprimimos qué nodo estamos explorando
        print(f"Explorando nodo: {nodo_actual}")
        
        # Si el nodo actual es el nodo objetivo, terminamos la búsqueda
        if nodo_actual == objetivo:
            print(f"Objetivo {objetivo} encontrado!")  # Encontramos el nodo objetivo
            return True  # Terminamos la función retornando True, indicando que lo encontramos
        
        # Recorremos los vecinos del nodo actual
        for vecino in grafo[nodo_actual]:
            # Si el vecino no ha sido visitado
            if vecino not in visitados:
                visitados.add(vecino)  # Marcamos el vecino como visitado
                cola.append(vecino)  # Añadimos el vecino a la cola para explorarlo más tarde
    
    # Si se recorrieron todos los nodos y no se encontró el objetivo
    print(f"Objetivo {objetivo} no encontrado.")  # Indicamos que no lo encontramos
    return False  # Retornamos False porque el nodo objetivo no fue encontrado

# Definimos el grafo, un diccionario donde las claves son los nodos y los valores son las listas de vecinos
grafo = {
    'A': ['B', 'C'],  # Nodo A está conectado con B y C
    'B': ['D'],       # Nodo B está conectado con D
    'C': ['D'],       # Nodo C también está conectado con D
    'D': []           # Nodo D no tiene vecinos
}

# Parámetros de la búsqueda: nodo inicial 'A' y el nodo objetivo 'D'
nodo_inicio = 'A'
objetivo = 'D'

# Ejecutamos la función BFS con el grafo, nodo inicial y nodo objetivo
bfs(grafo, nodo_inicio, objetivo)
