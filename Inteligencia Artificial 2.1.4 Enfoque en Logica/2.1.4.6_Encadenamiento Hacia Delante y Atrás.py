# Base de conocimiento: hechos y reglas
hechos = {"A"}  # Sabemos que A es verdadero
reglas = {
    "A implica B": ("A", "B"),  # Si A es verdadero, entonces B también lo es
    "B implica C": ("B", "C")   # Si B es verdadero, entonces C también lo es
}

# Función de encadenamiento hacia adelante
def encadenamiento_hacia_adelante(hechos, reglas, objetivo):
    # Continuamos mientras haya reglas que aplicar
    while True:
        nuevo_hecho = False
        for regla, (condicion, conclusion) in reglas.items():
            # Si la condición está en los hechos y la conclusión no está, agregamos la conclusión
            if condicion in hechos and conclusion not in hechos:
                hechos.add(conclusion)
                nuevo_hecho = True
                print(f"Aplicando {regla}: Ahora sabemos que {conclusion} es verdadero.")
                if conclusion == objetivo:
                    return True  # Objetivo alcanzado
        if not nuevo_hecho:
            break  # No hay nuevos hechos para agregar
    return objetivo in hechos  # Retorna si el objetivo fue alcanzado

# Función de encadenamiento hacia atrás
def encadenamiento_hacia_atras(hechos, reglas, objetivo):
    # Si el objetivo ya está en los hechos, retornamos True
    if objetivo in hechos:
        return True
    # Buscamos reglas que concluyan en el objetivo
    for regla, (condicion, conclusion) in reglas.items():
        if conclusion == objetivo:
            print(f"Revisando {regla}: ¿Podemos probar que {condicion} es verdadero?")
            # Verificamos si la condición se puede demostrar recursivamente
            if encadenamiento_hacia_atras(hechos, reglas, condicion):
                hechos.add(objetivo)
                print(f"{objetivo} es verdadero porque {condicion} lo es.")
                return True
    return False  # No se pudo demostrar el objetivo

# Definimos el objetivo a probar
objetivo = "C"

# Encadenamiento hacia adelante
print("Encadenamiento hacia adelante:")
if encadenamiento_hacia_adelante(hechos.copy(), reglas, objetivo):
    print(f"Se logró el objetivo: {objetivo} es verdadero.")
else:
    print(f"No se logró el objetivo: {objetivo} no se pudo demostrar.")

# Encadenamiento hacia atrás
print("\nEncadenamiento hacia atrás:")
if encadenamiento_hacia_atras(hechos.copy(), reglas, objetivo):
    print(f"Se logró el objetivo: {objetivo} es verdadero.")
else:
    print(f"No se logró el objetivo: {objetivo} no se pudo demostrar.")
