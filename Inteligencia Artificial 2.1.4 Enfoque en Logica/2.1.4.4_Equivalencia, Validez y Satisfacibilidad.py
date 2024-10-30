# Importamos lo necesario para trabajar con lógica proposicional
from sympy import symbols, Or, And, Not, simplify

# Definimos las proposiciones lógicas p y q
p, q = symbols('p q')

# Escribimos dos expresiones lógicas
expr1 = And(p, Or(Not(p), q))  # p y (no p o q)
expr2 = And(p, q)              # p y q

# Función para verificar si dos expresiones son equivalentes
def es_equivalente(expr1, expr2):
    # Simplificamos ambas expresiones y comparamos
    return simplify(expr1) == simplify(expr2)

# Función para comprobar si una expresión es válida (siempre verdadera)
def es_valida(expr):
    # Simplificamos la expresión y verificamos si es True
    return simplify(expr) == True

# Función para comprobar si una expresión es satisfacible (alguna vez verdadera)
def es_satisfacible(expr):
    # Verificamos si al simplificar no se vuelve False
    return simplify(expr) != False

# Verificamos equivalencia, validez y satisfacibilidad de las expresiones
print("Expr1 y Expr2 son equivalentes:", es_equivalente(expr1, expr2))
print("Expr1 es válida:", es_valida(expr1))
print("Expr1 es satisfacible:", es_satisfacible(expr1))
print("Expr2 es válida:", es_valida(expr2))
print("Expr2 es satisfacible:", es_satisfacible(expr2))
