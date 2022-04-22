# Conversor de monedas de BsS a USD

import enum


def divisa_to_dolar(divisa, equivalente) -> float:
    return round(divisa / equivalente, 2)

def dolar_to_divisa(dolar, equivalente) -> float:
    return round(dolar * equivalente, 2)

def imprimir_listado_opciones(opciones: list) -> None:
    for indice, opcion in enumerate(opciones):
        print(f"{indice}. ${opcion}")

monedas = ["VES", "USD", "EUR", "ARS"]
equivalentes = [4.56, 1, 0.92, 114.08]

menu_dialogo_1 = """
Bienvenido al conversor de monedas 😁
¿Qué divisa deseas convertir?  🤔:
"""

menu_dialogo_2 = """
 Genial!! 😎 ¿a cuál moneda deseas convertir?
"""

quiero_convertir = True

while(quiero_convertir):

    print(menu_dialogo_1)
    imprimir_listado_opciones(monedas)
    opcion1 = int(input("opción: "))
    
    print(menu_dialogo_2)
    imprimir_listado_opciones(monedas)
    opcion2 = int(input("opción: "))

    monto = input("Ingrese el monto a convertir 🤑: ")
    monto = float(monto)

    conversion = divisa_to_dolar(monto, equivalentes[opcion1])
    conversion = dolar_to_divisa(conversion, equivalentes[opcion2])
    resultado = f"\nel resultado es: ${conversion}${monedas[opcion2]}\n"
    print(resultado)

    quiero_convertir = eval(input("¿Quiere intentar otra conversión? (True,False)"))

print("Gracias por usar la App, hasta la proxima 😶‍🌫️")