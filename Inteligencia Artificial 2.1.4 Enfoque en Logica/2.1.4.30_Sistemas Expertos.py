# Definimos una clase para el Sistema Experto
class SistemaExperto:
    def __init__(self):
        self.diagnosticos = {
            "fiebre": "Podrías tener una infección, consulta a un médico.",
            "tos": "Podrías tener un resfriado o alergias.",
            "dolor_de_cabeza": "Podría ser tensión o deshidratación.",
            "sin_sintomas": "Estás saludable, sigue cuidándote."
        }

    # Método para hacer preguntas y obtener un diagnóstico
    def hacer_preguntas(self):
        print("Responde las siguientes preguntas (Sí/No):")
        
        # Preguntamos si tiene fiebre
        fiebre = input("¿Tienes fiebre? ").strip().lower() == 'sí'
        
        # Preguntamos si tiene tos
        tos = input("¿Tienes tos? ").strip().lower() == 'sí'
        
        # Preguntamos si tiene dolor de cabeza
        dolor_de_cabeza = input("¿Tienes dolor de cabeza? ").strip().lower() == 'sí'

        # Evaluamos las respuestas para diagnosticar
        if fiebre:
            print(self.diagnosticos["fiebre"])
        elif tos:
            print(self.diagnosticos["tos"])
        elif dolor_de_cabeza:
            print(self.diagnosticos["dolor_de_cabeza"])
        else:
            print(self.diagnosticos["sin_sintomas"])

# Creamos una instancia del sistema experto
sistema = SistemaExperto()

# Llamamos al método para hacer preguntas y obtener un diagnóstico
sistema.hacer_preguntas()
