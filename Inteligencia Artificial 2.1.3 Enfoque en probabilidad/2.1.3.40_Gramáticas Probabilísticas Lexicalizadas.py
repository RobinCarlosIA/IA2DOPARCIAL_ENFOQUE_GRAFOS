import random

# Definimos las reglas de producción como un diccionario, donde cada regla tiene una probabilidad asociada.
gramatica = {
    'S': [('NP VP', 1.0)],  # La única regla para S, genera un NP seguido de VP
    'NP': [('Det N', 0.5), ('Det N PP', 0.5)],  # NP puede ser Det N o Det N seguido de PP
    'VP': [('V NP', 0.6), ('V PP', 0.4)],  # VP puede ser V seguido de NP o V seguido de PP
    'PP': [('P NP', 1.0)],  # PP es siempre P seguido de NP
    'Det': [('el', 0.5), ('la', 0.5), ('un', 0.5)],  # Determinantes posibles
    'N': [('Fernanda', 0.5), ('Emmanuel', 0.5), ('Emiliano', 0.5)],  # Nombres posibles
    'V': [('juega', 0.5), ('salta', 0.5), ('nada', 0.5)],  # Verbos posibles
    'P': [('sobre', 1.0), ('junto a', 1.0)]  # Preposiciones
}

def generar_cadena(simbolo_inicial):
    # Generamos una cadena a partir del símbolo inicial usando la gramática.
    if simbolo_inicial not in gramatica:
        return simbolo_inicial  # Si es un símbolo terminal, retornamos directamente

    # Elegimos una producción aleatoria según sus probabilidades
    producciones = gramatica[simbolo_inicial]
    total_prob = sum(prob for _, prob in producciones)
    rand = random.uniform(0, total_prob)
    
    acumulado = 0
    for produccion, probabilidad in producciones:
        acumulado += probabilidad
        if rand < acumulado:
            # Generamos la cadena de cada símbolo en la producción
            return ' '.join(generar_cadena(s) for s in produccion.split())

# Generamos una cadena a partir del símbolo inicial 'S'
cadena_generada = generar_cadena('S')
print("Cadena generada:", cadena_generada)
