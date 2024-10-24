def pedir_altura():
    comprobacion = False

    while not comprobacion:
        try:
            altura = int(input('Introduce la altura del triangulo: '))

            while altura < 0:
                altura = int(input('Introduce la altura del triangulo: '))

            comprobacion = True

        except ValueError:
            print('\n**ERROR**\n Numero no valido.')
        
        except:
            print('Error desconocido.')
    
    return altura


def main():
    altura = pedir_altura()

    for i in range (1, altura + 1):
        print(('*') * i)


if __name__ == '__main__':
    main()