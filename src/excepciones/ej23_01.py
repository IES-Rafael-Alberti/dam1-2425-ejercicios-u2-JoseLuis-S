'''
Ej23_01

Este algoritmo crea una serie con los años que ha cumplido el usuario
en funcion de su edad

Funciones disponibles:
    * generar_serie - genera la serie de años cumplidos
    * pedir_edad - pide la edad al usuario
    * main - funcion principal
'''
def generar_serie(edad: int) -> str:
    '''
    Esta funcion genera la serie de años cumplidos por el usuario

    Args:
        edad (int): Edad del usuario

    Returns:
        str: Serie de años cumplidos por el usuario
    '''
    serie = ''

    for i in range(1, edad + 1): # Bucle que genera la serie
        if i == edad:
            serie += str(i)
        elif i == (edad - 1):
            serie += str(i) + ' y '
        else:
            serie += str(i) + ', '

    return serie

def pedir_edad() -> int:
    '''
    Esta funcion pide una edad al usuario y comprueba que sea
    mayor a 0 y menor que 120

    Returns:
        int: Edad introducida por el usuario
    '''
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
    ''' Funcion principal '''
    edad = pedir_edad()
    serie = generar_serie()

    print(f'Desde que naciste has cumplido {serie} años.')


if __name__ == '__main__':
    main()