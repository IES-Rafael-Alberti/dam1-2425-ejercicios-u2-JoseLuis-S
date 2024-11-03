'''
Ej 21_04

Este algoritmo comprueba si un numero es par o impar

Funciones disponibles:
    * num_par_o_impar - comprueba si un numero es par o impar
    * pedir_num - pide un numero al usuario
    * comprobar_num - comprueba que el valor introducido sea un numero
    entero natural
    * main - funcion main

'''
def num_par_o_impar(num: int) -> str:
    '''
    Comprueba si un numero es par o impar
    
    Args:
        num (int): Numero a comprobar

    Returns:
        str: Retorna una cadena de caracteres que indica si es par 
        o impar
    '''
    if num % 2 != 0:
        return 'impar'
    else:
        return 'par'

def pedir_num() -> int:
    ''' 
    Pide la edad al usuario
    
    Returns:
        int: Devuelve la edad del usuario

    '''
    num = input('Introduce un numero: ')

    while comprobar_num(num) is False:
        num = input('ERROR, introduce un numero valido: ')

    return int(num)

def comprobar_num(num: str) -> bool:
    '''
    Comprueba si lo que se ha introducido es un numero

    Args:
        num (str): Numero introducido por el usuario
    Returns:
        bool: Retorna True si es numero y False si no
    '''
    num = num.strip()

    for i in num:
        if i not in '0123456789-.':
            return False

def main():
    '''Funcion main'''
    num = pedir_num()
    resultado = num_par_o_impar(num)

    print(f'El numero {num} es un numero {resultado}.')


if __name__ == '__main__':
    main()