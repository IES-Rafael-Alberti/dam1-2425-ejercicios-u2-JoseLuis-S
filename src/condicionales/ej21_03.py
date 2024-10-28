'''

Ej 21_03

Este algoritmo calcula la division entre dos numeros

Funciones disponibles:
    * division - calcula la division 
    * pedir_num - pide un dividendo y un divisor
    * comprobar_num - comprueba que se haya introducido un numero
    * comprobar_cero - comprueba si el divisor es igual a 0
    * main - funcion principal

'''

def division(num1: float, num2: float) -> float:
    '''
    Calcula la division entre los dos numeros
    
    Args:
        num1 (float): Dividendo de la division
        num2 (float): Divisor de la division
    
    Returns: 
        float: Retorna el resultado de la division
    '''
    return num1/num2

def pedir_num(index: int) -> float:
    '''
    Pide los dos elementos de la division al usuario

    Args:
        index (int): Orden para saber si pedir el dividendo o divisor

    Returns:
        float: Retorna el numero introducido
    '''
    mensajes = ['Introduce el dividendo de la division: ', 'Introduce el divisor de la division: ']
    
    num = input(mensajes[index])

    while not comprobar_num(num):
        num = input('ERROR, número no válido: ')

    num = float(num)

    if index == 1:  
        while not comprobar_cero(num):
            num = float(input('(No se puede dividir entre 0)\nIntroduce otro numero:  '))

    return num
            
def comprobar_num(num: str) -> bool:
    '''
    Comprueba si lo que se ha introducido es un numero

    Args:
        num (str): Numero introducido por el usuario
    Returns:
        bool: Retorna True si es numero y False si no
    '''
    num = num.strip()

    if num.isdigit():
        return True
    else:
        return False

def comprobar_cero(num: float) -> bool:
    '''
    Comprueba si el divisor es igual a 0

    Args:
        num (float): Divisor
    
    Returns:
        bool: Retorna True si es distinto de cero y False si no
    '''
    return num != 0
    
def main():
    '''Funcion main'''
    num1 = pedir_num(0)
    num2 = pedir_num(1)
    resultado = division(num1, num2)
    print(round(resultado, 2))

if __name__ == '__main__':
    main() 