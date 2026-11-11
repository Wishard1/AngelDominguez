# =====================================================================
#  EJERCICIOS · MÓDULO 1: COMPLETA EL CÓDIGO
#
#  Cada función tiene uno o más espacios ___ (tres guiones bajos).
#  Cámbialos por lo que falta para que la función haga lo que dice.
#
#  Para revisar tu avance:   python revisar.py
#  Hazlo sin inteligencia artificial: todo lo vimos hoy en clase.
# =====================================================================


# Ejercicio 1 · Variables y operaciones
# Un cliente compra varias piezas del mismo producto. Regresa el total a pagar.
# Ejemplo: total_pedido(35, 3)  ->  105
def total_pedido(precio, cantidad):
    total = ___ * ___
    return total


# Ejercicio 2 · Texto con variables (f-string)
# Regresa un saludo con el nombre del cliente.
# Ejemplo: saludo("Ana")  ->  "Hola, Ana. Bienvenido a Café Nogal"
def saludo(nombre):
    return f"Hola, {___}. Bienvenido a Café Nogal"


# Ejercicio 3 · Decidir con if / elif / else
# Regresa el tamaño de la bebida según las onzas:
#   hasta 8 onzas -> "chico" · hasta 12 -> "mediano" · más de 12 -> "grande"
# Ejemplo: tamano_bebida(12)  ->  "mediano"
def tamano_bebida(onzas):
    if onzas <= 8:
        return "chico"
    elif onzas <= ___:
        return "mediano"
    else:
        return "___"


# Ejercicio 4 · Listas
# Agrega un producto al final del carrito y regresa el carrito.
# Ejemplo: agregar_al_carrito(["Concha"], "Capuchino")  ->  ["Concha", "Capuchino"]
def agregar_al_carrito(carrito, producto):
    carrito.___(producto)
    return carrito


# Ejercicio 5 · Ciclo for
# Suma todos los precios de la lista y regresa el total.
# Ejemplo: sumar_precios([35, 50, 15])  ->  100
def sumar_precios(precios):
    total = 0
    for precio in precios:
        total = total + ___
    return total


# Ejercicio 6 · Diccionarios
# Regresa el precio de un producto buscándolo en el menú.
# Ejemplo: precio_de({"Concha": 15, "Capuchino": 50}, "Capuchino")  ->  50
def precio_de(menu, producto):
    return menu[___]
