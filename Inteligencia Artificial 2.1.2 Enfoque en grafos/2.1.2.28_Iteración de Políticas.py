# Definimos las decisiones de cada persona (Fernanda, Emmanuel, y Carlos) y sus recompensas iniciales
# También les asignamos una política inicial, que se puede mejorar con iteraciones
decisiones = {
    "Fernanda": {
        "política": "Invertir",  # Política actual de Fernanda
        "recompensa": 80  # Recompensa inicial
    },
    "Emmanuel": {
        "política": "Ahorrar",  # Política actual de Emmanuel
        "recompensa": 60  # Recompensa inicial
    },
    "Carlos": {
        "política": "Gastar",  # Política actual de Carlos
        "recompensa": 50  # Recompensa inicial
    }
}

# Lista de posibles políticas para cada persona
posibles_politicas = ["Invertir", "Ahorrar", "Gastar"]

# Función para calcular la recompensa esperada dada una política
def calcular_recompensa(politica):
    """Devuelve la recompensa esperada basada en la política elegida."""
    if politica == "Invertir":
        return 80
    elif politica == "Ahorrar":
        return 60
    elif politica == "Gastar":
        return 50

# Función para iterar sobre las políticas y mejorarlas
def iterar_politicas(decisiones, iteraciones):
    """Ajusta las políticas de cada persona en varias iteraciones para maximizar la recompensa."""
    for i in range(iteraciones):
        print(f"\nIteración {i+1}")
        for nombre, info in decisiones.items():
            mejor_politica = info["política"]  # Inicialmente, la mejor política es la actual
            mejor_recompensa = info["recompensa"]  # La mejor recompensa es la que tienen ahora
            
            # Probamos todas las posibles políticas para encontrar la que da la mayor recompensa
            for politica in posibles_politicas:
                recompensa_esperada = calcular_recompensa(politica)
                if recompensa_esperada > mejor_recompensa:
                    mejor_politica = politica
                    mejor_recompensa = recompensa_esperada
            
            # Actualizamos la política y la recompensa
            info["política"] = mejor_politica
            info["recompensa"] = mejor_recompensa
            
            # Mostramos el resultado de la iteración
            print(f"{nombre} ha cambiado su política a '{mejor_politica}' con una recompensa de {mejor_recompensa}.")

# Definimos el número de iteraciones
iteraciones = 3  # Vamos a iterar 3 veces para mejorar las políticas

# Llamamos a la función para hacer la iteración de políticas
iterar_politicas(decisiones, iteraciones)
