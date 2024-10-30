# Importamos sympy para manejar expresiones lógicas
from sympy import symbols, Or, And, Not, to_cnf

# Definimos las proposiciones lógicas
p, q = symbols('p q')

# Escribimos una expresión lógica
expr = Or(And(p, Not(q)), And(Not(p), q))  # (p y no q) o (no p y q)

# Convertimos la expresión a Forma Normal Conjuntiva (FNC)
fnc = to_cnf(expr, simplify=True)  # Convierte expr a FNC
print("Forma Normal Conjuntiva de la expresión:", fnc)

# Ejemplo de resolución básica entre dos cláusulas
clausula1 = p  # Primera cláusula: p
clausula2 = Not(p)  # Segunda cláusula: no p
resolucion = Or(clausula1, clausula2)  # Resolvemos usando OR
print("Resultado de la resolución entre cláusula1 y cláusula2:", resolucion)
