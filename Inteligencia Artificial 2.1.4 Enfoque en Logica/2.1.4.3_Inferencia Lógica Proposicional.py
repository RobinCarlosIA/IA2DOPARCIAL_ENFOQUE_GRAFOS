# Definimos una función para hacer inferencias lógicas
def inferencia_logica(p, q):
    # Imprimimos los valores de p y q
    print(f"p: {p}, q: {q}")
    
    # Inferimos usando la lógica proposicional
    if p and q:  # Si p y q son verdaderos
        return "Ambos son verdaderos"
    elif p and not q:  # Si p es verdadero y q es falso
        return "p es verdadero, q es falso"
    elif not p and q:  # Si p es falso y q es verdadero
        return "p es falso, q es verdadero"
    else:  # Si ambos son falsos
        return "Ambos son falsos"

# Probamos con diferentes combinaciones de p y q
resultados = []

# Combinación 1: p verdadero, q verdadero
resultados.append(inferencia_logica(True, True))

# Combinación 2: p verdadero, q falso
resultados.append(inferencia_logica(True, False))

# Combinación 3: p falso, q verdadero
resultados.append(inferencia_logica(False, True))

# Combinación 4: p falso, q falso
resultados.append(inferencia_logica(False, False))

# Mostramos todos los resultados
print("\nResultados de las inferencias:")
for resultado in resultados:
    print(resultado)
