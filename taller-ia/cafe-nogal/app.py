# =====================================================================
#  PANEL DE CAFÉ NOGAL — una app web hecha solo con Python
#
#  Ejecutar (con el entorno activado):
#      streamlit run app.py
#  Se abre sola en el navegador: http://localhost:8501
#
#  Todo lo que usa este archivo lo vimos en el curso de Python:
#  variables, listas, diccionarios, if, for, funciones e import.
# =====================================================================
import csv
import json
import urllib.request
from pathlib import Path

import streamlit as st   # la biblioteca que convierte este archivo en página web

import chatbot           # nuestro archivo chatbot.py (lo construimos en la sesión 2)

CARPETA_DATOS = Path(__file__).parent / "datos"

st.set_page_config(page_title="Café Nogal · Panel", page_icon="☕", layout="wide")


# ------------------------------------------------------------------
# 1. LEER LOS DATOS DEL NEGOCIO
# ------------------------------------------------------------------
def leer_csv(nombre_archivo):
    """Lee un archivo CSV y regresa una lista de diccionarios (una por fila)."""
    with open(CARPETA_DATOS / nombre_archivo, encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def leer_negocio():
    """Lee la información general del negocio (nombre, horario, políticas...)."""
    with open(CARPETA_DATOS / "negocio.json", encoding="utf-8") as archivo:
        return json.load(archivo)


negocio = leer_negocio()
productos = leer_csv("productos.csv")
ventas = leer_csv("ventas.csv")
pedidos = leer_csv("pedidos.csv")

# Los CSV guardan todo como texto: convertimos los números
for v in ventas:
    v["cantidad"] = int(v["cantidad"])
    v["total"] = int(v["total"])
for p in productos:
    p["precio"] = int(p["precio"])


# ------------------------------------------------------------------
# 2. UNA API REAL: EL TIPO DE CAMBIO DEL DÍA
# ------------------------------------------------------------------
@st.cache_data(ttl=3600)   # guarda el resultado 1 hora para no llamar a la API a cada rato
def obtener_tipo_de_cambio():
    """Pide a una API pública cuántos pesos vale un dólar. Si no hay internet, regresa None."""
    url = "https://api.frankfurter.dev/v1/latest?base=USD&symbols=MXN"
    peticion = urllib.request.Request(url, headers={"User-Agent": "CafeNogal/1.0"})   # quién pregunta
    try:
        with urllib.request.urlopen(peticion, timeout=5) as respuesta:
            datos = json.loads(respuesta.read())   # el JSON se convierte en diccionario
        return datos["rates"]["MXN"]          # {"base": "USD", "rates": {"MXN": 18.4}}
    except Exception:
        return None


# ------------------------------------------------------------------
# 3. MENÚ LATERAL
# ------------------------------------------------------------------
with st.sidebar:
    st.title(f"☕ {negocio['nombre']}")
    st.caption(negocio["giro"])
    pagina = st.radio("Secciones", ["Inicio", "Ventas", "Menú", "Pedidos", "Asistente"])
    st.divider()
    dolar = obtener_tipo_de_cambio()
    if dolar:
        st.metric("Dólar hoy", f"${dolar:.2f} MXN")
    else:
        st.caption("Tipo de cambio no disponible (sin internet)")


# ------------------------------------------------------------------
# 4. PÁGINAS
# ------------------------------------------------------------------
def pagina_inicio():
    st.title("Resumen de la semana")

    total_semana = sum(v["total"] for v in ventas)
    piezas = sum(v["cantidad"] for v in ventas)
    pendientes = [p for p in pedidos if p["estado"] != "Entregado"]

    # Producto más vendido: sumamos piezas por producto en un diccionario
    por_producto = {}
    for v in ventas:
        nombre = v["producto"]
        anterior = por_producto.get(nombre, 0)       # 0 si todavía no está en el diccionario
        por_producto[nombre] = anterior + v["cantidad"]
    estrella = max(por_producto, key=por_producto.get)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Ventas de la semana", f"${total_semana:,}")
    col2.metric("Productos vendidos", f"{piezas:,}")
    col3.metric("Pedidos pendientes", len(pendientes))
    col4.metric("Más vendido", estrella)

    st.subheader("Ventas por día")
    por_dia = {}
    for v in ventas:
        por_dia[v["fecha"]] = por_dia.get(v["fecha"], 0) + v["total"]
    st.bar_chart([{"Día": d, "Ventas ($)": t} for d, t in por_dia.items()], x="Día", y="Ventas ($)")

    st.subheader("Pedidos pendientes")
    st.dataframe(pendientes, width="stretch", hide_index=True)


def pagina_ventas():
    st.title("Ventas por producto")
    por_producto = {}
    for v in ventas:
        por_producto[v["producto"]] = por_producto.get(v["producto"], 0) + v["total"]
    filas = sorted(
        [{"Producto": p, "Ventas ($)": t} for p, t in por_producto.items()],
        key=lambda fila: fila["Ventas ($)"],
        reverse=True,
    )
    st.bar_chart(filas, x="Producto", y="Ventas ($)", horizontal=True)
    st.dataframe(filas, width="stretch", hide_index=True)


def pagina_menu():
    st.title("Menú")
    categorias = sorted({p["categoria"] for p in productos})
    elegida = st.selectbox("Categoría", ["Todas"] + categorias)
    for p in productos:
        if elegida == "Todas" or p["categoria"] == elegida:
            estado = "✅ Disponible" if p["disponible"] == "si" else "❌ Agotado"
            st.write(f"**{p['producto']}** · ${p['precio']} · {estado}")


def pagina_pedidos():
    st.title("Pedidos")
    estados = sorted({p["estado"] for p in pedidos})
    elegidos = st.multiselect("Filtrar por estado", estados, default=estados)
    st.dataframe([p for p in pedidos if p["estado"] in elegidos], width="stretch", hide_index=True)


def pagina_asistente():
    st.title("💬 Asistente para clientes")
    st.caption("Responde dudas sobre el menú, precios, horarios y el estado de los pedidos.")

    # La plática se guarda mientras la página esté abierta
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

    if st.button("Nueva plática"):
        st.session_state.mensajes = []

    for m in st.session_state.mensajes:
        with st.chat_message("user" if m["rol"] == "usuario" else "assistant"):
            st.write(m["texto"])

    pregunta = st.chat_input("Escribe la pregunta del cliente…")
    if pregunta:
        with st.chat_message("user"):
            st.write(pregunta)

        # Aquí la app le pasa la pregunta al chatbot (chatbot.py)
        respuesta = chatbot.responder(pregunta, st.session_state.mensajes)

        if respuesta is None:
            st.info("El asistente todavía no está conectado. Lo construimos en la sesión 2, dentro de chatbot.py.")
        else:
            with st.chat_message("assistant"):
                st.write(respuesta)
            st.session_state.mensajes.append({"rol": "usuario", "texto": pregunta})
            st.session_state.mensajes.append({"rol": "modelo", "texto": respuesta})


# Mostrar la página elegida en el menú
if pagina == "Inicio":
    pagina_inicio()
elif pagina == "Ventas":
    pagina_ventas()
elif pagina == "Menú":
    pagina_menu()
elif pagina == "Pedidos":
    pagina_pedidos()
else:
    pagina_asistente()
