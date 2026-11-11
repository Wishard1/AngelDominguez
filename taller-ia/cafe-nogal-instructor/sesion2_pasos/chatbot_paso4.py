# =====================================================================
#  ASISTENTE DE CAFÉ NOGAL · PASO 4: MEMORIA
#  Objetivo: que recuerde la plática. La API NO tiene memoria:
#            en cada mensaje le volvemos a mandar los anteriores.
# =====================================================================
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

CARPETA = Path(__file__).parent
load_dotenv(CARPETA / ".env")

LLAVE = os.getenv("GEMINI_API_KEY")
MODELO = os.getenv("MODELO", "gemini-3.5-flash")

cliente = genai.Client(api_key=LLAVE)


def leer_archivo(nombre):
    """Regresa todo el texto de un archivo de la carpeta datos."""
    ruta = CARPETA / "datos" / nombre
    return ruta.read_text(encoding="utf-8")


INSTRUCCIONES = f"""
Eres el asistente virtual de Café Nogal, una cafetería y panadería en Nogales, Sonora.
Atiendes a los clientes por chat. Responde amable y breve (máximo 3 oraciones), sin markdown.

Información del negocio (dirección, horario, pagos y políticas):
{leer_archivo("negocio.json")}

Menú con precios en pesos (disponible: si / no):
{leer_archivo("productos.csv")}

Reglas:
- Usa SOLO esta información. Si no sabes algo, dilo y sugiere llamar al teléfono.
- Si un producto no está disponible, dilo y recomienda otro parecido.
- Solo hablas de temas de la cafetería.
"""

CONFIG = {"system_instruction": INSTRUCCIONES}


# NUEVO: convierte la plática de la app al formato que pide Gemini
def armar_platica(mensaje, historial):
    """historial es una lista de diccionarios: [{"rol": "usuario", "texto": "Hola"}, ...]"""
    platica = []
    for m in historial[-20:]:               # solo los últimos 20 mensajes
        if m["rol"] == "usuario":
            rol = "user"                    # lo dijo el cliente
        else:
            rol = "model"                   # lo dijo la IA
        platica.append({"role": rol, "parts": [{"text": m["texto"]}]})
    platica.append({"role": "user", "parts": [{"text": mensaje}]})   # el mensaje nuevo
    return platica


def responder(mensaje, historial):
    respuesta = cliente.models.generate_content(
        model=MODELO,
        contents=armar_platica(mensaje, historial),     # NUEVO: toda la plática
        config=CONFIG,
    )
    return respuesta.text


if __name__ == "__main__":
    anteriores = [
        {"rol": "usuario", "texto": "Hola, me llamo Ana"},
        {"rol": "modelo", "texto": "¡Hola, Ana! ¿En qué te ayudo?"},
    ]
    print(responder("¿Cómo me llamo?", anteriores))
