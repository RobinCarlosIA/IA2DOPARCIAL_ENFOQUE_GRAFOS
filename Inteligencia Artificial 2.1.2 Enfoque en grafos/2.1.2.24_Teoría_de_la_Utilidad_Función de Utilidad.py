# Función para calcular la utilidad de una decisión
def calcular_utilidad(decision, valor):
    """Calcula qué tan útil es una decisión para una persona según su valor."""
    return valor * 10  # Aquí, la utilidad es el valor de la decisión multiplicado por 10.

# Decisiones que tomaron Fernanda, Emmanuel y Carlos y sus respectivos valores
decisiones = {
    "Fernanda": {"decisión": "Invertir", "valor": 8},  # Fernanda tomó la decisión de invertir con un valor de 8.
    "Emmanuel": {"decisión": "Ahorrar", "valor": 6},  # Emmanuel decidió ahorrar con un valor de 6.
    "Carlos": {"decisión": "Gastar", "valor": 5}      # Carlos decidió gastar con un valor de 5.
}

# Cálculo de la utilidad para cada persona
for nombre, info in decisiones.items():
    decision = info["decisión"]
    valor = info["valor"]
    utilidad = calcular_utilidad(decision, valor)  # Calculamos la utilidad de la decisión.
    print(f"{nombre} tomó la decisión de {decision} con una utilidad de {utilidad}.")
