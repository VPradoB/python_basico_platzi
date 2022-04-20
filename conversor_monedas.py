# Conversor de monedas de BsS a USD

def bolivar_to_dolar(bolivar, equivalente) -> float:
    return round(bolivar / equivalente, 2)

def dolar_to_bolivar(dolar, equivalente) -> float:
    return round(dolar * equivalente, 2)


while(quiero_convertir):
    print("Escoja un tipo de conversión:")
    print("1. BsS-> USD")
    print("1. USD -> BsS")

    opcion = input("opción: ")
    quiero_convertir = True
    monto = input("Ingrese el monto a convertir: ")
    monto = float(monto)
    equivalente = 4.56

    if(opcion == '1'):
        resultado = bolivar_to_dolar(monto, equivalente)
        print(f'el monto en dolares es: ${resultado}')
    elif(opcion == '2'):
        resultado = dolar_to_bolivar(monto, equivalente)
        print(f'el monto en bolivares es: ${resultado}')
    else:
        print("la opción no es valida, escoja una de las alternativas (1, 2)")
    quiero_convertir = eval(input("¿Quiere intentar otra conversión? (True,False)"))

print("Gracias por usar la App")