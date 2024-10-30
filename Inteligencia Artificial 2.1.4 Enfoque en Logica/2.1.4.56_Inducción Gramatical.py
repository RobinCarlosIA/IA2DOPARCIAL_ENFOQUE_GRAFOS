import random

# Definimos una gramática simple con reglas de producción
gramatica = {
    'S': [['NP', 'VP']],  # Oración = Frase nominal + Frase verbal
    'NP': [['Det', 'N']],  # Frase nominal = Determinante + Nombre
    'VP': [['V', 'NP'], ['V', 'NP', 'PP']],  # Frase verbal = Verbo + Frase nominal (o + Frase preposicional)
    'PP': [['P', 'NP']],  # Frase preposicional = Preposición + Frase nominal
    'Det': [['el'], ['la'], ['un'], ['una']],  # Determinantes
    'N': [['gato'], ['perro'], ['pájaro'], ['ratón']],  # Nombres
    'V': [['come'], ['ve'], ['escucha']],  # Verbos
    'P': [['con'], ['sin'], ['para']]  # Preposiciones
}

# Función para generar una cadena de texto a partir de la gramática
def generar_cadena(simbolo):
    # Si el símbolo es terminal (palabra), lo devolvemos
    if simbolo not in gramatica:
        return simbolo
    # Elegimos una regla de producción aleatoria para el símbolo
    produccion = random.choice(gramatica[simbolo])
    # Generamos cada parte de la producción recursivamente
    return ' '.join(generar_cadena(s) for s in produccion)

# Generamos una frase a partir del símbolo inicial 'S'
frase_generada = generar_cadena('S')

# Mostramos la frase generada
print("Frase generada:", frase_generada)
