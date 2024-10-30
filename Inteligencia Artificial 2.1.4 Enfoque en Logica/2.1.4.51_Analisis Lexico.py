import re

# Definimos una función para realizar el análisis léxico
def analisis_lexico(codigo):
    # Definimos patrones para palabras clave, identificadores y números
    patron_clave = r'\b(if|else|while|return|function)\b'  # Palabras clave
    patron_identificador = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'   # Identificadores
    patron_numero = r'\b\d+\b'                              # Números

    # Buscamos las palabras clave en el código
    claves = re.findall(patron_clave, codigo)
    
    # Buscamos los identificadores en el código
    identificadores = re.findall(patron_identificador, codigo)
    
    # Buscamos los números en el código
    numeros = re.findall(patron_numero, codigo)

    # Devolvemos los resultados
    return claves, identificadores, numeros

# Un ejemplo de código para analizar
codigo_ejemplo = """
function suma(a, b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}
"""

# Realizamos el análisis léxico
claves, identificadores, numeros = analisis_lexico(codigo_ejemplo)

# Mostramos los resultados
print("Palabras clave encontradas:", claves)
print("Identificadores encontrados:", identificadores)
print("Números encontrados:", numeros)
