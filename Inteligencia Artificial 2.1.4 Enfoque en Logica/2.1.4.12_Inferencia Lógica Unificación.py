# Función que intenta unificar dos términos
def unificar(term1, term2):
    # Si ambos términos son iguales, la unificación es exitosa
    if term1 == term2:
        return True
    
    # Si uno de los términos es una variable, lo unificamos con el otro término
    if is_variable(term1) or is_variable(term2):
        return True  # La unificación es posible con la variable
    
    # Si los términos son diferentes y ninguno es una variable, no se pueden unificar
    return False

# Función que verifica si un término es una variable
def is_variable(term):
    return term.islower()  # Consideramos que las variables son letras minúsculas

# Ejemplos de uso
term_a = "X"  # Variable
term_b = "f(a, b)"  # Término más complejo
term_c = "f(a, b)"  # Otro término complejo igual

# Intentamos unificar diferentes pares de términos
print("Unificación de", term_a, "y", term_b, ":", unificar(term_a, term_b))  # True
print("Unificación de", term_b, "y", term_c, ":", unificar(term_b, term_c))  # True
print("Unificación de", term_b, "y", "g(a)", ":", unificar(term_b, "g(a)"))  # False
