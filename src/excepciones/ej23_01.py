def pedir_edad():
    comprobacion = False

    while not comprobacion:
        try:
            edad = int(input('Ingrese la edad: '))

            if edad < 0 or edad > 120:
                raise ValueError

            comprobacion = True

        except ValueError:
            print('Numero no valido')

        except:
            print('Error desconocido')

    return edad


def main():
    edad = pedir_edad()
    anios = ''

    for i in range(1, edad + 1):
        if i == edad:
            anios += str(i)
        elif i == (edad - 1):
            anios += str(i) + ' y '
        else:
            anios += str(i) + ', '

    print(f'Desde que naciste has cumplido {anios} años.')


if __name__ == '__main__':
    main()