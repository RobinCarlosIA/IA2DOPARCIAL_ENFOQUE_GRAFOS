import random

# Definimos una gramática simple de tipo 0
# Usamos reglas de producción para generar cadenas
gramatica = {
    'S': ['AB', 'aA', 'bB'],  # Regla de inicio
    'A': ['aA', 'a'],         # 'A' puede producir 'a' seguido de 'A' o solo 'a'
    'B': ['bB', 'b'],         # 'B' puede producir 'b' seguido de 'B' o solo 'b'
}

# Función para generar una cadena a partir de la gramática
def generar_cadena(simbolo):
    # Si el símbolo es una terminal, lo devolvemos
    if simbolo not in gramatica:
        return simbolo
    
    # Elegimos una regla de producción al azar
    produccion = random.choice(gramatica[simbolo])
    
    # Generamos la cadena a partir de la producción seleccionada
    return ''.join(generar_cadena(s) for s in produccion)

# Generamos una cadena a partir del símbolo inicial 'S'
cadena_generada = generar_cadena('S')

# Mostramos la cadena generada
print("Cadena Generada:", cadena_generada)
