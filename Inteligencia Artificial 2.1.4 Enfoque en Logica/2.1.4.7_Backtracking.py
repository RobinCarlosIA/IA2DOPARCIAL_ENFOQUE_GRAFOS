# Función de backtracking para encontrar combinaciones de una lista de números
def encontrar_combinaciones(nums, objetivo):
    # Lista para almacenar las combinaciones que sumen al objetivo
    soluciones = []

    # Función auxiliar que usa backtracking
    def backtrack(combinacion_actual, inicio):
        # Si la suma de la combinación actual es igual al objetivo, la guardamos
        if sum(combinacion_actual) == objetivo:
            soluciones.append(list(combinacion_actual))
            return
        # Intentamos agregar cada número a la combinación actual
        for i in range(inicio, len(nums)):
            # Agregamos el número a la combinación
            combinacion_actual.append(nums[i])
            # Llamamos recursivamente a la función para probar la siguiente posición
            backtrack(combinacion_actual, i + 1)
            # Quitamos el último número para probar con otro
            combinacion_actual.pop()

    # Iniciamos el proceso de backtracking con una combinación vacía
    backtrack([], 0)
    return soluciones

# Lista de números y el objetivo que queremos alcanzar con sus combinaciones
nums = [2, 3, 5, 7]
objetivo = 10

# Llamamos a la función y mostramos todas las combinaciones que suman al objetivo
combinaciones = encontrar_combinaciones(nums, objetivo)
print("Combinaciones que suman a", objetivo, ":", combinaciones)
