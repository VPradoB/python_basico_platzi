def es_palindromo(oracion):
    oracion = oracion.replace(' ','')
    oracion = oracion.lower()
    return oracion[::] == oracion[::-1]


def run():
    oracion : str = input("Ingrese la oración a verificar: ")

    if(es_palindromo(oracion)):
        print("la oración es palindroma!!")
    else:
        print("la oración no es palindroma :(")


if __name__ == '__main__':
    run()