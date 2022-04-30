def es_divisible(dividendo: int, divisor: int) -> bool:
    return dividendo % divisor == 0


def es_primo(dividendo: int) -> bool:
    for divisor in range(2, dividendo):
        if es_divisible(dividendo, divisor) == 0:
            return False

        elif (dividendo//divisor)  < divisor:
            break;

    return True   


def run():
    numero: int = int(input("Escribe un número: "))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()