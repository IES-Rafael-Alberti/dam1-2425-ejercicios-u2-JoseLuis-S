def pedir_num():
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Ingrese un numero entero: '))

            if num < 0:
                raise ValueError

            comprobacion = True

        except ValueError:
            print('Numero no valido')

        except:
            print('Error desconocido')

    return num


def main():
    num = pedir_num()
    print(num)

if __name__ == '__main__':
    main()