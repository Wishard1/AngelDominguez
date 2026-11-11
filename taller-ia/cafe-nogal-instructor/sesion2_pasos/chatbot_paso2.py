# =====================================================================
#  ASISTENTE DE CAFÉ NOGAL · PASO 2: PRIMERA RESPUESTA
#  Objetivo: mandar la pregunta a Gemini y regresar su respuesta.
#  Probar:   python chatbot.py   y luego   streamlit run app.py
# =====================================================================
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai                # NUEVO: la biblioteca de Gemini

CARPETA = Path(__file__).parent
load_dotenv(CARPETA / ".env")

LLAVE = os.getenv("GEMINI_API_KEY")
MODELO = os.getenv("MODELO", "gemini-3.5-flash")

cliente = genai.Client(api_key=LLAVE)   # NUEVO: la conexión con la API


def responder(mensaje, historial):
    """Recibe la pregunta del cliente y regresa la respuesta."""
    respuesta = cliente.models.generate_content(    # NUEVO: la petición
        model=MODELO,                   # qué modelo usar
        contents=mensaje,               # qué le preguntamos
    )
    return respuesta.text               # solo el texto de la respuesta


if __name__ == "__main__":
    print(responder("Hola, ¿quién eres?", []))
