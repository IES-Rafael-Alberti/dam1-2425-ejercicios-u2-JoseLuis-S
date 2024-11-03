def pedir_frase():
    frase = input('Introduce una frase: ')
    return frase


def main():
    salir = False

    while not salir:
        frase = pedir_frase()

        if frase.lower() == 'salir':
            salir = True
        else:
            print(frase)


if __name__ == '__main__':
    main()