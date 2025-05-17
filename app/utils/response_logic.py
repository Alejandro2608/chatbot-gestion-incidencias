import json
import os

# Ruta absoluta al archivo respuestas.json
RESPUESTAS_PATH = os.path.join(os.path.dirname(__file__), '..', 'respuestas.json')

# Cargar respuestas desde el JSON
def cargar_respuestas():
    try:
        with open(RESPUESTAS_PATH, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except Exception as e:
        print(f"❌ Error al cargar respuestas: {e}")
        return []

# Normaliza texto (opcional: mejora la búsqueda)
def limpiar_texto(texto):
    return texto.strip().lower()

# Función principal para obtener la respuesta del chatbot
def obtener_respuesta(pregunta_usuario: str) -> str | None:
    pregunta_usuario = limpiar_texto(pregunta_usuario)
    respuestas = cargar_respuestas()

    for item in respuestas:
        pregunta_guardada = limpiar_texto(item.get("pregunta", ""))
        if pregunta_guardada in pregunta_usuario or pregunta_usuario in pregunta_guardada:
            return item.get("respuesta")
    
    return None  # No se encontró respuesta
