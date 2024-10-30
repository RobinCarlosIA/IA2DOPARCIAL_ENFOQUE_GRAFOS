# Definimos una función para calcular la probabilidad usando la Regla de Bayes.
def regla_de_bayes(probabilidad_a_dado_b, probabilidad_b, probabilidad_a):
    """
    Calcula la probabilidad P(B|A) usando la Regla de Bayes.
    P(B|A) = (P(A|B) * P(B)) / P(A)
    """
    # Aplicamos la fórmula de Bayes.
    return (probabilidad_a_dado_b * probabilidad_b) / probabilidad_a

# Definimos las probabilidades.
# Supongamos que:
# P(A|B) = Probabilidad de que ocurra 'Emmanuel' dado 'Fernanda'.
probabilidad_emmanuel_dado_fernanda = 0.9  # 90%
# P(B) = Probabilidad de que ocurra 'Fernanda'.
probabilidad_fernanda = 0.6  # 60%
# P(A) = Probabilidad de que ocurra 'Emmanuel'.
probabilidad_emmanuel = 0.7  # 70%

# Calculamos la probabilidad de que ocurra 'Fernanda' dado que 'Emmanuel' ha ocurrido.
probabilidad_fernanda_dado_emmanuel = regla_de_bayes(probabilidad_emmanuel_dado_fernanda, probabilidad_fernanda, probabilidad_emmanuel)

# Mostramos el resultado.
print(f"La probabilidad de que ocurra 'Fernanda' dado que ha ocurrido 'Emmanuel' es: {probabilidad_fernanda_dado_emmanuel:.2f}")
