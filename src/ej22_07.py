def pedir_num():
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Introduce un numero para saber su tabla de multiplicar: '))
            while num < 0:
                num = int(input('Introduce un numero para la cuenta regresiva (mayor que 0): '))

            comprobacion = True

        except ValueError:
            print('\n**ERROR**\n Numero no valido.')
        
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