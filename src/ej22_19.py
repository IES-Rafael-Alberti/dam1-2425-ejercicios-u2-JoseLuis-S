def comprobar_opcion(opcion):
    if opcion == 1:
        return 'Has elegido la opcion 1'
    else:
        return 'Has elegido la opcion 2'
    

def pedir_opcion():
    comprobacion = False
    
    while not comprobacion:
        try:
            opcion = int(input('Elige una opcion (1 - comenzar programa, 2 - imprimir listado, 3 - finalizar programa): '))

            if opcion not in (1, 2, 3):
                raise ValueError
            
            else:
                comprobacion = True

        except ValueError:
            print('Opcion no valida')

        except:
            print('Error desconocido')

    return opcion


def main():
    terminar = False

    while not terminar:
        opcion = pedir_opcion()

        if opcion == 3:
            terminar = True
        else:
            resultado = comprobar_opcion(opcion)
            print(resultado)


if __name__ == '__main__':
    main()