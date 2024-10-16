'''
Ej 21_05

Este algoritmo determina si una persona debe tributar o no en funcion 
de su edad y sus ingresos

Funciones disponibles:
    * resultado_final - muestra el resultado final del algoritmo
    * pedir_ingresos - pide los ingresos al usuario
    * comprobar_num - comprueba que los numeros introducidos sean numeros
    * pedir_edad - pide la edad al usuario
    * main - funcion main
'''
def resultado_final(edad: int, edad_tributar: int, cantidad_para_tributar: float) -> str:
    '''
    Muestra si la persona tiene que tributar o no

    Args:
        edad (int): Edad del usuario
        edad_tributar (int): Edad minima para tributar
        cantidad_para_tributar (float): Cantidad minima para tributar

    Returns:
        str: Retorna una cadena de caracteres con el resultado     
    
    '''
    if edad >= edad_tributar:
        ingresos = pedir_ingresos()
        if ingresos < cantidad_para_tributar:
            return 'Enhorabuena!! No has generado suficiente y el estado no te va a saquear.'
        else:
            return 'Enhorabuena!! Has generado suficientes ingresos, ahora el estado te va a saquear'
    else:
        return 'Todavia no tienes que tributar.'

def pedir_ingresos() -> float:
    '''
    Pide los ingresos al usuario
    
    Returns:
        int: Retorna el numero de ingresos que introduce el usuario
    '''
    ingresos = input('Introduce los ingresos que has tenido: ')

    while not comprobar_num(ingresos):
        ingresos = input('ERROR, introduce un numero valido: ')

    return float(ingresos)    

def comprobar_num(num: str) -> bool:
    '''
    Comprueba si lo que se ha introducido es un número válido.
    
    Args:
        num (str): Edad/Ingresos introducidos/a por el usuario.
    Returns:
        bool: Retorna True si es un número entero válido y False si no.
    '''
    num = num.strip()

    if not num.isdigit():
        return False
    return True

def pedir_edad() -> int:
    '''
    Solicita al usuario introducir una edad válida.
    
    Returns:
        int: Edad validada que sea mayor de 0 y menor de 120.
    '''
    edad = input('Introduce tu edad: ')

    while not comprobar_num(edad) or not (0 < int(edad) <= 120):
        edad = input('ERROR, introduce una edad válida (entre 1 y 120): ')

    return int(edad)

def main():
    '''Funcion main'''
    edad = pedir_edad()
    edad_tributar = 16
    cantidad_para_tributar = 1000
    resultado = resultado_final(edad, edad_tributar, cantidad_para_tributar)

    print(resultado)

if __name__ == '__main__':
    main()
