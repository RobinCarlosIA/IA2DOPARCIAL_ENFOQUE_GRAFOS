# Definimos una función para calcular la probabilidad condicional.
def probabilidad_condicional(evento_a, evento_b, evento_condicion):
    """
    Calcula la probabilidad condicional P(A|B), que es la probabilidad de A dado B.
    """
    # En este caso, asumimos que tenemos alguna lógica para calcular la probabilidad.
    # Para simplificar, vamos a usar valores fijos:
    if evento_condicion == 'Fernanda':
        if evento_a == 'Emmanuel' and evento_b == 'Emiliano':
            return 0.8  # Ejemplo de probabilidad condicional.
    return 0.1  # Probabilidad por defecto si no se cumplen las condiciones.

# Definimos los nombres.
personas = ['Fernanda', 'Emmanuel', 'Emiliano']

# Mostramos la probabilidad de Emmanuel dado que Fernanda está presente.
evento_a = 'Emmanuel'  # Evento que queremos saber.
evento_b = 'Emiliano'   # Evento condicionante.
evento_condicion = 'Fernanda'  # Condición que se tiene en cuenta.

# Calculamos la probabilidad condicional.
probabilidad = probabilidad_condicional(evento_a, evento_b, evento_condicion)

# Mostramos el resultado.
print(f"La probabilidad de que '{evento_a}' ocurra dado '{evento_condicion}' y '{evento_b}' es: {probabilidad:.2f}")
