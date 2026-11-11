# =====================================================================
#  ASISTENTE DE CAFÉ NOGAL · PASO 3: CONOCER EL NEGOCIO
#  Objetivo: darle personalidad, reglas y los datos reales del negocio
#            (menú, precios, horario) con una "instrucción de sistema".
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


# NUEVO: una función que lee un archivo de la carpeta datos
def leer_archivo(nombre):
    """Regresa todo el texto de un archivo de la carpeta datos."""
    ruta = CARPETA / "datos" / nombre
    return ruta.read_text(encoding="utf-8")


# NUEVO: el "manual del empleado" que la IA lee antes de contestar
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

# NUEVO: la configuración de cada petición
CONFIG = {"system_instruction": INSTRUCCIONES}


def responder(mensaje, historial):
    respuesta = cliente.models.generate_content(
        model=MODELO,
        contents=mensaje,
        config=CONFIG,                # NUEVO: las instrucciones
    )
    return respuesta.text


if __name__ == "__main__":
    print(responder("¿Cuánto cuesta un capuchino?", []))
