# Definimos una función para analizar frases ambiguas
def analizar_frase(frase):
    # Creamos un diccionario con significados de frases ambiguas
    ambiguedades = {
        "Juan vio a Pedro con un telescopio": "Juan usó un telescopio para ver a Pedro.",
        "Juan vio a Pedro con un perro": "Pedro tenía un perro cuando Juan lo vio.",
        "El banco está cerrado": "El banco (entidad financiera) está cerrado.",
        "El banco está cerca del río": "Un banco (lugar para sentarse) está cerca del río."
    }
    
    # Verificamos si la frase está en el diccionario
    if frase in ambiguedades:
        return ambiguedades[frase]  # Devolvemos el significado
    else:
        return "Frase no reconocida."

# Frases a analizar
frases_a_analizar = [
    "Juan vio a Pedro con un telescopio",
    "Juan vio a Pedro con un perro",
    "El banco está cerrado",
    "El banco está cerca del río"
]

# Analizamos cada frase
for frase in frases_a_analizar:
    resultado = analizar_frase(frase)  # Llamamos a la función
    print(f"Frase: '{frase}' - Significado: {resultado}")  # Mostramos el resultado
