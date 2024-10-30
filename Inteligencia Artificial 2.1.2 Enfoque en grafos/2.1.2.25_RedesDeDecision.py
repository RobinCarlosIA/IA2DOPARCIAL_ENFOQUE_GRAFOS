# Aquí definimos las decisiones de Fernanda, Emmanuel y Carlos, junto con la probabilidad de éxito y sus utilidades
decisiones = {
    "Fernanda": {
        "decisión": "Invertir",  # Fernanda decidió invertir
        "probabilidad": 0.7,  # Hay un 70% de probabilidades de que su inversión sea exitosa
        "utilidad_si_exito": 80,  # Si su inversión tiene éxito, obtiene una utilidad de 80
        "utilidad_si_falla": 10   # Si su inversión falla, solo obtiene una utilidad de 10
    },
    "Emmanuel": {
        "decisión": "Ahorrar",  # Emmanuel decidió ahorrar
        "probabilidad": 0.9,  # Hay un 90% de probabilidades de que su ahorro sea exitoso
        "utilidad_si_exito": 60,  # Si el ahorro genera retorno, obtiene una utilidad de 60
        "utilidad_si_falla": 20   # Si el ahorro no genera retorno, obtiene una utilidad de 20
    },
    "Carlos": {
        "decisión": "Gastar",  # Carlos decidió gastar
        "probabilidad": 0.6,  # Hay un 60% de probabilidades de que el gasto sea útil
        "utilidad_si_exito": 50,  # Si el gasto fue una buena decisión, obtiene una utilidad de 50
        "utilidad_si_falla": 15   # Si el gasto no fue útil, obtiene una utilidad de 15
    }
}

# Esta función calcula la utilidad esperada de cada decisión
def calcular_utilidad_esperada(probabilidad, utilidad_exito, utilidad_falla):
    """Calcula qué tan útil es una decisión según la probabilidad de éxito y fallo."""
    return (probabilidad * utilidad_exito) + ((1 - probabilidad) * utilidad_falla)

# Recorremos cada persona para calcular la utilidad esperada de su decisión
for nombre, info in decisiones.items():
    decision = info["decisión"]
    probabilidad = info["probabilidad"]
    utilidad_exito = info["utilidad_si_exito"]
    utilidad_falla = info["utilidad_si_falla"]
    
    # Calculamos la utilidad esperada con los datos de cada persona
    utilidad_esperada = calcular_utilidad_esperada(probabilidad, utilidad_exito, utilidad_falla)
    
    # Mostramos los resultados para cada persona
    print(f"{nombre} tomó la decisión de {decision} con una utilidad esperada de {utilidad_esperada:.2f}.")
