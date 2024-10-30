import numpy as np

# Red de Hamming para clasificación
def red_hamming(entrada, patrones):
    # Calculamos la similitud entre el patrón de entrada y los patrones almacenados.
    similaridades = patrones @ entrada
    indice_clasificacion = np.argmax(similaridades)
    print("Red de Hamming - Clasificación:", patrones[indice_clasificacion])

# Red de Hopfield para memoria asociativa
def red_hopfield(patron_original, patron_ruidoso, iteraciones=5):
    # Crear matriz de pesos
    pesos = np.outer(patron_original, patron_original) - np.eye(len(patron_original))
    
    # Recuperar patrón a partir del patrón ruidoso
    for _ in range(iteraciones):
        patron_ruidoso = np.sign(pesos @ patron_ruidoso)
    print("Red de Hopfield - Patrón Recuperado:", patron_ruidoso)

# Red de Hebb para aprendizaje
def regla_hebb(entrada, salida):
    # Inicializamos pesos
    pesos = np.zeros((entrada.shape[1], salida.shape[1]))
    
    # Actualizar pesos con la regla de Hebb
    for x, y in zip(entrada, salida):
        pesos += np.outer(x, y)
    print("Regla de Hebb - Pesos Aprendidos:\n", pesos)

# Máquina de Boltzmann para actualización estocástica
def maquina_boltzmann(estados, pesos, temp=1.0, iteraciones=5):
    # Actualizar estados de forma probabilística
    def actualizar_estado(estados, pesos, temp):
        for i in range(len(estados)):
            energia = pesos[i] @ estados
            prob = 1 / (1 + np.exp(-2 * energia / temp))
            estados[i] = 1 if np.random.rand() < prob else -1
        return estados

    for _ in range(iteraciones):
        estados = actualizar_estado(estados, pesos, temp)
    print("Máquina de Boltzmann - Estados Finales:", estados)

# Ejemplos para cada red:
# 1. Red de Hamming
entrada_hamming = np.array([1, 1, -1, -1])
patrones_hamming = np.array([[1, 1, -1, -1], [-1, -1, 1, 1]])
red_hamming(entrada_hamming, patrones_hamming)

# 2. Red de Hopfield
patron_original = np.array([1, -1, 1, -1])
patron_ruidoso = np.array([1, -1, -1, -1])
red_hopfield(patron_original, patron_ruidoso)

# 3. Regla de Hebb
entrada_hebb = np.array([[1, -1], [-1, 1]])
salida_hebb = np.array([[1], [-1]])
regla_hebb(entrada_hebb, salida_hebb)

# 4. Máquina de Boltzmann
estados_boltzmann = np.array([1, -1])
pesos_boltzmann = np.array([[0, 1], [1, 0]])
maquina_boltzmann(estados_boltzmann, pesos_boltzmann)
