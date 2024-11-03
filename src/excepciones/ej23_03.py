def generar_cuenta_atras(num):
    serie = ''

    for i in reversed(range(num + 1)):
        if i == 0:
            serie += str(i)
        elif i == 1:
            serie += str(i) + ' y '
        else:
            serie += str(i) + ', '

    return serie

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
    serie = generar_cuenta_atras(num)

    print(f'La cuenta regresiva es: {serie}.')

if __name__ == '__main__':
    main()