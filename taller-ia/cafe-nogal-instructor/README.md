# Material del instructor · Café Nogal

No compartas esta carpeta con los alumnos antes de tiempo.

| Carpeta / archivo | Uso |
| --- | --- |
| `soluciones_ejercicios/` | Soluciones de los dos módulos (con `revisar.py` dan 12 de 12). Compártelas en el repaso de la sesión 2 |
| `sesion2_pasos/chatbot_paso1.py` … `chatbot_paso5.py` | Cómo debe quedar `chatbot.py` al terminar cada paso de la sesión 2 |
| `sesion2_pasos/chatbot_paso6_bonus.py` | Versión final con el bonus (consultar pedidos). Compártela al cierre |
| `sesion2_pasos/probar_chatbot.py` | Paso 6 "rompe el bot": se copia junto a `chatbot.py` y se corre con `python probar_chatbot.py` |

Si un alumno se atrasa en la sesión 2, que copie el archivo del paso actual sobre su `chatbot.py` y siga con el grupo.

## Los pasos de la sesión 2

| Paso | Qué agrega | Lo nuevo de Python |
| --- | --- | --- |
| 1 · La llave | Lee `GEMINI_API_KEY` del archivo `.env` | `import`, variables, `if` |
| 2 · Primera respuesta | `genai.Client` y `generate_content` con `gemini-3.5-flash` | Usar una biblioteca |
| 3 · Conocer el negocio | Instrucción de sistema con `negocio.json` y `productos.csv` | Función `leer_archivo`, f-string largo, diccionario `CONFIG` |
| 4 · Memoria | Reenvía los últimos 20 mensajes | Lista, `for`, `if`, diccionarios |
| 5 · Seguridad y plan B | Reglas firmes, revisa el mensaje antes de gastar, modelo de respaldo | `try / except` |
| 6 · Rompe el bot | `probar_chatbot.py` y reto por equipos | — |
| Bonus | `consultar_pedido` con *function calling* | `csv.DictReader` |

Los pasos 2, 3 y 4 todavía no manejan errores: si Google responde 503 (saturado), la app muestra el error.
Es intencional: el paso 5 lo resuelve y sirve de ejemplo.

## Sobre el modelo

El `.env` usa `MODELO=gemini-3.5-flash` y `MODELO_RESPALDO=gemini-3.5-flash-lite`. Google ya marca
`gemini-3.5-flash` como generación anterior y redirige sus peticiones a Gemini 3.6 Flash, así que sigue
funcionando. Si algún día deja de responder, basta con cambiar el nombre del modelo en el `.env`
(por ejemplo `gemini-3.6-flash`); el código no cambia.

En el bonus, la biblioteca imprime una sola vez el aviso *"Direct use of automatic function calling (AFC)
in Models.generate_content is not recommended"*. Es solo una recomendación: se puede ignorar.
