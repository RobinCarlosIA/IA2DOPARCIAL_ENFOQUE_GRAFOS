import random
import math

# Generamos puntos aleatorios
def generar_puntos(n, rango_x, rango_y):
    puntos = []
    for _ in range(n):
        x = random.uniform(*rango_x)
        y = random.uniform(*rango_y)
        puntos.append((x, y))
    return puntos

# Distancia euclidiana entre dos puntos
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Algoritmo K-Means
def k_means(puntos, k, iteraciones=10):
    # Inicializar los centroides aleatoriamente
    centroides = random.sample(puntos, k)

    for _ in range(iteraciones):
        # Asignamos cada punto al centroide más cercano
        clusters = {i: [] for i in range(k)}
        for punto in puntos:
            distancias = [distancia(punto, c) for c in centroides]
            cluster_mas_cercano = distancias.index(min(distancias))
            clusters[cluster_mas_cercano].append(punto)
        
        # Actualizamos los centroides
        for i in range(k):
            if clusters[i]:  # Evitamos división por cero
                centroides[i] = (
                    sum([p[0] for p in clusters[i]]) / len(clusters[i]),  # Promedio de x
                    sum([p[1] for p in clusters[i]]) / len(clusters[i])   # Promedio de y
                )
    
    return clusters, centroides

# Algoritmo k-NN para clasificar un nuevo punto
def k_nn(punto_nuevo, clusters, k):
    distancias = []
    for i, cluster in clusters.items():
        for punto in cluster:
            dist = distancia(punto_nuevo, punto)
            distancias.append((dist, i))  # Guardamos la distancia y el clúster del punto
    
    distancias.sort()  # Ordenamos por distancia
    vecinos_cercanos = [d[1] for d in distancias[:k]]  # Tomamos los k vecinos más cercanos
    
    # Clasificamos según el clúster más frecuente entre los vecinos
    clasificacion = max(set(vecinos_cercanos), key=vecinos_cercanos.count)
    return clasificacion

# Generamos 10 puntos aleatorios
puntos = generar_puntos(10, (0, 10), (0, 10))

# Agrupamos los puntos en 2 clústeres usando K-Means
clusters, centroides = k_means(puntos, 2)

# Mostramos los resultados de los clústeres
print("Clústeres formados:")
for i, cluster in clusters.items():
    print(f"Clúster {i}: {cluster}")

# Nuevo punto a clasificar
punto_nuevo = (3, 3)
clasificacion = k_nn(punto_nuevo, clusters, 3)

print(f"\nEl punto {punto_nuevo} pertenece al clúster {clasificacion}")
