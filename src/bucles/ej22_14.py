def sumar_nums(num, suma_nums):
    return suma_nums + num


def pedir_num():
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Introduce un numero entero: '))

            comprobacion = True

        except ValueError:
            print('Numero no valido.')
        
        except:
            print('Error desconocido.')
        
    return num


def main():
    num = pedir_num()
    suma_nums = 0
    suma_nums = sumar_nums(num, suma_nums)

    while num != 0:
        suma_nums = sumar_nums(num, suma_nums)
        print('\nPara terminar el script escriba (0).\n')
        num = pedir_num()

    print(f'\nLa suma de todos los numeros introducidos es {suma_nums}.\n')
    

if __name__ == '__main__':
    main()