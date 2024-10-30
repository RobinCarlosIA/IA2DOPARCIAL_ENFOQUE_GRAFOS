# Base de conocimiento del agente
hechos = {
    "es_de_dia": True,
    "hay_comida": True,
    "hay_peligro": False
}

# Función que toma decisiones basadas en los hechos
def tomar_decision(hechos):
    # Verificamos si es de día y hay comida
    if hechos["es_de_dia"] and hechos["hay_comida"]:
        decision = "El agente sale a comer."
    elif hechos["es_de_dia"] and not hechos["hay_comida"]:
        decision = "El agente busca comida."
    elif not hechos["es_de_dia"] and not hechos["hay_peligro"]:
        decision = "El agente se queda en casa."
    elif not hechos["es_de_dia"] and hechos["hay_peligro"]:
        decision = "El agente se esconde."
    else:
        decision = "El agente no puede tomar una decisión."

    return decision

# Ejemplo de uso
print("Hechos actuales:")
for hecho, valor in hechos.items():
    print(f"{hecho}: {'Sí' if valor else 'No'}")

# El agente toma una decisión basada en los hechos
decision_agente = tomar_decision(hechos)
print("\nDecisión del agente:")
print(decision_agente)
