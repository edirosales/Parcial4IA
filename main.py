import random
import time

class Patient:
    def __init__(self, patient_id, name, age, medical_history):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = medical_history
        
        self.heart_rate = random.randint(55, 105)
        self.temperature = round(random.uniform(36.5, 37.5), 1)
        self.position = "acostado"

    def update_vitals(self):
        self.heart_rate += random.randint(-5, 5)
        self.temperature += round(random.uniform(-0.2, 0.2), 1)
        if self.heart_rate < 40 or self.heart_rate > 130:
             self.heart_rate = 80
        if random.random() < 0.05:
            self.position = "en el suelo"

    def display_info(self):
        return (f"ID: {self.patient_id} | Nombre: {self.name} | FC: {self.heart_rate} bpm | "
                f"Temp: {self.temperature}°C | Posición: {self.position}")


def analyze_vitals_fuzzy(patient):
    risk_level = "bajo"
    reason = "Signos vitales estables."
    if patient.heart_rate > 110 or patient.heart_rate < 50:
        risk_level = "alto"
        reason = "Frecuencia cardíaca anómala."
    elif patient.temperature > 38.5:
        risk_level = "alto"
        reason = "Fiebre alta detectada."
    elif patient.heart_rate > 100 or patient.temperature > 37.8:
        risk_level = "medio"
        reason = "Frecuencia cardíaca o temperatura ligeramente elevadas."
        
    return risk_level, reason

def computer_vision_analysis(patient):
    if patient.position == "en el suelo":
        return "crítico", "¡POSIBLE CAÍDA DETECTADA!"
    return "bajo", "Posición normal."

def predict_complications_ml(patient):
    if "diabetes" in patient.medical_history and patient.temperature > 38.0:
        return "alto", "Riesgo de complicación diabética por fiebre."
    if "hipertensión" in patient.medical_history and patient.heart_rate > 110:
        return "alto", "Riesgo de crisis hipertensiva."
    return "bajo", "Sin predicciones de riesgo basadas en historial."

def expert_system_recommendation(risk_levels):
    recommendations = [msg for level, msg in risk_levels.values() if level != "bajo"]
    
    if any(level == "crítico" for level, msg in risk_levels.values()):
        final_priority = "¡URGENTE!"
        action = "Enviar personal médico inmediatamente a la habitación."
    elif any(level == "alto" for level, msg in risk_levels.values()):
        final_priority = "ALERTA ALTA"
        action = "Notificar a enfermería para una revisión prioritaria."
    elif any(level == "medio" for level, msg in risk_levels.values()):
        final_priority = "AVISO"
        action = "Agendar revisión de rutina en la próxima hora."
    else:
        return "Estado del paciente: Estable. No se requieren acciones."

    return f"Prioridad: {final_priority}\n  Motivos: {'; '.join(recommendations)}\n  Acción Sugerida: {action}"

def main():
    patient1 = Patient(patient_id="101", name="Edgar Rosales", age=20, medical_history=["diabetes", "hipertensión"])
    
    print("--- INICIANDO SISTEMA DE MONITOREO INTELIGENTE ---")
    
    try:
        while True:
            patient1.update_vitals()
            print("\n" + ("-"*80))
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Monitoreando paciente...")
            print(patient1.display_info())

            risk_levels = {
                "vitals": analyze_vitals_fuzzy(patient1),
                "vision": computer_vision_analysis(patient1),
                "prediction": predict_complications_ml(patient1)
            }
            
            recommendation = expert_system_recommendation(risk_levels)
            
            print("\n--- RECOMENDACIÓN DEL SISTEMA ---")
            print(recommendation)
            print("-" * 80)
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n--- SISTEMA DE MONITOREO DETENIDO ---")

if __name__ == "__main__":
    main()