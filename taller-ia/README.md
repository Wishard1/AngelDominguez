# Taller · Implementa IA en tus sistemas

Taller para alumnos de nuevo ingreso de Ingeniería en Sistemas Computacionales (Tec de Nogales).
2 sesiones de 2 horas con 15 minutos de descanso.

- **Sesión 1:** Python desde cero (qué es, qué puedes lograr, variables, funciones y lo mínimo para el chatbot),
  ejercicios en clase (completar código y corregir errores), qué es una API y qué puedes lograr con ella.
- **Sesión 2:** construimos paso a paso un chatbot con **Gemini 3.5 Flash** dentro de la app de Café Nogal.

| Archivo | Para quién | Qué es |
| --- | --- | --- |
| `Implementa_IA_en_tus_sistemas.pptx` | Instructor | Presentación de las 2 sesiones (55 diapositivas, con notas) |
| `Manual_del_instructor.pdf` | Instructor | Tiempos, qué decir en cada bloque y problemas comunes |
| `descargas/cafe-nogal.zip` | Alumnos | La app, la hoja de práctica y los ejercicios |
| `descargas/cafe-nogal-instructor.zip` | Instructor | Soluciones y el `chatbot.py` de cada paso |
| `cafe-nogal/` y `cafe-nogal-instructor/` | — | Las mismas carpetas sin comprimir |

## Descarga directa para los alumnos

https://github.com/Wishard1/AngelDominguez/raw/claude/taller-ia-python-apis-txcf21/taller-ia/descargas/cafe-nogal.zip

## Probarlo

```bash
cd cafe-nogal
python -m venv venv
venv\Scripts\activate          # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Para el asistente: copia `.env.example` como `.env`, pega tu llave de https://aistudio.google.com/app/apikey
y copia `cafe-nogal-instructor/sesion2_pasos/chatbot_paso6_bonus.py` sobre `cafe-nogal/chatbot.py`.
