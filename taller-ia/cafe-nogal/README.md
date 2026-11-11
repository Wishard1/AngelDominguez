# Café Nogal · Panel con asistente de IA

App del taller **Implementa IA en tus sistemas** (Tec de Nogales). Es el panel de una cafetería hecho solo
con Python: resumen de ventas, menú, pedidos, el dólar del día (una API real) y un **asistente con IA**
(Gemini 3.5 Flash) que construimos juntos en la sesión 2.

## 1. Instalar y abrir

1. Instala **Python** (python.org, marca la casilla *Add python.exe to PATH*), **Visual Studio Code** y, dentro de VS Code,
   la extensión **Python** de Microsoft ( → busca "Python" → Install).
2. Descomprime esta carpeta y ábrela en VS Code: *Archivo → Abrir carpeta…*
3. Abre la terminal: *Terminal → Nueva terminal*
4. Escribe, una línea a la vez:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

En Mac o Linux, la segunda línea es `source venv/bin/activate`.

La app se abre sola en el navegador (http://localhost:8501). Para detenerla: `Ctrl + C` en la terminal.

## 2. Qué hay en la carpeta

| Archivo | Qué es |
| --- | --- |
| `practica.py` | Tu hoja para probar los ejemplos de Python de la sesión 1 |
| `ejercicios/` | Ejercicios de Python: completar el código y corregir errores |
| `app.py` | La app: páginas, gráficas y tablas (no necesitas cambiarla) |
| `chatbot.py` | El asistente: está vacío, lo construimos en la sesión 2 |
| `datos/` | Información del negocio, menú, ventas y pedidos |
| `.env.example` | Plantilla para tu llave de la IA (sesión 2) |

## 3. Ejercicios (sesión 1)

```bash
cd ejercicios
python revisar.py
```

`revisar.py` te dice qué ejercicios están bien (✅), cuáles faltan (⬜) y te da una pista en los que tienen error (❌).
Hazlos sin inteligencia artificial: el chiste es entrenar el ojo.

## 4. Antes de la sesión 2: tu llave de Gemini

1. Entra a https://aistudio.google.com/app/apikey con tu cuenta de Google y crea una llave (es gratis).
2. Copia el archivo `.env.example` y renómbralo a **`.env`** (sin nada más).
3. Pega tu llave después de `GEMINI_API_KEY=`

**Nunca** subas el `.env` a GitHub ni compartas tu llave: es como tu contraseña.
