def crear_serie(num):
    serie = ''

    for i in range(1, num + 1, 2):
        if num % 2 == 0:
            if i == (num - 3):
                serie += str(i) + ' y '
            elif i == (num - 1):
                serie += str(i)
            else:
                serie += str(i) + ', '
        else:
            if i == (num - 1) or i == (num - 2):
                serie += str(i) + ' y '
            elif i == num:
                serie += str(i)
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
    serie = crear_serie(num)

    print(f'La serie de 1 hasta {num} de numeros impares es {serie}.')

if __name__ == '__main__':
    main()