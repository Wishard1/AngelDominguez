# =====================================================================
#  ASISTENTE DE CAFÉ NOGAL · PASO 1: LA LLAVE
#  Objetivo: que Python lea la llave del archivo .env
#            (la llave NUNCA se escribe dentro del código).
#  Probar:   python chatbot.py
# =====================================================================
import os                               # para leer variables del sistema
from pathlib import Path                # para ubicar archivos
from dotenv import load_dotenv          # para leer el archivo .env

CARPETA = Path(__file__).parent         # la carpeta donde vive este archivo
load_dotenv(CARPETA / ".env")           # lee el archivo .env

LLAVE = os.getenv("GEMINI_API_KEY")                 # la llave
MODELO = os.getenv("MODELO", "gemini-3.5-flash")    # el modelo de IA


def responder(mensaje, historial):
    """Recibe la pregunta del cliente y regresa la respuesta."""
    return None                         # todavía no responde nada


# Esto solo corre cuando escribes "python chatbot.py"
if __name__ == "__main__":
    if LLAVE:
        print("¡Llave encontrada! Modelo:", MODELO)
    else:
        print("No encontré la llave. Revisa que el archivo se llame .env")
