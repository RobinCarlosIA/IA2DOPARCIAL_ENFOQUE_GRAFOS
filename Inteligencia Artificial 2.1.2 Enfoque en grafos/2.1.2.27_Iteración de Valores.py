# Definimos las decisiones de cada persona (Fernanda, Emmanuel y Carlos) y sus recompensas iniciales.
decisiones = {
    "Fernanda": {
        "decisión": "Invertir",  # Fernanda decidió invertir
        "recompensa": 80  # La recompensa inicial de Fernanda por su decisión
    },
    "Emmanuel": {
        "decisión": "Ahorrar",  # Emmanuel decidió ahorrar
        "recompensa": 60  # La recompensa inicial de Emmanuel
    },
    "Carlos": {
        "decisión": "Gastar",  # Carlos decidió gastar
        "recompensa": 50  # La recompensa inicial de Carlos
    }
}

# Función para realizar la iteración de valores y actualizar las recompensas paso a paso
def iterar_valores(decisiones, iteraciones, factor_descuento):
    """Ajusta las recompensas en cada iteración, considerando un factor de descuento."""
    for i in range(iteraciones):
        print(f"\nIteración {i+1}")
        for nombre, info in decisiones.items():
            recompensa_actual = info["recompensa"]
            nueva_recompensa = recompensa_actual * factor_descuento  # Se ajusta el valor con un descuento
            info["recompensa"] = nueva_recompensa  # Actualizamos la recompensa
            
            # Mostramos el valor actualizado para cada persona
            print(f"{nombre} decidió {info['decisión']} y ahora tiene una recompensa ajustada de {nueva_recompensa:.2f}.")

# Parámetros: Número de iteraciones y factor de descuento (cómo disminuye el valor cada vez)
iteraciones = 5  # Vamos a iterar 5 veces
factor_descuento = 0.9  # Factor de descuento del 90% en cada iteración

# Llamamos a la función para ajustar las recompensas
iterar_valores(decisiones, iteraciones, factor_descuento)
