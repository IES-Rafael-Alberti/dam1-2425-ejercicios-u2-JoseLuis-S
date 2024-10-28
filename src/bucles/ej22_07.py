def pedir_num():
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Introduce un numero para saber su tabla de multiplicar (del 0 al 10): '))
            if num < 0 or num > 10:
                raise ValueError

            comprobacion = True

        except ValueError:
            print('\n**ERROR**\nNumero no valido.')
        
        except:
            print('Error desconocido.')
    
    return num


def main():
    num = pedir_num()
    
    print(f'\nLa tabla de multiplicar de {num} es:\n')

    for i in range (11):
        print(f'{num} * {i} = {num * i}')

if __name__ == '__main__':
    main()