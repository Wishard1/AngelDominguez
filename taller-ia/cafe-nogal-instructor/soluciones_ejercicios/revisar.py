# =====================================================================
#  REVISOR DE LOS EJERCICIOS
#  Ejecutar desde la carpeta ejercicios:   python revisar.py
#  Te dice qué ejercicios están bien y una pista de los que faltan.
#  No necesitas modificar este archivo.
# =====================================================================
import importlib
import io
from contextlib import redirect_stdout


def revisar(nombre_modulo, ejercicios):
    print(f"\n=== {nombre_modulo} ===")
    try:
        modulo = importlib.import_module(nombre_modulo)
    except Exception as error:
        print(f"❌ El archivo no se pudo cargar: {type(error).__name__}: {error}")
        print("   Revisa que no hayas borrado algún paréntesis, comilla o dos puntos.")
        return 0

    bien = 0
    for numero, (funcion, casos, pista) in enumerate(ejercicios, start=1):
        try:
            for argumentos, esperado in casos:
                with redirect_stdout(io.StringIO()):          # oculta los print del alumno
                    obtenido = getattr(modulo, funcion)(*argumentos)
                if obtenido != esperado:
                    raise AssertionError(f"con {argumentos} se esperaba {esperado!r} y salió {obtenido!r}")
            print(f"✅ {numero}. {funcion}")
            bien += 1
        except Exception as error:
            if "___" in str(error) or isinstance(error, NameError):
                print(f"⬜ {numero}. {funcion}: todavía tiene ___ por completar")
                continue
            print(f"❌ {numero}. {funcion}: {error}")
            print(f"   Pista: {pista}")
    print(f"Resultado: {bien} de {len(ejercicios)}")
    return bien


MODULO_1 = [
    ("total_pedido", [((35, 3), 105), ((50, 2), 100)], "Multiplica el precio por la cantidad."),
    ("saludo", [(("Ana",), "Hola, Ana. Bienvenido a Café Nogal")], "Dentro de las llaves va el nombre de la variable."),
    ("tamano_bebida", [((8,), "chico"), ((12,), "mediano"), ((16,), "grande")], "Revisa el número del elif y el texto del else."),
    ("agregar_al_carrito", [((["Concha"], "Capuchino"), ["Concha", "Capuchino"])], "¿Qué método agrega al final de una lista?"),
    ("sumar_precios", [(([35, 50, 15],), 100), (([],), 0)], "En cada vuelta suma el precio actual."),
    ("precio_de", [(({"Concha": 15, "Capuchino": 50}, "Capuchino"), 50)], "La clave es el nombre del producto que recibe la función."),
]

MODULO_2 = [
    ("con_descuento", [((100,), 90.0), ((50,), 45.0)], "10 % no es 10: es 0.10."),
    ("contar_capuchinos", [((["Capuchino", "Concha", "Capuchino"],), 2)], "Fíjate bien en el orden de los signos de la suma."),
    ("ultimo_pedido", [((["P-1", "P-2", "P-3"],), "P-3")], "Las posiciones empiezan en 0. ¿Cuál es la última?"),
    ("total_desde_texto", [(("3", 15), 45)], "Un texto por un número repite el texto. Conviértelo primero."),
    ("mensaje", [(("Luis",), "Hola, Luis")], "print muestra, pero no regresa nada."),
    ("esta_abierto", [((7,), True), ((15,), True), ((20,), False)], "A las 7 en punto ya está abierto."),
]

total = revisar("modulo1_completa", MODULO_1) + revisar("modulo2_corrige", MODULO_2)
print(f"\nTOTAL: {total} de {len(MODULO_1) + len(MODULO_2)}")
if total == len(MODULO_1) + len(MODULO_2):
    print("🎉 ¡Todo bien! Ya estás listo para la sesión 2.")
