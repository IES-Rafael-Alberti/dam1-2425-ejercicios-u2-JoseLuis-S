'''
Ej 22_10

Este algoritmo comprueba si el numero introducido es un numero primo o no

Funciones disponibles:
    * comprobarPrimo - comprueba si un numero es primo o no
    * pedirNum - pide un numero al usuario
    * comprobarNum - comprueba que un valor introducido sea un numero entero
    * main - funcion main
'''

def comprobar_primo(num: int) -> str:
    '''Comprueba si el numero introducido es un numero primo o no

    Args: 
        num (int): Numero a comprobar si es primo o no

    Returns:
        str: Devuelve un mensaje en funcion de si el numero es
        primo o no
    
    '''
    numDivisores = 0

    # Con este bucle for se calcula el numero de divisores,
    # comienza desde el 1 hasta 1 numero menos que el numero
    # introducido
    for i in range (1, num):
            # Si el modulo de la division es 0 se le suma un
            # divisor
            divisores = num % i
            if divisores == 0:
                numDivisores += 1

    # Si tiene mas de 1 divisor (ya que todos los numeros son divisibles
    # entre 1) no es un numero primo y viceversa
    if numDivisores > 1:
        return (f'El numero {num} no es un numero primo.')
    else:
        return (f'El numero {num} es un numero primo.')    

def pedir_num() -> int:
    ''' Pide un numero al usuario

    Returns:
        int: Devuelve el numero que introduce el usuario
    
    '''
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Introduce el numero a comprobar: '))

            while num < 0:
                num = int(input('Introduce el numero a comprobar (mayor a 0): '))

            comprobacion = True

        except ValueError:
            print('NUMERO NO VALIDO.')

        except:
            print('ERROR DESCONOCIDO.')

    return num


def main():
    '''Funcion main'''
    num = pedir_num()
    comprobacion = comprobar_primo(num)
    
    print(comprobacion)

if __name__ == '__main__':
    main()