'''
Ej 21_01

Este algoritmo pregunta la edad de un usuario para comprobar si es mayor o menor de 
edad. En funcion de si es mayor o menor de edad muestra un mensaje u otro

Funciones disponibles:
    * comprobarMayoriaEdad - comprueba si la edad introducida es mayor o menor 
    de 18 años
    * pedirEdad - pide la edad al usuario
    * comprobarEdad - comprueba que la edad introducida sea un numero entero
    * main - funcion main
'''

def comprobarMayoriaEdad(edad: int) -> str:
    ''' 
    Comprueba si la edad introducida es mayor o menor a 18 años

    Args:
        edad (int): La edad del usuario a comprobar
    Returns:
        str: Retorna un mensaje en funcion de si es menor o mayor de edad
    '''
    # Si la edad es mayor o igual a 18 es mayor de edad
    if edad >= 18:
        return 'Felicidades!! Puedes tomarte una cerveza e ir a la carcel.'
    # Si la edad introducida es menor a 18 es menor de edad
    else:
        return 'Felicidades!! Aun puedes no tener responsabilidades.'

def pedirEdad() -> int:
    ''' 
    Pide la edad al usuario
    
    Returns:
        int: Devuelve la edad del usuario

    '''
    # Lee el dato introducido
    edad = input('Introduce tu edad: ')

    # Mientras que la funcion comprobarEdad no devuelva que el dato
    # introducido es un entero pedira la edad
    while comprobarEdad(edad) is not True:
        edad = input('ERROR, introduce una edad valida: ')
        
    return int(edad)

def comprobarEdad(edad: str) -> bool:
    ''' 
    Comprueba que la edad introducida sea un numero entero

    Args:
        edad (str): Edad del usuario

    Returns:
        bool: Retorna True si es numero entero y False si no

    '''
    # Elimina los espacios tras convertir num en str
    edad = edad.strip()

    # Comprueba que la edad introducida unicamente contenga numeros enteros naturales
    for i in edad:
        if i not in '0123456789':
            return False 
        
    # La edad no puede ser mayor a 120 años
    if edad > 120:
        return False

    # Si todas las anteriores no se cumplen significa que es un entero natural,
    # por lo que devuelve True
    return True

def main():
    '''Funcion main'''
    edad = pedirEdad()
    resultado = comprobarMayoriaEdad(edad)
    print(resultado)
    
if __name__ == "__main__":
    main()
