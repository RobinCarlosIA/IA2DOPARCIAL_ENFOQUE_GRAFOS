import heapq  # Importa la biblioteca para manejar la cola de prioridad

def ucs(grafo, inicio, objetivo):
    # Cola de prioridad para nodos a explorar, empieza con el nodo inicial y costo 0
    cola_prioridad = [(0, inicio)]  # (costo, nodo)
    
    # Diccionario para almacenar el costo más bajo a cada nodo
    costos = {inicio: 0}  
    
    # Diccionario para almacenar el camino hacia cada nodo
    caminos = {inicio: []}  

    # Bucle principal del algoritmo
    while cola_prioridad:
        # Extrae el nodo con menor costo acumulado
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Si llegamos al nodo objetivo, devolvemos el camino y el costo
        if nodo_actual == objetivo:
            return caminos[nodo_actual] + [objetivo], costo_actual

        # Expandir los nodos vecinos
        for vecino, costo in grafo[nodo_actual].items():
            # Calcula el costo total para llegar al vecino
            costo_total = costo_actual + costo

            # Si encontramos un costo menor para el vecino, lo actualizamos
            if vecino not in costos or costo_total < costos[vecino]:
                costos[vecino] = costo_total  # Actualiza el costo más bajo
                caminos[vecino] = caminos[nodo_actual] + [nodo_actual]  # Guarda el camino
                # Añade el vecino a la cola de prioridad
                heapq.heappush(cola_prioridad, (costo_total, vecino))

    return None, float('inf')  # Retorna si no se encontró el objetivo

# Ejemplo de uso
grafo = {
    'A': {'B': 1, 'C': 4},  # Conexiones desde A
    'B': {'A': 1, 'D': 2, 'E': 5},  # Conexiones desde B
    'C': {'A': 4, 'E': 1},  # Conexiones desde C
    'D': {'B': 2, 'E': 1},  # Conexiones desde D
    'E': {'B': 5, 'C': 1, 'D': 1}  # Conexiones desde E
}

# Definimos el nodo inicial y el objetivo
inicio = 'A'
objetivo = 'E'

# Ejecutamos el algoritmo UCS y guardamos el resultado
camino, costo = ucs(grafo, inicio, objetivo)

# Imprimimos el resultado
print(f'Camino más corto de {inicio} a {objetivo}: {camino} con costo {costo}')
