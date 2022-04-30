def es_divisible(dividendo: int, divisor: int) -> bool:
    return dividendo % divisor == 0

def es_primo(numero: int) -> bool:
    for i in range(2, numero):
        if es_divisible(numero, i):
            return False
    return True        


def run():
    numero: int = int(input("Escribe un número: "))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()