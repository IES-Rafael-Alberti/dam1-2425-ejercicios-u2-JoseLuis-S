def pedir_num() -> int:
    ''' Pide un numero al usuario

    Returns:
        int: Devuelve el numero que introduce el usuario
    
    '''
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Introduce un numero entero de dos digitos o mas: '))

            while num < 10:
                num = int(input('Introduce un numero entero de dos digitos o mas: '))

            comprobacion = True

        except ValueError:
            print('NUMERO NO VALIDO.')

        except:
            print('ERROR DESCONOCIDO.')

    return str(num)


def main(): 
    num1 = pedir_num()
    nums_separados = list(num1)
    suma = 0

    for i in range (len(nums_separados)):
        suma += int(nums_separados[i])

    print(f'La suma de los numeros {nums_separados} es: {suma}')

if __name__ == '__main__':
    main() 