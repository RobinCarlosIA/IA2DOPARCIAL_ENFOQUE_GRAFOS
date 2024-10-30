# Decisiones de Fernanda, Emmanuel y Carlos, y sus probabilidades con y sin información adicional
decisiones = {
    "Fernanda": {
        "decisión": "Invertir",  # Fernanda va a invertir
        "probabilidad_sin_info": 0.7,  # Probabilidad de éxito sin información
        "probabilidad_con_info": 0.9,  # Probabilidad de éxito con información adicional
        "utilidad_si_exito": 80,  # Ganancia si la inversión es exitosa
        "utilidad_si_falla": 10   # Ganancia si la inversión falla
    },
    "Emmanuel": {
        "decisión": "Ahorrar",  # Emmanuel decidió ahorrar
        "probabilidad_sin_info": 0.8,  # Probabilidad de éxito sin información
        "probabilidad_con_info": 0.95,  # Probabilidad de éxito con información adicional
        "utilidad_si_exito": 60,  # Ganancia si el ahorro genera retorno
        "utilidad_si_falla": 20   # Ganancia si no genera retorno
    },
    "Carlos": {
        "decisión": "Gastar",  # Carlos decidió gastar
        "probabilidad_sin_info": 0.6,  # Probabilidad de éxito sin información
        "probabilidad_con_info": 0.85,  # Probabilidad de éxito con información adicional
        "utilidad_si_exito": 50,  # Ganancia si el gasto fue útil
        "utilidad_si_falla": 15   # Ganancia si el gasto no fue útil
    }
}

# Esta función calcula la utilidad esperada dependiendo de la probabilidad y las ganancias
def calcular_utilidad_esperada(probabilidad, utilidad_exito, utilidad_falla):
    """Calcula cuánto se espera ganar tomando en cuenta las probabilidades y utilidades."""
    return (probabilidad * utilidad_exito) + ((1 - probabilidad) * utilidad_falla)

# Esta función calcula el valor de la información adicional
def valor_informacion(probabilidad_sin_info, probabilidad_con_info, utilidad_exito, utilidad_falla):
    """Compara la utilidad esperada con y sin información para saber si la información adicional vale la pena."""
    utilidad_sin_info = calcular_utilidad_esperada(probabilidad_sin_info, utilidad_exito, utilidad_falla)
    utilidad_con_info = calcular_utilidad_esperada(probabilidad_con_info, utilidad_exito, utilidad_falla)
    return utilidad_con_info - utilidad_sin_info  # Valor de la información adicional

# Recorremos cada persona para calcular su utilidad esperada con y sin información
for nombre, info in decisiones.items():
    decision = info["decisión"]
    probabilidad_sin_info = info["probabilidad_sin_info"]
    probabilidad_con_info = info["probabilidad_con_info"]
    utilidad_exito = info["utilidad_si_exito"]
    utilidad_falla = info["utilidad_si_falla"]
    
    # Calculamos el valor de la información adicional
    valor_info = valor_informacion(probabilidad_sin_info, probabilidad_con_info, utilidad_exito, utilidad_falla)
    
    # Imprimimos los resultados
    print(f"{nombre} decidió {decision}. El valor de la información adicional es {valor_info:.2f}.")
