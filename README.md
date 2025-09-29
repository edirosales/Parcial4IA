# Sistema de Monitoreo Inteligente para Hospitales (Simulación Conceptual)

## 1. Descripción

Este script de Python es una simulación conceptual de un sistema de monitoreo inteligente para pacientes en un entorno hospitalario. El programa demuestra, de manera simplificada, cómo diferentes componentes de Inteligencia Artificial (IA) podrían interactuar para analizar el estado de un paciente, detectar riesgos y generar recomendaciones para el personal médico en tiempo real.

**Aviso:** Este código es una demostración con fines educativos y **no debe ser utilizado en un entorno clínico real**. Los modelos de IA son simulados con lógica simple.

## 2. Características Simuladas

El sistema integra cuatro componentes principales de IA de forma simulada:

* **Lógica Difusa:** La función `analyze_vitals_fuzzy` evalúa los signos vitales del paciente (frecuencia cardíaca, temperatura) usando reglas flexibles para determinar un nivel de riesgo (bajo, medio, alto).
* **Visión Artificial:** La función `computer_vision_analysis` simula el análisis de una cámara en la habitación para detectar eventos críticos, como una posible caída del paciente.
* **Machine Learning Predictivo:** La función `predict_complications_ml` simula un modelo predictivo que analiza el historial médico del paciente en conjunto con sus signos vitales actuales para anticipar posibles complicaciones.
* **Sistema Experto:** La función `expert_system_recommendation` actúa como el módulo central de decisión. Recopila las evaluaciones de los otros componentes y, basándose en un conjunto de reglas de prioridad, genera un informe final con una acción sugerida para el personal médico.

## 3. Estructura del Código

El script está organizado en las siguientes secciones:

* **Clase `Patient`:** Define la estructura de datos para un paciente, incluyendo su información básica, historial médico y los datos de los sensores que se actualizan dinámicamente.
* **Módulos de IA (Simulados):** Conjunto de funciones (`analyze_vitals_fuzzy`, `computer_vision_analysis`, `predict_complications_ml`, `expert_system_recommendation`) que representan cada una de las técnicas de IA. Cada función recibe el objeto `patient` y devuelve un análisis.
* **Bucle Principal de Monitoreo (`main`)**:
    1.  Crea una instancia de un paciente de prueba.
    2.  Inicia un bucle infinito que se ejecuta cada 5 segundos.
    3.  En cada iteración, actualiza los signos vitales del paciente para simular fluctuaciones.
    4.  Llama a cada función de análisis de IA.
    5.  Pasa los resultados al sistema experto para obtener una recomendación consolidada.
    6.  Imprime el estado del paciente y la recomendación final en la consola.

## 4. Cómo Ejecutar el Programa

1.  Asegúrate de tener Python 3 instalado en tu sistema.
2.  Guarda el código en un archivo llamado `hospital_monitoring_system.py`.
3.  Abre una terminal o línea de comandos.
4.  Navega hasta el directorio donde guardaste el archivo.
6.  El programa comenzará a imprimir el estado del paciente y las recomendaciones cada 5 segundos.
