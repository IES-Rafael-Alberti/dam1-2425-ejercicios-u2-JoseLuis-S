'''
Ej 21_02

Este algoritmo se encarga de pedir una contraseña y luego preguntar la contraseña para comprobar
si se ha introducido por segunda vez de manera correcta

Funciones disponibles:
    * comprobarContraseña - comprueba si el usuario ha escrito la contraseña con exito
    Comprueba si el usuario ha escrito la contraseña con exito
    * preguntarContraseña - pregunta la contraseña al usuario
    * pedirContraseña - pide una contraseña al usuario
    * main - funcion main

'''

def comprobarContraseña(contraseña: str, contraseñaIntroducida: str) -> str:
    ''' Comprueba si la contraseña introducida es igual a la contraseña    
    
    Args:
        contraseña (str): Contraseña del usuario
        contraseñaIntroducida (str): Contraseña a comparar

    Returns:
        str: Retorna un mensaje en funcion desi la contraseña es correcta o no

    '''

    # Si la contraseña introducida no es igual a la anterior
    # muestra mensaje de error
    if contraseña != contraseñaIntroducida:
        return 'Has introducido la contraseña incorrecta.'
    # Si la contraseña introducida es igual a la anterior
    # muestra mensaje de exito
    if contraseña == contraseñaIntroducida:
        return 'Has introducido la contraseña con exito.'

def preguntarContraseña() -> str:
    ''' Pregunta al usuario la contraseña que ha escrito previamente
    
    Returns:
        str: La contraseña a comprobar en minusculas

    '''
    contreñaIntroducida = input('Dime la contraseña: ')
    # Devuelve la contraseña en minusculas
    return contreñaIntroducida.lower()

def pedirContraseña() -> str:
    ''' Pide al usuario una contraseña

    Returns:
        str: Retorna la contraseña escrita en minusculas
    
    '''
    contraseña = input('Introduce la contraseña: ')
    # Devuelve la contraseña en minusculas
    return contraseña.lower()

def main():
    ''' Funcion main '''
    contraseña = pedirContraseña()
    
    contraseñaIntroducida = preguntarContraseña()

    resultado = comprobarContraseña(contraseña, contraseñaIntroducida)
    
    print(resultado)

if __name__ == "__main__":
    main()