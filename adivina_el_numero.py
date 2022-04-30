from random import randint
def run() -> bool:
    numero_correto = randint(1,100)
    print(""" Bienvenido!
    he pensado en un número, intenta adivinarlo.
    pista! se encuentra entre 1 y 100, tienes 10 intentos.""")
    numero_jugador = int(input("escribe el número! podras ganarme?: "))
    for i in range(10):
        if(numero_jugador > numero_correto):
            print("el numero es más pequeño!")
        elif(numero_jugador < numero_correto):
            print("el numero es más grande")
        else:
            return True
        
        numero_jugador = int(input("esoge otro número: "))
    return False


if __name__ == '__main__':
    if(run()):
        print("me has vencido!!! nos veremos en otra partida")
    else:
        print("Sabrias que no podrias contra mi, mejor suerte la proxima")