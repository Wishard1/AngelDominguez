# =====================================================================
#  EJERCICIOS · MÓDULO 2: CORRIGE EL ERROR (SOLUCIÓN)
#
#  Cada función tiene UN error. El código corre, pero hace algo
#  distinto a lo que dice su comentario (o truena al usarlo).
#  Encuentra el error, corrígelo y explica en un comentario qué estaba mal.
#
#  Para revisar tu avance:   python revisar.py
#  Pista: lee el mensaje de error de abajo hacia arriba.
# =====================================================================


# Error 1
# Aplica un descuento de 10 % al precio.
# Ejemplo: con_descuento(100)  ->  90.0
def con_descuento(precio):
    return precio - precio * 0.10   # 10 % es 0.10, no 10


# Error 2
# Cuenta cuántas veces aparece "Capuchino" en la lista de pedidos.
# Ejemplo: contar_capuchinos(["Capuchino", "Concha", "Capuchino"])  ->  2
def contar_capuchinos(pedidos):
    cuenta = 0
    for producto in pedidos:
        if producto == "Capuchino":
            cuenta += 1   # =+ asignaba 1 en cada vuelta
    return cuenta


# Error 3
# Regresa el último pedido de la lista.
# Ejemplo: ultimo_pedido(["P-1", "P-2", "P-3"])  ->  "P-3"
def ultimo_pedido(pedidos):
    return pedidos[-1]   # len(pedidos) se sale de la lista


# Error 4
# La cantidad llega como texto (así la regresa input). Calcula el total.
# Ejemplo: total_desde_texto("3", 15)  ->  45
def total_desde_texto(cantidad_texto, precio):
    return int(cantidad_texto) * precio   # convertir texto a número


# Error 5
# Regresa el mensaje de bienvenida (no lo imprime: lo REGRESA).
# Ejemplo: mensaje("Luis")  ->  "Hola, Luis"
def mensaje(nombre):
    return f"Hola, {nombre}"   # print no regresa nada


# Error 6
# Dice si la cafetería está abierta a cierta hora (abre a las 7 y cierra a las 20).
# Ejemplo: esta_abierto(7) -> True · esta_abierto(15) -> True · esta_abierto(20) -> False
def esta_abierto(hora):
    if hora >= 7 and hora < 20:   # a las 7 en punto ya está abierto
        return True
    else:
        return False
